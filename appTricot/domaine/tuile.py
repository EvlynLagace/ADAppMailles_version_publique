import math
class Tuile:
    """
    Représente une tuile de la couverture

    Calcule le nombre de mailles et le nombre de rangs de la tuile,
    Permet de sélectionner un motif compatible et de calculer sa structure, soit
    le nombre de répétition du motif et les mailles à ajuster.
    """
    def __init__(self, largeur_cm=100, hauteur_cm=100):
        """
        Initialise une tuile

        Args:
            largeur_cm: largeur de la tuile en cm.
            hauteur_cm: hauteur de la tuile en cm.
        """
        self.largeur_cm = largeur_cm
        self.hauteur_cm = hauteur_cm
        self.nb_mailles = None
        self.nb_rangs = None
        self.motif = None
        self.motifs_compatibles = []
        self.nb_mailles_effectif = None
        self.nb_rangs_effectif = None
        self.nb_mailles_final = None
        self.motif_structure = None
        self.rangs = []

    def initialiser_dimensions(self, echantillon):
        """
        Calcule et initialise les dimensions de la tuile
        en nombre de mailles et de rangs, à partir d'un échantillon

        Args:
            echantillon: l'échantillon utilisé pour la conversion.

        Modifie:
            modifie nb_mailles et nb_rangs de l'instance
        """
        self.nb_mailles = echantillon.calculer_mailles_pour_largeur(self.largeur_cm)
        self.nb_rangs = echantillon.calculer_rangs_pour_hauteur(self.hauteur_cm)

    def initialiser_liste_motifs_compatibles(self, catalogue):
        liste_compatibles = []
        for motif in catalogue:
            if self.motif_est_compatible(motif):
                liste_compatibles.append(motif)

        self.motifs_compatibles = liste_compatibles

        return liste_compatibles

    def calculer_nb_mailles_effectif (self, motif):
        return math.ceil(self.nb_mailles / motif.coefficient_horizontal)
    
    def calculer_nb_rangs_effectif (self, motif):
        return math.ceil(self.nb_rangs / motif.coefficient_vertical)
    
    def motif_est_compatible(self, motif, tolerance=4):
        """
        Determine si une tuile a un nombre de mailles suffisant
        pour un motif : nb_mailles = avant + k (repetees) + apres
        avec une tolerance qui permet l'ajout de mailles au motif

        Args:
            motif: le motif utilisé
            tolerance: le nombre de mailles ajoutées à la tuile toléré

        Returns:
            True si le motif est commpatible.
        """

        repetees = motif.nb_mailles_repetees
        ajoutees = motif.nb_mailles_ajoutees
        effectives = self.calculer_nb_mailles_effectif(motif)

        # 1. trop petit (on peut ajouter, mais pas enlever)
        if effectives + tolerance < motif.nb_mailles_minimum:
            return False
     
        base = effectives - ajoutees
        reste = base % repetees

        return min(reste, repetees - reste ) <= tolerance
    
    def calculer_structure_motif(self):
        
        repetees_motif = self.motif.nb_mailles_repetees
        ajoutees_motif = self.motif.nb_mailles_ajoutees

        nb_repetitions = (self.nb_mailles_effectif - ajoutees_motif) // repetees_motif

        if nb_repetitions <= 0:
            nb_repetitions = 1
            reste = 0

            nb_ajoutees_tuile = max(0, self.motif.nb_mailles_minimum - self.nb_mailles_effectif)
            self.nb_mailles_final = self.nb_mailles_effectif + nb_ajoutees_tuile

        else:
            nb_ajoutees_tuile = 0
            reste = self.nb_mailles_effectif - ajoutees_motif - (nb_repetitions * repetees_motif)
            reste += reste % 2
            self.nb_mailles_final = (nb_repetitions * repetees_motif) + ajoutees_motif + reste + nb_ajoutees_tuile

        self.motif_structure = {
            "nb_repetitions": nb_repetitions,
            "nb_ajoutees": nb_ajoutees_tuile,
            "reste": reste,
            "max_mailles": self.nb_mailles_final
        }

        return self.motif_structure