from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profil, Commentaire, Message

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = Profil
        fields = ('username', 'email', 'password1', 'password2')

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ('contenu',)
        widgets = {
            'contenu': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Votre commentaire...'})
        }

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('nom', 'telephone', 'contenu')
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': 'Votre nom'}),
            'telephone': forms.TextInput(attrs={'placeholder': 'Votre téléphone'}),
            'contenu': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Votre message...'})
        }