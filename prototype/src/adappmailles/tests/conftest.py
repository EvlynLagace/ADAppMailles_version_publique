import pytest

from adappmailles.modele.echantillon import Echantillon

@pytest.fixture
def echantillon_defaut():
    return Echantillon(largeur_cm=10, hauteur_cm=10, nb_mailles=10, nb_rangs=10)