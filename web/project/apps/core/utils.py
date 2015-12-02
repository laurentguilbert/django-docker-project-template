"""
Utils for core.
"""
import os
import datetime

from PIL import Image

from django.conf import settings as django_settings


def verify_image(file):
    # http://stackoverflow.com/questions/5770660/django-imagefield-validation-is-it-sufficient
    try:
        # load() is the only method that can spot a truncated JPEG
        # but it cannot be called sanely after verify()
        trial_image = Image.open(file)
        trial_image.load()

        # Since we're about to use the file again we have to reset the
        # file object if possible.
        if hasattr(file, 'reset'):
            file.reset()

        # verify() is the only method that can spot a corrupt PNG
        # but it must be called immediately after the constructor.
        trial_image = Image.open(file)
        trial_image.verify()
    except Exception:  # PIL doesn't recognize it as an image.
        return False
    return True


def save_file(dest_path, f, filename):
    original_name, file_extension = os.path.splitext(f.name)
    filename = u"{0}-{1}{2}".format(
        filename,
        datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'),
        file_extension,
    )
    url = '/' + dest_path + '/' + filename
    path = django_settings.MEDIA_ROOT + url
    destination = open(path, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    return {
        'path': path,
        'filename': filename,
        'url': u"{0}{1}".format(django_settings.MEDIA_URL, url),
    }
