from adappmailles.modele.catalogue import Catalogue
from adappmailles.modele.couverture import Couverture
from adappmailles.modele.echantillon import Echantillon
from adappmailles.services.generateur_tuile import GenerateurTuile

class ApplicationControleur:
    def __init__(self):
        self.valeurs = {
            "largeur_couverture":100,
            "hauteur_couverture":80,
            "largeur_echantillon":10,
            "hauteur_echantillon":10,
            "nb_mailles_echantillon":10,
            "nb_rangs_echantillon":10
        }

        self.couverture=None
        self.echantillon=None
        self.catalogue=None
        self.generateur = None

    def configurer(self):
        self.couverture = Couverture(
            self.valeurs["largeur_couverture"],
            self.valeurs["hauteur_couverture"]
        )

        self.echantillon = Echantillon(
            self.valeurs["largeur_echantillon"],
            self.valeurs["hauteur_echantillon"],
            self.valeurs["nb_mailles_echantillon"],
            self.valeurs["nb_rangs_echantillon"]
        )

        self.catalogue = Catalogue.from_json_file("src/adappmailles/data/catalogue.json")

        self.generateur = GenerateurTuile()

    def generer(self):
        self.couverture.generer_tuiles()
        
        return self.generateur.generer(
            self.couverture,
            self.echantillon,
            self.catalogue
        )