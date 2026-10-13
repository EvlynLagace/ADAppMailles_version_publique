import json

from appTricot.domaine.echantillon import Echantillon
from appTricot.models import EchantillonModel

def charger_user_echantillon(user):
    echantillon_model = (
        charger_user_echantillons(user)
        .last()
    )

    if echantillon_model is None:
        return None

    return Echantillon(
        largeur_cm=echantillon_model.largeur_cm,
        hauteur_cm=echantillon_model.hauteur_cm,
        nb_mailles=echantillon_model.nb_mailles,
        nb_rangs=echantillon_model.nb_rangs,
        nom_echantillon=echantillon_model.nom_echantillon,
    )

def charger_user_echantillons(user):
    return EchantillonModel.objects.filter(user=user).order_by("id")

def convertir_echantillon_model(echantillon_model):
    return Echantillon(
            largeur_cm=echantillon_model.largeur_cm,
            hauteur_cm=echantillon_model.hauteur_cm,
            nb_mailles=echantillon_model.nb_mailles,
            nb_rangs=echantillon_model.nb_rangs,
            nom_echantillon=echantillon_model.nom_echantillon,
        )

def charger_user_echantillon_par_id(user, echantillon_id):
    echantillon_model = (
        charger_user_echantillons(user)
        .filter(id=echantillon_id)
        .first()
    )

    if echantillon_model is None:
        return None

    return convertir_echantillon_model(echantillon_model)

def charger_echantillon(chemin):
    with open(chemin, "r", encoding="utf-8") as f:
        data = json.load(f)

    return Echantillon.from_dict(data)

def creer_echantillon(user, echantillon, nom_echantillon):
    return EchantillonModel.objects.create(
        user=user,
        nom_echantillon=nom_echantillon,
        largeur_cm=echantillon.largeur_cm,
        hauteur_cm=echantillon.hauteur_cm,
        nb_mailles=echantillon.nb_mailles,
        nb_rangs=echantillon.nb_rangs,
    )

def trouver_ou_creer_echantillon(user, echantillon):
    echantillon_model = EchantillonModel.objects.filter(
        user=user,
        largeur_cm=echantillon.largeur_cm,
        hauteur_cm=echantillon.hauteur_cm,
        nb_mailles=echantillon.nb_mailles,
        nb_rangs=echantillon.nb_rangs,
        nom_echantillon=echantillon.nom_echantillon
    ).last()

    if echantillon_model is not None:
        return echantillon_model

    return creer_echantillon(
        user,
        echantillon,
        echantillon.nom_echantillon,
    )