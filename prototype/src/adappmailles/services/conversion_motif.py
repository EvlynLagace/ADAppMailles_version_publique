from adappmailles.modele.maille import Maille, TypeMaille
from adappmailles.modele.rang import Rang, TypeRang

#Premiere etape : convertir une instruction du motif en maille

def expand_instruction(instr):
    kind, n = instr

    if kind == "K":
        return[Maille(TypeMaille.ENDROIT) for _ in range(n)]
    
    if kind == "P":
        return[Maille(TypeMaille.ENVERS) for _ in range(n)]
    
    raise ValueError(f"Instruction inconnue : {kind}")

def pattern_to_rang(pattern):
    mailles = []

    for instr in pattern.avant:
        mailles += expand_instruction(instr)

    for instr in pattern.repetees:
        mailles += expand_instruction(instr)

    for instr in pattern.apres:
        mailles += expand_instruction(instr)

    return Rang(
        type_rang=pattern.type_rang,
        mailles = mailles
    )

def pattern_to_mailles(pattern, nb_repetitions=1, reste=0, taille_cible=None):

    mailles = []
    reste_gauche = reste // 2
    reste_droit = reste - reste_gauche

    est_endroit = pattern.type_rang == TypeRang.ENDROIT

    if not est_endroit:
        reste_gauche, reste_droit = reste_droit, reste_gauche
        
        
    mailles.extend([Maille(TypeMaille.ENDROIT) for _ in range(reste_gauche)])

    for instr in pattern.avant:
        mailles.extend(expand_instruction(instr))

    for _ in range(nb_repetitions):
        for instr in pattern.repetees:
            mailles.extend(expand_instruction(instr))

    for instr in pattern.apres:
        mailles.extend(expand_instruction(instr))

    mailles.extend([Maille(TypeMaille.ENDROIT) for _ in range(reste_droit)])
        

    # 🔥 NORMALISATION FINALE
    if taille_cible is not None:
        while len(mailles) < taille_cible:
            mailles.append(Maille(TypeMaille.ENDROIT))

        mailles = mailles[:taille_cible]

    return mailles