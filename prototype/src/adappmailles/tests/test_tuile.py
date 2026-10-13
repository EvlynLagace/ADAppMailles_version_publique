from adappmailles.modele.echantillon import Echantillon
from adappmailles.modele.maille import Maille, TypeMaille
from adappmailles.modele.motif import Motif
from adappmailles.modele.rang_instructions import RangInstructions
from adappmailles.modele.tuile import Tuile

def test_default():
    t = Tuile()

    assert t.largeur_cm == 100
    assert t.hauteur_cm == 100
    assert t.nb_mailles is None
    assert t.nb_rangs is None
    assert t.motif is None

def test_tuile_creation_dimensions():
    t = Tuile(largeur_cm=50, hauteur_cm=50)
    assert t.largeur_cm == 50
    assert t.hauteur_cm == 50
    assert t.nb_mailles is None
    assert t.nb_rangs is None
    assert t.motif is None

def test_dimensions_defaut(echantillon_defaut):
    t = Tuile()
    t.initialiser_dimensions(echantillon_defaut)
    assert t.nb_mailles == 100
    assert t.nb_rangs == 100

def test_dimensions_mailles_cm_fraction():
    t = Tuile(largeur_cm=10, hauteur_cm=100)
    e = Echantillon(largeur_cm=20, nb_mailles = 10)
    t.initialiser_dimensions(e)
    assert t.nb_mailles == 5


def test_dimensions_mailles_cm_entier_et_fraction():
    t = Tuile(largeur_cm=20, hauteur_cm=100)
    e = Echantillon(largeur_cm=15, nb_mailles = 100)
    t.initialiser_dimensions(e)
    assert t.nb_mailles == 134

def creer_motif(repetees=0, ajoutees_avant=0, ajoutees_apres=0):
    instruction = RangInstructions(
        repetees=[(Maille(TypeMaille.ENDROIT), repetees)] if repetees else [],
        avant=[(Maille(TypeMaille.ENDROIT), ajoutees_avant)] if ajoutees_avant else [],
        apres=[(Maille(TypeMaille.ENDROIT), ajoutees_apres)] if ajoutees_apres else [],
    )

    return Motif(
        nom_motif="test",
        instructions=[instruction]
    )

def test_motif_compatible_exact():
    t = Tuile()
    t.nb_mailles = 14

    # 2 mailles ajoutées + multiple de 4
    motif = creer_motif(repetees=4, ajoutees_avant=1, ajoutees_apres=1)

    assert t.motif_est_compatible(motif)


def test_motif_incompatible():
    t = Tuile()
    t.nb_mailles = 13

    motif = creer_motif(repetees=4, ajoutees_avant=1, ajoutees_apres=1)

    assert not t.motif_est_compatible(motif, tolerance=0)


def test_motif_compatible_avec_tolerance():
    t = Tuile()
    t.nb_mailles = 13

    motif = creer_motif(repetees=4, ajoutees_avant=1, ajoutees_apres=1)

    assert t.motif_est_compatible(motif, tolerance=1)

def test_motif_trop_petit():
    t = Tuile()
    t.nb_mailles = 3

    motif = creer_motif(repetees=4, ajoutees_avant=1, ajoutees_apres=1)

    assert not t.motif_est_compatible(motif, tolerance=0)

def test_motif_sans_repetition():
    t = Tuile()
    t.nb_mailles = 2

    motif = creer_motif(repetees=0, ajoutees_avant=1, ajoutees_apres=1)

    assert t.motif_est_compatible(motif)