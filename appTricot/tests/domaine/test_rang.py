from django.test import SimpleTestCase, TestCase

from appTricot.domaine.maille import Maille, TypeMaille
from appTricot.domaine.rang import Rang, TypeRang


class TypeRangTests(SimpleTestCase):
    def test_valeurs_enum(self):
        self.assertEqual(TypeRang.ENDROIT.value, "endroit")
        self.assertEqual(TypeRang.ENVERS.value, "envers")

class RangTest(SimpleTestCase):
    def test_par_defaut(self):
        rang = Rang()
        self.assertEqual(rang.type_rang, TypeRang.ENDROIT)
        self.assertEqual(rang.mailles, [])

    def test_initialisation_explicite_envers(self):
        r = Rang(TypeRang.ENVERS)
        self.assertEqual(r.type_rang, TypeRang.ENVERS)

    def test_initialisation_mailles(self):
        m1 = Maille()
        m2 = Maille(TypeMaille.ENVERS)

        mailles = [m1, m2]

        r = Rang(mailles=mailles)

        self.assertEqual(r.mailles, mailles)
        self.assertIsNot(r.mailles, mailles)