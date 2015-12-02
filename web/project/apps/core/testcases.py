"""
Base test cases for core.
"""
from django.test import TestCase


class BaseFormTestCase(TestCase):
    """
    Base test case for forms providing usefull assertion methods.
    """
    form_class = None
    valid_data = {}

    def get_form_kwargs(self):
        return {}

    def get_valid_data(self):
        """
        Return a valid data dict for the form class.
        Should be overriden by children.
        """
        return self.valid_data

    def assertFormError(self, form, error_message):
        """
        Assert that a given error appened on the form.
        """
        self.assertIn(error_message, form.errors['__all__'])

    def assertFieldError(self, form, field_name, error_msg=""):
        """
        Assert that a given error appened on the field.
        """
        self.assertIn(field_name, form.errors)
        if error_msg:
            self.assertEqual(form.errors[field_name][0], error_msg)

    def assertFieldInvalid(
            self,
            field_name,
            value,
            error_msg="",
            form_error=False):
        """
        Assert that the given field and value will invalidate the form.
        If form_error is true search for the error at form level
        instead of field level.
        """
        invalid_data = self.get_valid_data().copy()
        invalid_data[field_name] = value
        f = self.assertInvalid(invalid_data)
        if error_msg:
            if form_error:
                self.assertFormError(f, error_msg)
            else:
                self.assertFieldError(f, field_name, error_msg)

    def assertInvalid(self, data):
        """
        Assert that the form is invalid.
        """
        f = self.form_class(data, **self.get_form_kwargs())
        self.assertFalse(f.is_valid())
        return f

    def assertValid(self, **kwargs):
        """
        Assert that the form is valid.
        """
        valid_data = kwargs.get('data', self.get_valid_data())
        f = self.form_class(valid_data, **self.get_form_kwargs())
        self.assertTrue(f.is_valid())
        return f

    def assertFieldOptional(self, field_name):
        """
        Assert that a field is optional.
        """
        valid_data = self.get_valid_data().copy()
        valid_data.pop(field_name)
        self.assertValid(data=valid_data)

    def assertFieldRequired(self, field_name):
        """
        Assert that a field is required.
        """
        invalid_data = self.get_valid_data().copy()
        invalid_data.pop(field_name)
        if self.form_class(invalid_data, **self.get_form_kwargs()).is_valid():
            self.fail("'{0}' shall be required".format(field_name))

    def assertRequired(self):
        """
        Assert that all fields are required.
        """
        for key, field in self.form_class.base_fields.items():
            self.assertFieldRequired(key)
