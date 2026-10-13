import math

from adappmailles.modele.tuile import Tuile

class Couverture:
    """
    Représente une couverture composée de tuiles carrées.

    Permet de générer la grille de tuiles et de calculer
    les mailles et les rangs pour chaque tuile.
    """

    def __init__(self, largeur_cm, hauteur_cm, tuiles = None):

        if not isinstance(largeur_cm, int) or not isinstance(hauteur_cm, int):
            raise ValueError("Les dimensions doivent être des entiers")
        if largeur_cm <= 0 or hauteur_cm <= 0:
            raise ValueError("Les dimensions doivent être strictement positives")
        
        self.largeur_cm = largeur_cm
        self.hauteur_cm = hauteur_cm
        self.tuiles = tuiles if tuiles is not None else []

    @property
    def cote_tuile(self) -> int:
        #la mesure maximale du côté d'un carré que l'on peut répéter pour couvrir
        #toute la surface de la couverture est le plus grand commun diviseur
        #de sa largeur et de sa hauteur.
        """Retourne la longueur du côté d'une tuile carrée maximale pour couvrir la surface"""
        return math.gcd(self.largeur_cm, self.hauteur_cm)
         
    @property
    def nb_tuiles_largeur(self) -> int:
        #division entière puisque la mesure d'un coté d'une tuile est un multiple 
        # de la largeur de la couverture
        """Retourne le nombre de tuiles carrées nécessaires pour couvrir la largeur de la couverture"""
        return (self.largeur_cm // self.cote_tuile)
        
    @property
    def nb_tuiles_hauteur(self) -> int:
        """Retourne le nombre de tuiles carrées nécessaires pour couvrir la hauteur de la couverture"""
        return (self.hauteur_cm // self.cote_tuile)
    
    def calculer_nb_tuiles(self):
        #pour les tests
        return self.nb_tuiles_hauteur*self.nb_tuiles_largeur
    
    def generer_tuiles(self):
        self.tuiles=[]
        
        for _ in range(self.nb_tuiles_hauteur):
            ligne = []
            for _ in range(self.nb_tuiles_largeur):
                tuile = Tuile(self.cote_tuile, self.cote_tuile)
                ligne.append(tuile)
            self.tuiles.append(ligne)