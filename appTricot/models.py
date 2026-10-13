from django.contrib.auth.models import User
from django.db import models

class EchantillonModel(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="echantillons",
    )
    nom_echantillon = models.CharField(max_length=100)
    largeur_cm = models.IntegerField(default=10)
    hauteur_cm = models.IntegerField(default=10)
    nb_mailles = models.PositiveIntegerField(default=20)
    nb_rangs = models.PositiveIntegerField(default=27)

class CouvertureModel(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="couvertures",
    )

    echantillon = models.ForeignKey(
        EchantillonModel,
        on_delete=models.PROTECT,
        related_name="couvertures",
    )

    nom_couverture = models.CharField(max_length=100)

    largeur_cm = models.IntegerField(default=125)
    hauteur_cm = models.IntegerField(default=150)
    tuiles = models.JSONField()