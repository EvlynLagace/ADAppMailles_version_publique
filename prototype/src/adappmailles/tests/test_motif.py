from adappmailles.modele.motif import Motif
from adappmailles.modele.rang import TypeRang
from adappmailles.modele.rang_instructions import RangInstructions


def test_motif_par_defaut():
    motif = Motif()

    assert motif.nom_motif is None
    assert motif.instructions == []
    assert motif.coefficient ==1
    assert motif.couleur_motif is None

def test_motif_simple_calcul_mailles():
    instruction = RangInstructions(
        avant=[("K", 1)],
        repetees=[("K", 2)],
        apres=[("K", 1)]
    )

    motif = Motif(instructions=[instruction])

    assert motif.nb_mailles_repetees == 2
    assert motif.nb_mailles_ajoutees == 2
    assert motif.nb_mailles_minimum == 4

def test_motif_ignore_autres_instructions():
    instruction1 = RangInstructions(
        avant=[("K", 1)],
        repetees=[("K", 2)],
        apres=[("K", 1)]
    )

    instruction2 = RangInstructions(
        avant=[("K", 10)],
        repetees=[("K", 10)],
        apres=[("K", 10)]
    )

    motif = Motif(instructions=[instruction1, instruction2])

    assert motif.nb_mailles_minimum == 4

def test_parse_group_simple():
    data = [
        {"type": "K", "n": 2},
        {"type": "P", "n": 1}
    ]

    result = Motif._parse_group(data)

    assert result == [("K", 2), ("P", 1)]

def test_motif_from_json_jersey():
    data = {
        "nom_motif": "Jersey",
        "coefficient": 1,
        "instructions": [
            {
                "type_rang": "ENDROIT",
                "avant": [],
                "repetees": [{"type": "K", "n": 1}],
                "apres": []
            },
            {
                "type_rang": "ENVERS",
                "avant": [],
                "repetees": [{"type": "P", "n": 1}],
                "apres": []
            }
        ]
    }

    motif = Motif.from_json(data)

    assert motif.nom_motif == "Jersey"
    assert motif.coefficient == 1
    assert len(motif.instructions) == 2

def test_motif_from_json_calculs():
    data = {
        "nom_motif": "Test",
        "coefficient": 1,
        "instructions": [
            {
                "type_rang": "ENDROIT",
                "avant": [],
                "repetees": [{"type": "K", "n": 2}],
                "apres": []
            }
        ]
    }

    motif = Motif.from_json(data)

    assert motif.nb_mailles_repetees == 2
    assert motif.nb_mailles_minimum == 2

def test_motif_to_json_simple():
    r = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[("K", 1)],
        repetees=[("P", 2)],
        apres=[]
    )

    motif = Motif(
        nom_motif="Test",
        coefficient=1,
        instructions=[r]
    )

    result = motif.to_json()

    assert result == {
        "nom_motif": "Test",
        "coefficient": 1,
        "instructions": [
            {
                "type_rang": "ENDROIT",
                "avant": [{"type": "K", "n": 1}],
                "repetees": [{"type": "P", "n": 2}],
                "apres": []
            }
        ]
    }

def test_motif_to_json_structure():
    r = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[],
        repetees=[("K", 1)],
        apres=[]
    )

    motif = Motif("Test", instructions=[r], coefficient=1)

    data = motif.to_json()

    assert data["nom_motif"] == "Test"
    assert data["coefficient"] == 1
    assert isinstance(data["instructions"], list)
    assert len(data["instructions"]) == 1

def test_motif_round_trip():
    # 1. motif original
    r = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[("K", 1)],
        repetees=[("P", 2)],
        apres=[("K", 1)]
    )

    original = Motif(
        nom_motif="Test",
        coefficient=1,
        instructions=[r]
    )

    # 2. sérialisation
    data = original.to_json()

    # 3. reconstruction
    reconstruit = Motif.from_json(data)

    # 4. vérifications
    assert reconstruit.nom_motif == original.nom_motif
    assert reconstruit.coefficient == original.coefficient

    assert len(reconstruit.instructions) == len(original.instructions)

    # comparaison du premier rang (simple et suffisant au début)
    r1 = reconstruit.instructions[0]
    r0 = original.instructions[0]

    assert r1.type_rang == r0.type_rang
    assert r1.avant == r0.avant
    assert r1.repetees == r0.repetees
    assert r1.apres == r0.apres