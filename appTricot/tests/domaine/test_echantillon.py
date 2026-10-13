from django.test import SimpleTestCase

from appTricot.domaine.echantillon import Echantillon


class EchantillonTests(SimpleTestCase):
    def test_par_defaut(self):
        echantillon = Echantillon()
        self.assertEqual(echantillon.largeur_cm, 10)
        self.assertEqual(echantillon.hauteur_cm, 10)
        self.assertEqual(echantillon.nb_mailles, 20)
        self.assertEqual(echantillon.nb_rangs, 27)

    def test_initialisation_autres_valeurs(self):
        echantillon = Echantillon(
            largeur_cm=10,
            hauteur_cm=20,
            nb_mailles=15,
            nb_rangs=30
        )
        self.assertEqual(echantillon.largeur_cm, 10)
        self.assertEqual(echantillon.hauteur_cm, 20)
        self.assertEqual(echantillon.nb_mailles, 15)
        self.assertEqual(echantillon.nb_rangs, 30)

    def test_nb_mailles_type_invalide(self):
        with self.assertRaises(TypeError):
            Echantillon(nb_mailles="10")

    def test_nb_rangs_type_invalide(self):
        with self.assertRaises(TypeError):
            Echantillon(nb_rangs=2.5)

    def test_largeur_cm_invalide(self):
        with self.assertRaises(ValueError):
            Echantillon(largeur_cm=0)

    def test_hauteur_cm_invalide(self):
        with self.assertRaises(ValueError):
            Echantillon(hauteur_cm=-5)

    def test_nb_mailles_invalide(self):
        with self.assertRaises(ValueError):
            Echantillon(nb_mailles=0)

    def test_nb_rangs_invalide(self):
        with self.assertRaises (ValueError):
            Echantillon(nb_rangs=-5)