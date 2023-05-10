from app1.models import user
from django.contrib.auth.forms import forms

class userForm(forms.ModelForm):
   class Meta:
        model = user
        fields = '__all__'