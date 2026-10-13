import math
import random
class Tuile:
    """
    Représente une tuile de la couverture

    Calcule le nombre de mailles et le nombre de rangs de la tuile,
    Permet de sélectionner un motif compatible et de 
    Générer le patron de la tuile.
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
        self.nb_mailles_effectif = None

    def initialiser_dimensions(self, echantillon):
        """
        Calcule et initialise les dimensions de la tuile
        en nombre de mailles et de rangs, à partir d'un échantillon

        Args:
            echantillon: l'échantillon utilisé pour la conversion.

        Returns:
            modifie nb_mailles et nb_rangs
        """
        self.nb_mailles = echantillon.calculer_mailles_pour_largeur(self.largeur_cm)
        self.nb_rangs = echantillon.calculer_rangs_pour_hauteur(self.hauteur_cm)

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
        total = math.ceil(self.nb_mailles/motif.coefficient)

        # 1. trop petit (on peut ajouter, mais pas enlever)
        if total + tolerance < motif.nb_mailles_minimum:
            return False

        # 2. pas de mailles répétées dans le motif
        if repetees == 0:            
            return ajoutees <= total <= ajoutees + tolerance
        
        # si des mailles sont répétées dans le motif
        base = total - ajoutees
        reste = base % repetees

        return min(reste, repetees - reste ) <= tolerance

    def lister_motifs_compatibles(self, catalogue):
        """
        Retourne une liste des motifs compatibles avec la tuile
        
        Args :
            catalogue (Catalogue) : catalogue des motifs possibles

        Returns :
            List[Motif] : la liste des motifs qui sont compatibles
        """
        motifs_compatibles = []

        for motif in catalogue.motifs:
            if self.motif_est_compatible(motif):
                motifs_compatibles.append(motif)

        return motifs_compatibles
    
    def selectionner_motif(self, motifs_compatibles, voisins=None):
        """
        Sélectionne un motif compatible pour la tuile
        en appliquant la contrainte que deux tuiles voisines
        ne peuvent pas avoir le même motif

        Args :
            motifs_compatibles (List)
            voisins (List) : liste des voisins de la tuile

        Returns :
            modifie self.motif
        """
        if voisins is None:
            voisins=[]

        if not motifs_compatibles:
            raise ValueError("Aucun motif compatible")
        
        motifs_filtres = [m for m in motifs_compatibles if m not in [v.motif for v in voisins if v.motif]]

        if motifs_filtres:
            self.motif = random.choice(motifs_filtres)
            self.nb_mailles_effectif = math.ceil(self.nb_mailles/ self.motif.coefficient)
        else :
            print("fallback (conflit voisins)")
            self.motif = random.choice(motifs_compatibles)
            self.nb_mailles_effectif = math.ceil(self.nb_mailles/ self.motif.coefficient)