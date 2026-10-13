from adappmailles.modele.couverture import Couverture
from adappmailles.modele.tuile import Tuile
from adappmailles.ui.console import Console

def test_retourne_dimensions_tuiles_couverture_carree():
    couverture = Couverture (100,100)

    assert couverture.cote_tuile == 100

def test_retourne_dimensions_tuiles_couverture_rectangulaire():
    couverture = Couverture(100, 50)

    assert couverture.cote_tuile == 50

def test_retourne_dimensions_tuiles_nombres_premiers():
    couverture = Couverture(13, 17)

    assert couverture.cote_tuile == 1

def test_retourne_dimensions_tuiles_facteur_commun():
    couverture = Couverture (100, 60)

    assert couverture.cote_tuile == 20

def test_retourne_nb_tuiles_couverture_carree():
    couverture = Couverture(100,100)

    resultat = couverture.calculer_nb_tuiles()

    assert resultat == 1

def test_retourne_nb_tuiles_couverture_rectangulaire():
    couverture = Couverture(100,50)

    resultat = couverture.calculer_nb_tuiles()

    assert resultat == 2

def test_retourne_nb_tuiles_couverture_nb_premiers():
    couverture = Couverture(17,13)

    resultat = couverture.calculer_nb_tuiles()

    assert resultat == (221)

def test_retourne_nb_tuiles_couverture_facteur_commun():
    couverture = Couverture(100,60)

    resultat = couverture.calculer_nb_tuiles()

    assert resultat == (15)

def test_lire_dimensions_couverture():
    # Fonction simulée qui renvoie 100 puis 60
    def fake_input(prompt):
        return {"Entrez la largeur de la couverture en cm : ": "100",
                "Entrez la hauteur de la couverture en cm : ": "60"}[prompt]

    largeur, hauteur = Console.lire_dimensions_couverture(fake_input)
    assert largeur == 100
    assert hauteur == 60

def test_dimensions_grille_apres_generation_des_tuiles():
    couverture = Couverture(100, 200)
    
    couverture.generer_tuiles()

    assert len(couverture.tuiles) == 200 // couverture.cote_tuile
    assert len(couverture.tuiles[0]) == 100 // couverture.cote_tuile

def test_nombre_total_de_tuiles_generees():
    couverture = Couverture(100, 200)
    
    couverture.generer_tuiles()
    total = sum(len(ligne) for ligne in couverture.tuiles)
    assert total == (100//couverture.cote_tuile) * (200//couverture.cote_tuile)

def test_type_tuiles():
    couverture = Couverture(100, 200)
    
    couverture.generer_tuiles()

    for ligne in couverture.tuiles:
        for t in ligne:
            assert isinstance(t, Tuile)

def test_dimensions_des_tuiles_dans_couverture():
    couverture = Couverture(100, 200)
    
    couverture.generer_tuiles()

    for ligne in couverture.tuiles:
        for t in ligne:
            assert t.largeur_cm == couverture.cote_tuile
            assert t.hauteur_cm == couverture.cote_tuile

def test_couverture_reconstruite():
    couverture = Couverture(100, 100)
    
    couverture.generer_tuiles()
    couverture.generer_tuiles()

    assert len(couverture.tuiles) == couverture.nb_tuiles_hauteur
    assert len(couverture.tuiles[0]) == couverture.nb_tuiles_largeur