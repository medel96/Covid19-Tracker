from django.db import models

# Create your models here.

class Sie_Utilisateur(models.Model):
    UTI_NOM = models.CharField(max_length=50)
    UTI_PRENOM = models.CharField(max_length=50)
    UTI_CIVILITE = models.CharField(max_length=1)
    UTI_EMAIL = models.CharField(max_length=50)
    UTI_SUPPRIME = models.BooleanField()
    UTI_ADRESSE = models.CharField(max_length=500)
    UTI_NUMBER = models.CharField(max_length=3, default="0")

    def __str__(self):   #méthoce qui returne un string con el nombre de l'utilisateur
        return self.UTI_NOM
