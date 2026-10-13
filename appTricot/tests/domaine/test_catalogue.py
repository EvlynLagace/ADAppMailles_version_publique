import json
import tempfile

from django.test import TestCase

from appTricot.domaine.catalogue import Catalogue
from appTricot.domaine.motif import Motif




class CatalogueTests(TestCase):
    def test_initialisation_par_defaut(self):
        catalogue = Catalogue()

        self.assertEqual(catalogue.motifs, [])

    def test_initialisation_avec_motifs(self):
        m1 = Motif("Motif 1")
        m2 = Motif("Motif 2")

        catalogue = Catalogue([m1, m2])

        self.assertIn(m1, catalogue.motifs)
        self.assertIn(m2, catalogue.motifs)
        self.assertEqual(len(catalogue.motifs), 2)

    def test_from_json_file_charge_les_motifs(self):
        contenu = {
            "motifs": [
                {
                    "nom_motif": "Motif JSON",
                    "coefficient_horizontal": 1,
                    "coefficient_vertical":1,
                    "couleur_motif": "#000000",
                    "instructions": [
                        {
                            "type_rang": "ENDROIT",
                            "avant": [],
                            "repetees": [{"type": "K", "n": 1}],
                            "apres": [],
                        }
                    ],
                }
            ]
        }

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as tmp:
            json.dump(contenu, tmp, ensure_ascii=False)
            tmp_path = tmp.name

        try:
            catalogue = Catalogue.from_json_file(tmp_path)

            self.assertEqual(len(catalogue.motifs), 1)
            self.assertEqual(catalogue.motifs[0].nom_motif, "Motif JSON")
            self.assertEqual(catalogue.motifs[0].coefficient_horizontal, 1)
            self.assertEqual(catalogue.motifs[0].couleur_motif, "#000000")
        finally:
            import os

            os.remove(tmp_path)