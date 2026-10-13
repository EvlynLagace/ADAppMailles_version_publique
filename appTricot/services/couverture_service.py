
import json

from appTricot.domaine.couverture import Couverture
from appTricot.models import CouvertureModel
from appTricot.services.echantillon_service import convertir_echantillon_model, trouver_ou_creer_echantillon
from appTricot.services.motifs_service import charger_motifs


def get_couverture_domaine():
    from ..domaine.couverture import Couverture
    from ..models import CouvertureModel

    db = CouvertureModel.objects.first()

    if not db:
        return None

    return Couverture(
        largeur_cm=db.largeur_cm,
        hauteur_cm=db.hauteur_cm,
    )

def sauvegarder_couverture(couverture, chemin):
    with open(chemin, 'w', encoding="utf-8") as fichier:
        json.dump(
            couverture.to_dict(),
            fichier,
            indent=4,
            ensure_ascii=False
        )

def charger_couverture(chemin, catalogue):
    with open(chemin, "r", encoding="utf-8") as f:
        data = json.load(f)

    return Couverture.from_dict(data, catalogue)

def creer_couverture(user, couverture, echantillon, nom_couverture):

    echantillon_model = trouver_ou_creer_echantillon(user, echantillon)
    
    return CouvertureModel.objects.create(
        user=user,
        echantillon=echantillon_model,
        nom_couverture=nom_couverture,
        largeur_cm=couverture.largeur_cm,
        hauteur_cm=couverture.hauteur_cm,
        tuiles=couverture.tuiles_to_dict(),
    )

def charger_user_couverture(user):
    couverture_model = (
        charger_user_couvertures(user)
        .last()
    )

    if couverture_model is None:
        return None

    catalogue = charger_motifs()

    data = {
        "largeur_cm":couverture_model.largeur_cm,
        "hauteur_cm":couverture_model.hauteur_cm,
        "tuiles": couverture_model.tuiles,
        "nom_couverture": couverture_model.nom_couverture,
    }

    return Couverture.from_dict(data, catalogue)

def charger_user_couvertures(user):
    return CouvertureModel.objects.filter(user=user).order_by("id")

def charger_user_couverture_par_id(user, couverture_id):
    couverture_model = (
        charger_user_couvertures(user)
        .filter(id=couverture_id)
        .first()
    )

    if couverture_model is None:
        return None

    catalogue = charger_motifs()


    data = {
        "largeur_cm":couverture_model.largeur_cm,
        "hauteur_cm":couverture_model.hauteur_cm,
        "tuiles": couverture_model.tuiles,
        "nom_couverture": couverture_model.nom_couverture,
    }

    couverture = Couverture.from_dict(data, catalogue)
    echantillon = convertir_echantillon_model(
        couverture_model.echantillon
    )

    return couverture, echantillon