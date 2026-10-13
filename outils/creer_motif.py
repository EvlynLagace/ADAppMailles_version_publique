import json
import re

from appTricot.domaine.maille import TypeMaille

def parser_sequence(texte):

    types_acceptes = {maille.value for maille in TypeMaille}
    
    sequence_rang = []

    mailles = texte.split()

    for maille in mailles :

        match_nombre = re.match(r"\d+", maille)

        if match_nombre:
            nombre = nombre = int(match_nombre.group())
        else:
            nombre = 1

        type_maille = re.search(r"[A-Z]+", maille).group()

        if type_maille not in types_acceptes:
            raise ValueError(f"Maille inconnue : {type_maille}")

        sequence_rang.append(
            {
                "type":type_maille,
                "n": nombre
            }
        )

    return sequence_rang

def creer_motif():
    nom_motif = input("Nom du motif : ")
    coefficient_horizontal = float(input("Coefficient horizontal : "))
    coefficient_vertical = float(input("Coefficient_vertical : "))
    couleur_motif =input("couleur_motif : ")

    nb_rang = int(input("nombre de rangs du motif : "))

    instructions = []

    for rang in range(nb_rang):
        sens_rang = input(f"sens du rang {rang +1}: ").upper()
        texte_avant = input ("Les mailles au début sont : ")
        texte_repetees = input("Les mailles répétées sont : ")
        texte_apres = input("Les mailles de la fin sont : ")

        instructions_rang = {
            "type_rang": sens_rang,
            "avant": parser_sequence(texte_avant),
            "repetees":parser_sequence(texte_repetees),
            "apres":parser_sequence(texte_apres)
        }

        instructions.append(instructions_rang)
    
    motif = {
        "nom_motif":nom_motif,
        "coefficient_horizontal":coefficient_horizontal,
        "coefficient_vertical":coefficient_vertical,
        "couleur_motif":couleur_motif,
        "instructions": instructions
    }

    return motif

if __name__ == "__main__":
    motif = creer_motif()

    nom_fichier = motif["nom_motif"].lower().replace(" ", "_") + ".json"

    with open(nom_fichier, "w", encoding="utf-8") as fichier:
        json.dump(
            motif,
            fichier,
            indent=4,
            ensure_ascii=False
        )

    print(f"Motif enregistré dans {nom_fichier}")
    