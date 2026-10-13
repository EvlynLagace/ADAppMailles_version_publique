from django.test import SimpleTestCase

from appTricot.domaine.maille import Maille, TypeMaille
from appTricot.domaine.rang import TypeRang
from appTricot.domaine.rang_instructions import RangInstructions


class RangInstructionsTest(SimpleTestCase):

    def test_par_defaut(self):
        r = RangInstructions(repetees=["endroit"])
        self.assertEqual(r.type_rang, TypeRang.ENDROIT)
        self.assertEqual(r.avant, [])
        self.assertEqual(r.repetees, ["endroit"])
        self.assertEqual(r.apres, [])

    def test_initialisation_avec_rangs(self):

        #création des mailles
        m1 = Maille()
        m2 = Maille(TypeMaille.ENVERS)
        m3 = Maille()
        m4 = Maille(TypeMaille.ENVERS)
        m5 = Maille()
        m6 = Maille(TypeMaille.ENVERS)

        #création des listes d'instructions
        avant = [(m1, 1), (m2, 2)]
        milieu = [(m3, 1), (m4, 1)]
        apres = [(m5, 3), (m6, 1)]

        r = RangInstructions(
            type_rang = TypeRang.ENDROIT,
            avant=avant,
            repetees=milieu,
            apres=apres
        )
        
        self.assertEqual(r.type_rang, TypeRang.ENDROIT)
        self.assertEqual(r.avant, avant)
        self.assertEqual(r.repetees, milieu)
        self.assertEqual(r.apres, apres)