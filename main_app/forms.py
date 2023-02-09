from django.forms import ModelForm
from .models import Weilder

class WeilderForm(ModelForm):
    class Meta:
        model = Weilder
        fields = ['character','is_hero','phase_of_use']
