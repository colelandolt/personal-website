from django import forms
from django.core.validators import validate_email

from .models import Subscriber

class SubscriberModelForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        fields = ["name", "email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            attributes = {
                "class": "form-control",
                "id": field,
                "placeholder": f"Your {field}"
            }
            self.fields[field].widget.attrs.update(attributes)