from django import forms
from django.forms import ModelForm
from .models import Student
# creating a form

class PostForm(ModelForm):
    class Meta:
        model = Student
        fields = ["name", "phone", "address"]

    def clean(self):
        super(PostForm, self).clean()
        name = self.cleaned_data.get('name')
        address = self.cleaned_data.get('address')
        if len(name) < 3:
            self._errors['name'] = self.error_class(['at least 3 character'])
        if len(address) < 5:
            self._errors['address'] = self.error_class(['address at least 5 character'])
        return self.cleaned_data
