from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User
from .models import Profile

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model   = Profile
        fields  = (
            'masker_medis', 
            'masker_n95', 
            'hazmat',
            'apron',
            'hand_sanitizer',
            'sarung_tangan',
            'face_shield',
            'sepatu_boots'
        )

