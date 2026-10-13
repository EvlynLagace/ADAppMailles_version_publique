from appTricot.domaine.maille import TypeMaille

def afficher_grille(rangs):

    grille = []

    for r in rangs:

        ligne = r["mailles"]

        if r["type_rang"] == "ENDROIT":
            ligne = ligne[::-1]
            type_rang = "ENDROIT"
        elif r["type_rang"] == "ENVERS":
            type_rang = "ENVERS"
        else:
            raise ValueError(f"type de rang inattendu : ({r['type_rang']})")

        grille.insert(0, {
            "mailles": ligne,
            "type_rang": type_rang
        })

    return grille

def construire_grille_pdf(tuile):

    grille = []
    instructions = list(tuile.motif.instructions)

    reste = tuile.motif_structure["reste"]
    nb_repetitions = tuile.motif_structure["nb_repetitions"]

    for i in range(tuile.nb_rangs_effectif):

        m = instructions[i % len(instructions)]

        if m.est_pattern_simple:

            nb_mailles_grille = tuile.motif.nb_mailles_minimum

            grille.append({
                "numero": i + 1,
                "type_rang": m.type_rang.name,

                "bordure": ["K"] * (reste // 2),

                "avant": [],

                "milieu": groupe_to_mailles(m.repetees) * (nb_mailles_grille//m.nb_mailles_repetees),

                "nb_repetitions": nb_repetitions,

                "apres": [],

                "est_pattern_simple": m.est_pattern_simple,
            })

        else:

            grille.append({
                "numero": i + 1,
                "type_rang": m.type_rang.name,

                "bordure": ["K"] * (reste // 2),

                "avant": groupe_to_mailles(m.avant),

                "milieu": groupe_to_mailles(m.repetees),

                "nb_repetitions": nb_repetitions,

                "apres": groupe_to_mailles(m.apres),

                "est_pattern_simple": m.est_pattern_simple,
            })


    return grille

def preparer_grille_affichage(grille):
    grille_affichage = []

    for rang in reversed(grille):
        ligne = {
            "bordure": rang["bordure"],
            "avant": rang["avant"],
            "milieu": rang["milieu"],
            "repetitions": rang["nb_repetitions"],
            "apres": rang["apres"],
        }

        if rang["type_rang"] == "ENDROIT":
            ligne = {
                "bordure": list(reversed(rang["bordure"])),
                "avant" : list(reversed(rang["apres"])),
                "milieu": list(reversed(rang["milieu"])),
                "apres" : list(reversed(rang["avant"])),
                "repetitions": rang["nb_repetitions"],
            }

        nb_mailles_sans_bordure = (
            len(rang["avant"]) +
            len(rang["milieu"]) * rang["nb_repetitions"]+
            len(rang["apres"])
        )

        grille_affichage.append({
            "numero": rang["numero"],
            "type_rang" : rang["type_rang"],
            "bordure": ligne["bordure"],
            "avant": ligne["avant"],
            "milieu": ligne["milieu"],
            "apres": ligne["apres"],
            "nb_repetitions": ligne["repetitions"],
            "est_pattern_simple": rang["est_pattern_simple"],
            "nb_mailles_sans_bordure": nb_mailles_sans_bordure,
        })

    return grille_affichage

def groupe_to_mailles(groupe):
    mailles = []

    for maille, n in groupe:
        mailles.extend([maille.value] * n)

    return mailles

def construire_legende(motif):

    legende = set()

    for rang in motif.instructions:

        groupes = [rang.avant, rang.repetees, rang.apres]

        for groupe in groupes:
            for maille, _ in groupe:

                if rang.type_rang.name == "ENDROIT":

                    if maille == TypeMaille.ENDROIT:
                        legende.add(("sens_tricot",
                                     "Maille endroit sur rang endroit"))
                    elif maille == TypeMaille.ENVERS:
                        legende.add(("inverse_tricot",
                                     "Maille envers sur rang endroit"))
                    elif maille == TypeMaille.WYIF:
                        legende.add(("with_yarn_in_front",
                                     "Glisser une maille, fil devant"))
                    elif maille == TypeMaille.WYIB:
                        legende.add(("with_yarn_in_back",
                                     "Glisser une maille, fil derrière"))

                elif rang.type_rang.name == "ENVERS":

                    if maille == TypeMaille.ENDROIT:
                        legende.add(("inverse_tricot",
                                     "Maille endroit sur rang envers"))
                    elif maille == TypeMaille.ENVERS:
                        legende.add(("sens_tricot",
                                     "Maille envers sur rang envers"))
                    elif maille == TypeMaille.WYIF:
                        legende.add(("with_yarn_in_front",
                                     "Glisser une maille, fil devant"))
                    elif maille == TypeMaille.WYIB:
                        legende.add(("with_yarn_in_back",
                                     "Glisser une maille, fil derrière"))

                else:
                    raise ValueError(f"Type de rang inattendu : { rang.type_rang }")
                        
    order = {
    "sens_tricot": 0,
    "inverse_tricot": 1,
    "with_yarn_in_front": 2,
    "with_yarn_in_back": 3
}
    return sorted(legende, key=lambda x: order.get(x[0], 999))      

def generer_instructions_textuelles(sequence_mailles):

    instructions = []
    
    for maille, n in sequence_mailles:
        instructions.append(f'{n} <i>{maille.abreviation}</i>')

    return ", ".join(instructions)

def generer_instructions_textuelles_pattern_simple(sequence_mailles, nb_mailles_tuile_remplissage):

    ligne = []
    nb_mailles_milieu = 0

    for maille, n in sequence_mailles:
        nb_mailles_milieu += n
        ligne.append(f'{n} <i>{maille.abreviation}</i>')

    ligne.append(f'{nb_mailles_tuile_remplissage//nb_mailles_milieu} fois')
    
    return ", ".join(ligne)

def afficher_tuile_texte (motif, nb_rangs_tuile:int=0, nb_mailles_tuile:int=0, nb_repetitions:int = 1, reste:int=0):

    lignes = []
    instructions = list(motif.instructions)

    for i in range(nb_rangs_tuile):

        m = instructions[i % len(instructions)]
        simple = m.est_pattern_simple

        bordure = f"{(reste//2)} end." if reste >0 else ""
    
        a = m.avant
        milieu = m.repetees
        ap = m.apres

        avant_txt = ""
        if a:
            avant_txt = generer_instructions_textuelles(a)

        milieu_txt=""
        if milieu:
            if simple:
                nb_mailles_tuile_remplissage = nb_mailles_tuile - reste//2
                milieu_txt = generer_instructions_textuelles_pattern_simple(milieu, nb_mailles_tuile_remplissage)
            else:
                milieu_txt = generer_instructions_textuelles(milieu)

        apres_txt = ""
        if ap:
            apres_txt = generer_instructions_textuelles(ap)


        lignes.append({
            "numero": i +1,
            "type_rang":m.type_rang.value,
            "bordure":bordure,
            "avant":avant_txt,
            "milieu":milieu_txt,
            "nb_repetitions":nb_repetitions,
            "apres": apres_txt,
            "simple": simple
        })
    
    return lignes