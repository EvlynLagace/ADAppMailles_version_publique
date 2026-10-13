from adappmailles.modele.maille import Maille, TypeMaille

def test_default_est_endroit():
    m = Maille()
    assert m.est_endroit
    assert not m.est_envers

def test_creation_maille_envers():
    m = Maille(TypeMaille.ENVERS)
    assert m.est_envers
    assert not m.est_endroit

def test_str():
    m = Maille(TypeMaille.ENDROIT)
    assert str(m) == "K"

def test_repr():
    m = Maille(type_maille=TypeMaille.ENVERS)
    assert repr(m) == "Maille(ENVERS)"

def test_type_maille():
    m = Maille(TypeMaille.ENVERS)
    assert m.type_maille == TypeMaille.ENVERS

def test_coherence_proprietes():
    m = Maille(TypeMaille.ENDROIT)
    assert m.est_endroit
    assert not m.est_envers

    m = Maille(TypeMaille.ENVERS)
    assert m.est_envers
    assert not m.est_endroit