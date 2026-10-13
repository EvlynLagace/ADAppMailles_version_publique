import json
import math

from .tuile import Tuile

class Couverture:
    """
    Représente une couverture composée de tuiles carrées.

    Permet de générer la grille de tuiles et de calculer
    les mailles et les rangs pour chaque tuile.
    """

    def __init__(self, largeur_cm=100, hauteur_cm=60, tuiles = None, nom_couverture = "Ma couverture"):
        """
        Initialise une couverture à partir d'une largeur et d'une hauteur fournies pour l'utilisateur

        Args:
            largeur_cm : largeur de la couverture en cm
            hauteur_cm : hauteur de la couverture en cm
            tuiles : liste de Tuile de la couverture
        """

        if not isinstance(largeur_cm, int) or not isinstance(hauteur_cm, int):
            raise TypeError("Les dimensions doivent être des entiers")
        if largeur_cm <= 0 or hauteur_cm <= 0:
            raise ValueError("Les dimensions doivent être strictement positives")
        
        self.largeur_cm = largeur_cm
        self.hauteur_cm = hauteur_cm
        self.tuiles = tuiles if tuiles is not None else []
        self.nom_couverture = nom_couverture

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

    def tuiles_to_dict(self):
        return [
            [
                {
                    "motif":tuile.motif.nom_motif if tuile.motif else None,
                    "nb_mailles": tuile.nb_mailles,
                    "nb_rangs":tuile.nb_rangs,
                }
                for tuile in ligne
            ]
            for ligne in self.tuiles
        ]
        
    def to_dict(self):
        return {
            "largeur_cm": self.largeur_cm,
            "hauteur_cm": self.hauteur_cm,
            "tuiles": self.tuiles_to_dict(),
            "nom_couverture": self.nom_couverture
        }

    def to_json(self):
        couverture = self.to_dict()
        return json.dumps(couverture, indent=4, ensure_ascii=False)
   
    @classmethod
    def from_dict(cls, data, catalogue):
        couverture = cls(
            largeur_cm=data["largeur_cm"],
            hauteur_cm=data["hauteur_cm"],
            nom_couverture=data.get("nom_couverture", "Ma couverture"),
        )

        couverture.generer_tuiles()

        for i, ligne in enumerate(data["tuiles"]):
            for j, tuile_data in enumerate(ligne):

                tuile=couverture.tuiles[i][j]

                tuile.nb_mailles = tuile_data.get("nb_mailles")
                tuile.nb_rangs = tuile_data.get("nb_rangs")

                nom_motif = tuile_data["motif"]

                if not nom_motif:
                    raise ValueError("Une tuile de la couverture n'a pas de motif spécifié.")
                
                   
                tuile.motif = next(
                    (
                        motif
                        for motif in catalogue
                        if motif.nom_motif == nom_motif
                    ),
                    None
                )

                if tuile.motif is None:
                    raise ValueError(f"Motif '{nom_motif}' non trouvé dans le catalogue.")
                    
                tuile.nb_mailles_effectif = tuile.calculer_nb_mailles_effectif(tuile.motif)
                tuile.nb_rangs_effectif = tuile.calculer_nb_rangs_effectif(tuile.motif)
                tuile.calculer_structure_motif()
                tuile.initialiser_liste_motifs_compatibles(catalogue)

        return couverture