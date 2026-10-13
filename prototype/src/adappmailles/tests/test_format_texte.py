
from adappmailles.modele.maille import Maille, TypeMaille
from adappmailles.modele.motif import Motif
from adappmailles.modele.rang import Rang, TypeRang
from adappmailles.services.format_texte import compresser_mailles, motif_vers_texte, rang_vers_texte

def K(): return Maille(TypeMaille.ENDROIT)
def P(): return Maille(TypeMaille.ENVERS)

def test_compresser_mailles_simple():
    mailles = [
        Maille(TypeMaille.ENDROIT),
        Maille(TypeMaille.ENDROIT),
        Maille(TypeMaille.ENDROIT),
        Maille(TypeMaille.ENVERS),
        Maille(TypeMaille.ENVERS),
        Maille(TypeMaille.ENDROIT),
    ]

    resultat = compresser_mailles(mailles)

    assert resultat == "K3, P2, K"
    assert compresser_mailles([Maille(TypeMaille.ENDROIT)]) == "K"
    assert compresser_mailles([K(), P(), K()]) == "K, P, K"

def test_sequence_mailles_simple():
    mailles = [
        Maille(TypeMaille.ENDROIT),
        Maille(TypeMaille.ENVERS),
        Maille(TypeMaille.ENDROIT),
        Maille(TypeMaille.ENVERS),
        Maille(TypeMaille.ENDROIT),
        Maille(TypeMaille.ENVERS),
    ]

    resultat = compresser_mailles(mailles)

    assert resultat == "K, P, K, P, K, P"

def test_plusieurs_blocs():
    mailles = [K(), K(), P(), P(), P(), K(), K(), K(), P()]

    assert compresser_mailles(mailles) == "K2, P3, K3, P"

def test_rang_vers_texte_simple():
    rang = Rang(
        type_rang=TypeRang.ENDROIT,
        mailles=[
            Maille(TypeMaille.ENDROIT),
            Maille(TypeMaille.ENDROIT),
            Maille(TypeMaille.ENDROIT),
            Maille(TypeMaille.ENVERS),
        ]
    )

    resultat = rang_vers_texte(rang, 0)

    assert resultat == "Rang 1 (endroit) : K3, P"

def test_rang_vers_texte_alternance():
    rang = Rang(
        type_rang=TypeRang.ENVERS,
        mailles=[
            Maille(TypeMaille.ENDROIT),
            Maille(TypeMaille.ENVERS),
            Maille(TypeMaille.ENDROIT),
        ]
    )

    resultat = rang_vers_texte(rang, 1)

    assert resultat == "Rang 2 (envers) : K, P, K"

def test_rang_vers_texte_vide():
    rang = Rang(
        type_rang=TypeRang.ENDROIT,
        mailles=[]
    )

    resultat = rang_vers_texte(rang, 0)

    assert resultat == "Rang 1 (endroit) : "

def test_motif_vers_texte_simple():
    rang1 = Rang(
        type_rang=TypeRang.ENDROIT,
        mailles=[
            Maille(TypeMaille.ENDROIT),
            Maille(TypeMaille.ENDROIT),
            Maille(TypeMaille.ENVERS),
        ]
    )

    rang2 = Rang(
        type_rang=TypeRang.ENVERS,
        mailles=[
            Maille(TypeMaille.ENVERS),
            Maille(TypeMaille.ENVERS),
        ]
    )

    motif = Motif(instructions=[])  # pas utilisé ici pour le texte
    motif.rangs = [rang1, rang2]

    resultat = motif_vers_texte(motif)

    assert "Rang 1 (endroit)" in resultat
    assert "K2" in resultat
    assert "P2" in resultat