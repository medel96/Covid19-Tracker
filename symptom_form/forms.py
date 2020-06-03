from django import forms
from .models import Sie_Utilisateur

class UtiForm(forms.ModelForm):

    class Meta:
        model = Sie_Utilisateur
        fields = ('UTI_NOM', 'UTI_PRENOM','UTI_CIVILITE', 'UTI_EMAIL', 'UTI_SUPPRIME', 'UTI_ADRESSE', 'UTI_NUMBER')
