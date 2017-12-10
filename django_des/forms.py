from django.forms import ModelForm, PasswordInput
from django_des.models import DynamicEmailConfiguration


class DynamicEmailConfigurationForm(ModelForm):
    class Meta:
        model = DynamicEmailConfiguration
        exclude = []
        widgets = {
            "password": PasswordInput(render_value=True),
        }
