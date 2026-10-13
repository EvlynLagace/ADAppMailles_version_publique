import pytest
from adappmailles.data.motifs_test_listes import get_motifs_test_listes
from adappmailles.modele.maille import TypeMaille
from adappmailles.modele.rang_instructions import RangInstructions
from adappmailles.modele.rang import TypeRang
from adappmailles.services.conversion_motif import expand_instruction, pattern_to_rang

#Test 1 : cas K pour maille endroit
def test_expend_K():
    result = expand_instruction(("K", 3))

    assert len(result) == 3
    assert all(m.type_maille == TypeMaille.ENDROIT for m in result)

#Test 2 : cas P pour maille envers
def test_expend_P():
    result = expand_instruction(("P", 2))

    assert len(result) == 2
    assert all(m.type_maille == TypeMaille.ENVERS for m in result)

#Test 3 : erreur
def test_expend_erreur():
    with pytest.raises(ValueError):
        expand_instruction(("X", 1))

#Test 4 : tester si pattern to rang fonctionne pour un motif simple
def test_pattern_to_rang_jersey():
    pattern = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees=[("K", 2)],
        apres=[]
    )

    rang = pattern_to_rang(pattern)

    assert len(rang.mailles) == 2
    assert all(m.type_maille == TypeMaille.ENDROIT for m in rang.mailles)

# test avec un motif mixte
def test_pattern_to_rang_mix():
    pattern = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[("K", 1)],
        repetees=[("P", 2)],
        apres=[("K", 1)]
    )

    rang = pattern_to_rang(pattern)

    types = [m.type_maille for m in rang.mailles]

    assert types == [
        TypeMaille.ENDROIT,
        TypeMaille.ENVERS, TypeMaille.ENVERS,
        TypeMaille.ENDROIT
    ]

#test avec le jersey provenant de la liste de motifs test
def test_motif_jersey_rangs():
    motifs = get_motifs_test_listes()
    jersey = next(m for m in motifs if m.nom_motif == "Jersey")

    rang0 = pattern_to_rang(jersey.instructions[0])
    rang1 = pattern_to_rang(jersey.instructions[1])

    # Rang endroit → K
    assert all(m.type_maille == TypeMaille.ENDROIT for m in rang0.mailles)

    # Rang envers → P
    assert all(m.type_maille == TypeMaille.ENVERS for m in rang1.mailles)