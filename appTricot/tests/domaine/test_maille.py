from django.test import SimpleTestCase, TestCase

from appTricot.domaine.maille import Maille, TypeMaille

class TypeMailleTests(SimpleTestCase):
   def test_valeurs_enum(self):
      self.assertEqual(TypeMaille.ENDROIT.value, "K")
      self.assertEqual(TypeMaille.ENVERS.value, "P")

class MailleTests(TestCase):

   def test_par_defaut_est_endroit(self):
      maille = Maille()
      self.assertEqual(maille.type_maille, TypeMaille.ENDROIT)

   def test_initialisation_explicite_envers(self):
      maille = Maille(TypeMaille.ENVERS)
      self.assertEqual(maille.type_maille, TypeMaille.ENVERS)