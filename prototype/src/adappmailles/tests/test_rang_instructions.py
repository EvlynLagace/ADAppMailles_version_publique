from adappmailles.modele.maille import Maille
from adappmailles.modele.rang import TypeRang
from adappmailles.modele.rang_instructions import RangInstructions


def test_rang_instructions_par_defaut():
    r = RangInstructions()

    assert r.type_rang == TypeRang.ENDROIT
    assert r.avant == []
    assert r.repetees == []
    assert r.apres == []

def test_rang_instructions_construction():
    r = RangInstructions(
        avant=[(Maille(), 1)],
        repetees=[(Maille(), 2)],
        apres=[(Maille(), 3)]
    )

    assert len(r.avant) == 1
    assert len(r.repetees) == 1
    assert len(r.apres) == 1

def test_nb_mailles_repetees():
    r = RangInstructions(
        repetees=[(Maille(), 2), (Maille(), 3)]
    )

    assert r.nb_mailles_repetees == 5

def test_nb_mailles_ajoutees():
    r = RangInstructions(
        avant=[(Maille(), 1), (Maille(), 2)],
        apres=[(Maille(), 3)]
    )

    assert r.nb_mailles_ajoutees == 6

def test_rang_instructions_complet():
    r = RangInstructions(
        avant=[(Maille(), 1)],
        repetees=[(Maille(), 2)],
        apres=[(Maille(), 3)]
    )

    assert r.nb_mailles_repetees == 2
    assert r.nb_mailles_ajoutees == 4

def test_independance_listes():
    base = [(Maille(), 1)]
    r = RangInstructions(avant=base)

    base.append((Maille(), 2))

    assert len(r.avant) == 1

def test_encode_group_simple():
    group = [("K", 2), ("P", 1)]

    result = RangInstructions._encode_group(group)

    assert result == [
        {"type": "K", "n": 2},
        {"type": "P", "n": 1}
    ]

def test_rang_to_json():
    r = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[("K", 1)],
        repetees=[("P", 2)],
        apres=[("K", 1)]
    )

    result = r.to_json()

    assert result == {
        "type_rang": "ENDROIT",
        "avant": [{"type": "K", "n": 1}],
        "repetees": [{"type": "P", "n": 2}],
        "apres": [{"type": "K", "n": 1}],
    }

def test_encode_group_vide():
    assert RangInstructions._encode_group([]) == []