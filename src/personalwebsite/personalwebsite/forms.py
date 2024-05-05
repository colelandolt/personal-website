from django import forms
from django.core.validators import validate_email

class LandingPageForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(validators=[validate_email])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            attributes = {
                "class": "form-control",
                "id": field,
                "placeholder": f"Your {field}"
            }
            self.fields[field].widget.attrs.update(attributes)