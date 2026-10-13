import json
import math

class Echantillon:
    """
    Représente un échantillon.

    Permet de convertir les dimensions (cm) en nombre de mailles et de rangs
    d'une tuile en fonction de cet échantillon.
    """
    def __init__(self, largeur_cm=10, hauteur_cm=10, nb_mailles=20, nb_rangs=27, nom_echantillon = "Mon échantillon"):
        """
        Initialise un échantillon.

        Args:
            largeur_cm: largeur de l'échantillon en cm (défaut 10).
            hauteur_cm: hauteur de l'échantillon en cm (défaut 10).
            nb_mailles: nombre de mailles dans l'échantillon (défaut 20).
            nb_rangs: nombre de rangs dans l'échantillon (défaut 27).
        """

        if type(nb_mailles) is not int:
            raise TypeError("Le nombre de mailles doit être un entier")
        if type(nb_rangs) is not int:
            raise TypeError("Le nombre de rangs doit être un entier")        
        if largeur_cm <= 0:
            raise ValueError("La largeur doit être strictement positive")
        if hauteur_cm <= 0:
            raise ValueError("La hauteur doit être strictement positive")
        if nb_mailles <= 0:
            raise ValueError("le nombre de mailles doit être strictement positif")
        if nb_rangs <= 0:
            raise ValueError("Le nombre de rangs doit être strictement positif")
        
        self.largeur_cm = largeur_cm
        self.hauteur_cm = hauteur_cm
        self.nb_mailles = nb_mailles
        self.nb_rangs = nb_rangs
        self.nom_echantillon = nom_echantillon

    @property
    def mailles_par_cm(self) -> float:
        """Nombre de mailles par centimètre (largeur)."""              
        return (self.nb_mailles/self.largeur_cm)
    
    @property
    def rangs_par_cm(self) -> float:
        """Nombre de rangs par centimètre (hauteur)."""
        return (self.nb_rangs/self.hauteur_cm)
    
    def calculer_mailles_pour_largeur(self, largeur_cm_tuile)-> int:
        """
        Calcule le nombre de mailles nécessaires pour une largeur donnée.
        
        Args:
            largeur_cm_tuile: largeur de la tuile en cm.

        Returns:
            int: nombre de mailles de la tuile (arrondi supérieur).
        """
        return math.ceil(largeur_cm_tuile * self.mailles_par_cm)
    
    def calculer_rangs_pour_hauteur(self, hauteur_cm_tuile) -> int:
        """
        Calcule le nombre de rangs nécessaires pour une hauteur donnée.

        Args:
            hauteur_cm_tuile: hauteur de la tuile en cm

        Returns:
            int: nombre de rangs de la tuile (arrondi suprieur).
        """
        return math.ceil(hauteur_cm_tuile * self.rangs_par_cm)

    def to_dict(self):
        return {
            "largeur_cm": self.largeur_cm,
            "hauteur_cm": self.hauteur_cm,
            "nb_mailles": self.nb_mailles,
            "nb_rangs": self.nb_rangs,
            "nom_echantillon": self.nom_echantillon
        }

    def to_json(self):
        echantillon = self.to_dict()
        return json.dumps(echantillon, indent=4, ensure_ascii=False)

    @classmethod
    def from_dict(cls, data):
        echantillon = cls(
            largeur_cm=data["largeur_cm"],
            hauteur_cm=data["hauteur_cm"],
            nb_mailles=data["nb_mailles"],
            nb_rangs=data["nb_rangs"],
            nom_echantillon=data.get("nom_echantillon", "Mon échantillon")
        )

        return echantillon