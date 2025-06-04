from django import forms
from .models import Influencer

class InfluencerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Influencer
        fields = ["code", "commission"]
        widgets = {
            "code": forms.TextInput(attrs={"placeholder": "Código único"}),
            "commission": forms.NumberInput(attrs={"step": "0.01"}),
        }
