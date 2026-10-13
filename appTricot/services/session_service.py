from appTricot.domaine.couverture import Couverture
from appTricot.domaine.echantillon import Echantillon
from appTricot.services.motifs_service import charger_motifs

COUVERTURE_SESSION_VERSION = 2


def get_echantillon_session(request):
    params = request.session.get("echantillon", {})

    return Echantillon(**params)

def get_couverture_session(request):

    version =request.session.get("couverture_version")

    if version != COUVERTURE_SESSION_VERSION:
        request.session.pop("couverture", None)
        request.session["couverture_version"] = COUVERTURE_SESSION_VERSION
        return Couverture()

    data = request.session.get("couverture", {})

    if "tuiles" in data:
        catalogue = charger_motifs()

        return Couverture.from_dict(
            data,
            catalogue,
        )
    
    return Couverture(**data)

def save_couverture_session(request, couverture):
    request.session["couverture"]=couverture.to_dict()
    request.session["couverture_version"] = COUVERTURE_SESSION_VERSION

def save_echantillon_session(request, echantillon):
    request.session["echantillon"]=echantillon.to_dict()
