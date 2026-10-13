
def compresser_mailles(mailles):
    if not mailles:
        return ""
    
    resultat = []
    courant = str(mailles[0])
    count = 1

    for m in mailles[1:]:
        t = str(m)
        if t == courant:
            count += 1
        else:
            resultat.append(f"{courant}{count}" if count>1 else courant)
            courant = t
            count = 1

    resultat.append(f"{courant}{count}" if count>1 else courant)

    return ", ".join(resultat)

def rang_vers_texte(rang, index):
    type_rang = str(rang)

    mailles = compresser_mailles(rang.mailles)

    return f"Rang {index + 1} ({type_rang}) : {mailles}"

def motif_vers_texte(motif):
    lignes = []

    for i, rang in enumerate(motif.rangs):
        type_rang = str(rang)
        mailles = compresser_mailles(rang.mailles)

        lignes.append(f"Rang {i + 1} ({type_rang}) : {mailles}")

    return "\n".join(lignes)
    