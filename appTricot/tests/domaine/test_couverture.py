import json
from pathlib import Path
import tempfile

from django.test import SimpleTestCase

from appTricot.domaine import catalogue, couverture
from appTricot.domaine.tuile import Tuile
from appTricot.services.couverture_service import charger_couverture, sauvegarder_couverture
from appTricot.services.motifs_service import charger_motifs


class CouvertureTests(SimpleTestCase):
    def test_par_defaut(self):
        c = couverture.Couverture()
        self.assertEqual(c.largeur_cm, 100)
        self.assertEqual(c.hauteur_cm, 60)
        self.assertEqual(c.tuiles, [])

    def test_initialisation_avec_dimensions(self):
        t1 = Tuile()
        t2 = Tuile()
        tuiles= [t1, t2]

        c = couverture.Couverture(
            largeur_cm = 200,
            hauteur_cm = 100,
            tuiles = tuiles
        )

        self.assertEqual(c.largeur_cm, 200)
        self.assertEqual(c.hauteur_cm, 100)
        self.assertEqual(c.tuiles, tuiles)

    def test_dimensions_doivent_etre_des_entiers(self):
        with self.assertRaises(TypeError):
            couverture.Couverture(largeur_cm=100.5, hauteur_cm=60)

        with self.assertRaises(TypeError):
            couverture.Couverture(largeur_cm=100, hauteur_cm="60")

    def test_dimensions_doivent_etre_positives(self):
        with self.assertRaises(ValueError):
            couverture.Couverture(largeur_cm=-0, hauteur_cm=60)

        with self.assertRaises(ValueError):
            couverture.Couverture(largeur_cm=100, hauteur_cm=0)

        with self.assertRaises(ValueError):
            couverture.Couverture(largeur_cm=-100, hauteur_cm=-60)

        with self.assertRaises(ValueError):
            couverture.Couverture(largeur_cm=100, hauteur_cm=-60)

    def test_generation_tuile_par_defaut(self):
        c = couverture.Couverture()
        c.generer_tuiles()
        self.assertEqual(len(c.tuiles), 3) #hauteur de 3 tuiles
        self.assertEqual(len(c.tuiles[0]), 5)

    def test_cote_tuile(self):
        c = couverture.Couverture(100, 60)
        self.assertEqual(c.cote_tuile, 20)

    def test_cote_tuile_premiere_entre_elles(self):
        c = couverture.Couverture(7)
        self.assertEqual(c.cote_tuile, 1)

    #largeur de 5 tuiles

    def test_to_json_couverture(self):
        c = couverture.Couverture(100, 60)
        c.generer_tuiles()

        json_resultat = c.to_json()

        data = json.loads(json_resultat)

        assert data["largeur_cm"] == 100
        assert data["hauteur_cm"] == 60
        assert len(data["tuiles"]) == 3

    def test_sauvegarder_couverture(self):
        c = couverture.Couverture(100, 60)
        c.generer_tuiles()

        with tempfile.TemporaryDirectory() as dossier:
            fichier = Path(dossier) / "test_couverture.json"

            sauvegarder_couverture(c, fichier)

            self.assertTrue


    # def test_charger_couverture(self):
    #     c1 = couverture.Couverture(100, 60)
    #     c1.generer_tuiles()

    #     with tempfile.TemporaryDirectory() as dossier:
    #         fichier = Path(dossier) / "test_couverture.json"

    #         sauvegarder_couverture(c1, fichier)

    #         self.assertTrue(fichier.exists())

    #         catalogue = charger_motifs()

    #         c2 = charger_couverture(fichier, catalogue)

    #         assert c2.nb_tuiles_largeur == c1.nb_tuiles_largeur
    #         assert c2.nb_tuiles_hauteur == c1.nb_tuiles_hauteur
    #         assert c2.largeur_cm == c1.largeur_cm
    #         assert c2.hauteur_cm == c1.hauteur_cm
    #         assert c1.to_dict() == c2.to_dict()
