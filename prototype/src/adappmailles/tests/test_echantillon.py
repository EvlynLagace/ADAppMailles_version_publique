import pytest

from adappmailles.modele.echantillon import Echantillon

def test_nb_mailles_et_rangs_entiers():
    with pytest.raises(TypeError):
        Echantillon(nb_mailles=10.5)  # float → erreur
    
    with pytest.raises(TypeError):
        Echantillon(nb_rangs=12.0)    # float → erreur

    # Cas valide
    echantillon = Echantillon(nb_mailles=10, nb_rangs=12)
    assert echantillon.nb_mailles == 10
    assert echantillon.nb_rangs == 12

def test_nombre_de_mailles_par_cm_echantillon_par_defaut(echantillon_defaut: Echantillon):
    assert echantillon_defaut.mailles_par_cm == 1

def test_nombre_de_mailles_par_cm_decimal():
    echantillon = Echantillon(largeur_cm=10, nb_mailles=15)
    assert echantillon.mailles_par_cm == pytest.approx(1.5)    

def test_retourne_nombre_mailles_par_cm_autres_valeurs():
    echantillon = Echantillon (largeur_cm = 10, hauteur_cm = 10, nb_mailles = 100, nb_rangs = 100)

    resultat = echantillon.mailles_par_cm

    assert resultat == 10

def test_retourne_nombre_mailles_par_cm_valeurs_non_entieres():
    echantillon = Echantillon(
        largeur_cm=15,
        hauteur_cm=10,
        nb_mailles=100,
        nb_rangs=100
    )

    resultat = echantillon.mailles_par_cm

    assert resultat == pytest.approx(100/15)

def test_calculer_mailles_pour_largeur_valeurs_non_entieres():
    # Arrange : échantillon avec 100 mailles pour 15 cm → 100/15 ≈ 6,666 mailles/cm
    echantillon = Echantillon(largeur_cm=15, nb_mailles=100)
    
    # Act : tuile de 20 cm
    resultat = echantillon.calculer_mailles_pour_largeur(20)
    
    # Calcul attendu : 20 * 6,666… ≈ 133,333 → math.ceil → 134
    assert resultat == 134

def test_calculer_mailles_largeur_zero():
    echantillon = Echantillon()
    assert echantillon.calculer_mailles_pour_largeur(0) == 0

def test_calculer_rangs_pour_hauteur_autres_valeurs():
    echantillon = Echantillon(hauteur_cm=10, nb_rangs=15)
    
    resultat = echantillon.calculer_rangs_pour_hauteur(20)
    
    assert resultat == 30

def test_calculer_rangs_pour_hauteur_valeurs_non_entieres():
    # Arrange : échantillon avec 100 rangs pour 15 cm → 100/15 ≈ 6,666 rangs/cm
    echantillon = Echantillon(hauteur_cm=15, nb_rangs=100)
    
    # Act : tuile de 20 cm
    resultat = echantillon.calculer_rangs_pour_hauteur(20)
    
    # Calcul attendu : 20 * 6,666… ≈ 133,333 → math.ceil → 134
    assert resultat == 134

def test_valeurs_negatives():
    with pytest.raises(ValueError):
        Echantillon(largeur_cm=-1)

    with pytest.raises(ValueError):
        Echantillon(hauteur_cm=0)

def test_coherence_mailles():
    e = Echantillon(largeur_cm=10, nb_mailles=10)

    assert e.calculer_mailles_pour_largeur(10) == 10