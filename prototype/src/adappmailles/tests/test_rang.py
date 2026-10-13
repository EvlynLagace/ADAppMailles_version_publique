from adappmailles.modele.maille import Maille, TypeMaille
from adappmailles.modele.rang import Rang, TypeRang

def test_default_est_endroit():
    r = Rang()
    assert r.est_endroit
    assert not r.est_envers
    assert list(r) == []

def test_creation_rang_envers():
    r = Rang(TypeRang.ENVERS)
    assert r.est_envers
    assert not r.est_endroit
    assert list(r)==[]

def test_str():
    r = Rang(TypeRang.ENVERS)
    assert str(r) == "envers"

def test_rang_iter():
    r = Rang(mailles=[
        Maille(TypeMaille.ENDROIT),
        Maille(TypeMaille.ENVERS),
        Maille(TypeMaille.ENDROIT)
    ])
    assert list(r)==[
        Maille(TypeMaille.ENDROIT),
        Maille(TypeMaille.ENVERS),
        Maille(TypeMaille.ENDROIT)
    ]

def test_rang_independance_liste():
    base = [1, 2]
    r = Rang(mailles=base)
    base.append(3)

    assert len(list(r)) == 2

def test_coherence_types():
    r1 = Rang(TypeRang.ENDROIT)
    assert r1.est_endroit
    assert not r1.est_envers

    r2 = Rang(TypeRang.ENVERS)
    assert r2.est_envers
    assert not r2.est_endroit