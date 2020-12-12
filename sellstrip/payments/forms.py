from django.forms import ModelForm
from .models import check

class checkoutform(ModelForm):
    class Meta:
        model = check
        fields = '__all__'
