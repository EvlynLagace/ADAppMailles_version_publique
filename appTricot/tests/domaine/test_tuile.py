from unittest.mock import Mock

from django.test import SimpleTestCase

from appTricot.domaine.tuile import Tuile


class TuileTests(SimpleTestCase):
    def test_par_defaut(self):
        tuile = Tuile()
        self.assertEqual(tuile.largeur_cm, 100)
        self.assertEqual(tuile.hauteur_cm, 100)
        self.assertEqual(tuile.nb_mailles, None)
        self.assertEqual(tuile.nb_rangs, None)
        self.assertEqual(tuile.motif, None)
        self.assertEqual(tuile.nb_mailles_effectif, None)
        self.assertEqual(tuile.motif_structure, None)
        self.assertEqual(tuile.rangs, [])

    def test_initialiser_avec_dimensions(self):
        t = Tuile(largeur_cm=120, hauteur_cm=240)
        self.assertEqual(t.largeur_cm, 120)
        self.assertEqual(t.hauteur_cm, 240)

    def test_motif_incompatible_tuile_trop_petite(self):
        t = Tuile(largeur_cm=10, hauteur_cm=10)
        motif = Mock()

        motif.nb_mailles_repetees = 2
        motif.nb_mailles_ajoutees = 48
        motif.nb_mailles_minimum = 50

        t.calculer_nb_mailles_effectif = lambda m:10

        self.assertFalse(t.motif_est_compatible(motif))

    def test_motif_compatible_repetitions(self):
        t = Tuile()
        motif = Mock()

        motif.nb_mailles_repetees = 3
        motif.nb_mailles_ajoutees = 0
        motif.nb_mailles_minimum = 9

        t.calculer_nb_mailles_effectif = lambda m:18

        self.assertTrue(t.motif_est_compatible(motif))

    def test_motif_compatible_grace_a_tolerance(self):
        t = Tuile()
        motif = Mock()
        motif.nb_mailles_repetees = 4
        motif.nb_mailles_ajoutees = 0
        motif.nb_mailles_minimum = 0

        t.calculer_nb_mailles_effectif = lambda m:9

        self.assertTrue(t.motif_est_compatible(motif))

    def test_calcul_structure_motif_cas_normal(self):
        t = Tuile()

        motif = Mock()
        motif.nb_mailles_repetees = 3
        motif.nb_mailles_ajoutees = 1
        motif.nb_mailles_minimum = 0

        t.motif = motif
        t.nb_mailles_effectif = 10

        result = t.calculer_structure_motif()

        self.assertEqual(result["nb_repetitions"], 3)
        self.assertEqual(result["nb_ajoutees"], 0)
        self.assertIn("reste", result)

    def test_calcul_structure_motif_trop_petit(self):
        t = Tuile()

        motif = Mock()
        motif.nb_mailles_repetees = 5
        motif.nb_mailles_ajoutees = 10
        motif.nb_mailles_minimum = 20

        t.motif = motif
        t.nb_mailles_effectif = 5

        result = t.calculer_structure_motif()

        self.assertEqual(result["nb_repetitions"], 1)
        self.assertEqual(result["nb_ajoutees"], 15)
        self.assertEqual(result["reste"], 0)
        self.assertEqual(result["max_mailles"], 20)

    def test_calcul_structure_motif_contient_cles(self):
        t = Tuile()

        motif = Mock()
        motif.nb_mailles_repetees = 2
        motif.nb_mailles_ajoutees = 1
        motif.nb_mailles_minimum = 0

        t.motif = motif
        t.nb_mailles_effectif = 8

        result = t.calculer_structure_motif()

        self.assertIn("nb_repetitions", result)
        self.assertIn("nb_ajoutees", result)
        self.assertIn("reste", result)
        self.assertIn("max_mailles", result)