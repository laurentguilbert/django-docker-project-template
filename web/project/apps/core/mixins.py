"""
Mixins for core.
"""
import json

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.utils.encoding import force_text
from django.utils.functional import Promise


class LazyEncoder(DjangoJSONEncoder):

    def default(self, obj):
        if isinstance(obj, Promise):
            return force_text(obj)
        return super(LazyEncoder, self).default(obj)


class JSONResponseMixin(object):
    response_status = 200

    def error_to_response(self, message="", error_status=400):
        return HttpResponse(status=error_status, content=message)

    def render_to_response(self, context={}):
        return HttpResponse(
            status=self.response_status,
            content=self.convert_context_to_json(context),
            content_type='application/json'
        )

    def convert_context_to_json(self, context):
        return json.dumps(context, cls=LazyEncoder)
