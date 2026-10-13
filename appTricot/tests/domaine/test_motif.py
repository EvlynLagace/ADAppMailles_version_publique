from django.test import SimpleTestCase

from appTricot.domaine.motif import Motif
from appTricot.domaine.rang_instructions import RangInstructions


class MotifTests(SimpleTestCase):
    def test_par_defaut(self):
        motif = Motif()
        self.assertEqual(motif.nom_motif, None)
        self.assertEqual(motif.instructions, [])
        self.assertEqual(motif.coefficient_horizontal, 1)
        self.assertEqual(motif.couleur_motif, None)

    def test_initialisation_avec_valeurs(self):
        instructions=[RangInstructions(repetees=["endroit"])]

        motif = Motif(
            nom_motif="Nom",
            instructions=instructions,
            coefficient_horizontal=2,
            coefficient_vertical=1,
            couleur_motif="#FF0000"
        )

        self.assertEqual(motif.nom_motif, "Nom")
        self.assertEqual(motif.instructions, instructions)
        self.assertEqual(motif.coefficient_horizontal, 2)
        self.assertEqual(motif.couleur_motif, "#FF0000")