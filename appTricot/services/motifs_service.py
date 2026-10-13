import json
from pathlib import Path
from django.utils.text import slugify

from appTricot.domaine.rang_instructions import RangInstructions
from appTricot.services.affichage_service import afficher_grille, construire_legende, generer_instructions_textuelles

from ..domaine.motif import Motif

def charger_motifs():
    dossier = Path(__file__).resolve().parent.parent / "data" / "motifs"

    motifs = []

    for fichier in sorted(dossier.glob("*.json")):

        with open(fichier, encoding="utf-8") as f:
            data = json.load(f)

        motifs.append(Motif.from_json(data))

    return motifs

def chemin_image_motif(motif):
    
    nom = slugify(motif.nom_motif).replace("-","_")
    chemin_url = f"appTricot/images/echantillons/{nom}.jpg"

    fichier = (
        Path(__file__).resolve().parent.parent
        / "static"
        / chemin_url
    )

    if fichier.exists():
        return chemin_url
    
    return "appTricot/images/echantillons/photo-a-venir.jpg"

def motif_to_rangs(motif, nb_repetitions:int=1, nb_mailles_tuile:int=0):
    rangs = []

    for instruction in motif.instructions:
        
        mailles = rang_instructions_to_mailles(instruction, nb_repetitions, nb_mailles_tuile)
        type_rang = instruction.type_rang.name


        rangs.append({
            "mailles": mailles,
            "type_rang":type_rang    
        })

    return rangs

def rang_instructions_to_mailles(rang:RangInstructions, nb_repetitions:int, nb_mailles_tuile:int, reste:int=0):

    mailles = []

    #Répartition du reste au début
    if reste>0:
        mailles.extend(["K"] * (reste//2))

    if rang.est_pattern_simple:
        while len(mailles)<nb_mailles_tuile - (reste//2):
            for maille, n in rang.repetees:
                mailles.extend([maille.value]*n)

    else:
    
        #Construction du bloc avant
        for maille, n in rang.avant:
            mailles.extend([maille.value] * n)

        #Construction du bloc répété
        for _ in range(nb_repetitions):
            for maille, n in rang.repetees:
                mailles.extend([maille.value]*n)

        #Construction du bloc après
        for maille, n in rang.apres:
            mailles.extend([maille.value] * n)

    #Répartition du reste à la fin
    if reste >0:
        mailles.extend(["K"] * (reste//2))

    return mailles

def preparer_motif_pour_affichage(motif):
    instructions = afficher_motif_texte(motif)

    rangs = motif_to_rangs(
        motif,
        1,
        motif.nb_mailles_minimum
    )

    grille = afficher_grille(rangs)

    types_maille = motif.types_mailles_utilises()

    legende = construire_legende(motif)

    photo = chemin_image_motif(motif)

    return {
        "motif": motif,
        "instructions": instructions,
        "rangs": rangs,
        "grille": grille,
        "legende": legende,
        "photo":photo,
        "types_maille":types_maille
    }

def afficher_motif_texte (motif):

    lignes = []

    for r, m in enumerate(motif.instructions):

        avant = m.avant
        milieu = m.repetees
        apres = m.apres

        avant_txt = ""
        if avant:
            avant_txt = generer_instructions_textuelles(avant)

        milieu_txt = generer_instructions_textuelles(milieu)

        apres_txt = ""
        if apres:
            apres_txt = generer_instructions_textuelles(apres)

        ligne = (f"Rang {r + 1} ({m.type_rang.value}) : {avant_txt} * {milieu_txt} * {apres_txt}")
        lignes.append(ligne)
    
    return lignes

def get_motif(nom_motif):
    return next(
        (
            m
            for m in charger_motifs()
            if m.nom_motif == nom_motif
        ),
        None
    )

def preparer_contexte_motif_print(motif):
    data = preparer_motif_pour_affichage(motif)

    return{
        "motif": motif,
        "instructions_formatees": data["instructions"],
        "grille_motif": data["grille"],
        "legende": data["legende"],
        "types_maille": data["types_maille"]
    }