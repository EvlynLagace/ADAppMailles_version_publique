from appTricot.services.session_service import get_couverture_session, get_echantillon_session, save_couverture_session
from .motifs_service import charger_motifs
from .tuile_service import selectionner_motif

def get_current_couverture(request):
    return build_couverture(request)

def build_couverture(request):

    couverture = get_couverture_session(request)

    if couverture is None:
        return None

    if not couverture.tuiles:
        generer_contenu_couverture(request, couverture)

    return couverture

def reset_couverture(request):
    request.session.pop("couverture", None)

def reset_tuiles_couverture(request):
    couverture = get_couverture_session(request)

    if couverture is None:
        return

    couverture.tuiles = []
    generer_contenu_couverture(request, couverture)

def generer_contenu_couverture(request, couverture):
    couverture.generer_tuiles()

    catalogue = charger_motifs()
    echantillon = get_echantillon_session(request)

    selectionner_motif(couverture, echantillon, catalogue)

    save_couverture_session(request, couverture)