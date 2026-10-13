import math

from adappmailles.modele.rang import Rang
from adappmailles.services.conversion_motif import pattern_to_mailles
class GenerateurTuile:

    def generer(self, couverture, echantillon, catalogue):

       # Génération des tuiles
        for i, ligne in enumerate(couverture.tuiles):
            for j, tuile in enumerate(ligne):

                tuile.initialiser_dimensions(echantillon)

                # choix du motif
                if tuile.motif is None:
                    motifs = tuile.lister_motifs_compatibles(catalogue)

                    if not motifs:
                        raise ValueError("Aucun motif compatible")
                    
                    voisins = obtenir_voisins(couverture, i, j)
                    tuile.selectionner_motif(motifs, voisins)

                self.calculer_structure_motif(tuile)

                self.construire_rangs(tuile)

        return couverture

    # -------------------------

    def calculer_structure_motif(self, tuile, tolerance=4):
        motif = tuile.motif

        if motif is None :
            raise ValueError("Aucun motif pour cette tuile")
        
        if tuile.nb_mailles is None:
            raise ValueError("Tuile non initialisée")
        
        total = tuile.nb_mailles_effectif
        
        instruction_ref = next(
            p for p in motif.instructions if p.repetees
        )
        repetees = instruction_ref.nb_mailles_repetees
        ajoutees = instruction_ref.nb_mailles_ajoutees

        # Mailles disponibles pour les répétitions
        zone_repetition = total - ajoutees

        # Si pas de répétitions
        if repetees == 0 :
            tuile.motif_structure = {
                "nb_repetitions" : 0,
                "reste" : 0,
                "repetees" : 0,
                "ajoutees" : ajoutees
            }
            return
        
        # Calcul du nombre de repetitions
        nb_repetitions = zone_repetition // repetees

        #Calcul du reste sans compter les mailles ajoutees
        reste = zone_repetition % repetees

        if min(reste, repetees - reste) > tolerance:
            # motif pas exploitable proprement
            raise ValueError("Motif incompatible (reste trop grand)")

        #stockage du resultat dans la tuile
        tuile.motif_structure = {
            "nb_repetitions" : nb_repetitions,
            "reste" : reste,
            "repetees" : repetees,
            "ajoutees" : ajoutees
        }

    def construire_rangs(self, tuile):
        motif = tuile.motif
        structure = tuile.motif_structure

        if motif is None or structure is None:
            raise ValueError ("Motif ou structure non initialisée")
            
        nb_repetitions = structure["nb_repetitions"]
        reste = structure["reste"]

        tuile.rangs = []

        for index_rang in range(tuile.nb_rangs):
            rang = self._construire_rang(
                motif,
                nb_repetitions,
                reste,
                index_rang,
                tuile
            )

            tuile.rangs.append(rang)

    def _construire_rang(self, motif, nb_repetitions, reste, index_rang, tuile):
        pattern = motif.instructions[index_rang % len(motif.instructions)]

        mailles = pattern_to_mailles(
            pattern,
            nb_repetitions=nb_repetitions,
            reste=reste,
            taille_cible=tuile.nb_mailles_effectif
        )

        return Rang(type_rang=pattern.type_rang, mailles=mailles)

def obtenir_voisins(couverture, i, j):
    voisins = []

    if i > 0:
        voisins.append(couverture.tuiles[i-1][j])  # haut

    if j > 0:
        voisins.append(couverture.tuiles[i][j-1])  # gauche

    return voisins   