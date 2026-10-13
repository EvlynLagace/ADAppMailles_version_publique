import random

from appTricot.services.motifs_service import rang_instructions_to_mailles

from ..domaine.rang_instructions import RangInstructions

def selectionner_motif(couverture_obj, echantillon_obj, motifs_obj):

    for i, ligne in enumerate(couverture_obj.tuiles):
        for j, tuile in enumerate(ligne):

            tuile.initialiser_dimensions(echantillon_obj)
            tuile.initialiser_liste_motifs_compatibles(motifs_obj)

            motifs_disponibles = tuile.motifs_compatibles.copy()

            if i > 0:
                motif_gauche = couverture_obj.tuiles[i-1][j].motif
                if motif_gauche in motifs_disponibles:
                    motifs_disponibles.remove(motif_gauche)

            if j > 0:
                motif_haut = couverture_obj.tuiles[i][j-1].motif
                if motif_haut in motifs_disponibles:
                    motifs_disponibles.remove(motif_haut)

            if not motifs_disponibles:
                raise ValueError(
                    f"Impossible de trouver un motif compatible pour la tuile ({i}, {j})"
                )
    
            tuile.motif = random.choice(motifs_disponibles)
            tuile.nb_mailles_effectif = tuile.calculer_nb_mailles_effectif(tuile.motif)
            tuile.nb_rangs_effectif = tuile.calculer_nb_rangs_effectif(tuile.motif)

            tuile.calculer_structure_motif()
    
    return (couverture_obj)



def tuile_to_rangs(motif, nb_rangs_tuile:int=0, nb_repetitions:int=1, nb_mailles_tuile:int=0, reste:int=0):
    rangs = []
    instructions = list(motif.instructions)

    for i in range(nb_rangs_tuile):
        m=instructions[i % len(instructions)]
        
        mailles = rang_instructions_to_mailles(m, nb_repetitions, nb_mailles_tuile, reste)
        type_rang = m.type_rang.name if m.type_rang else "inconnu"


        rangs.append({
            "numero": i + 1,
            "mailles": mailles,
            "type_rang":type_rang    
        })

    return rangs
