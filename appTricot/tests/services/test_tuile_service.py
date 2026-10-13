from appTricot.services.tuile_service import (
    rang_instructions_to_mailles,
    motif_to_rangs,
    tuile_to_rangs,
    afficher_tuile_texte,
)
from appTricot.domaine.rang_instructions import RangInstructions
from appTricot.domaine.rang import TypeRang
from appTricot.domaine.motif import Motif


def test_rang_instructions_to_mailles_pattern_simple():
    r = RangInstructions(type_rang=TypeRang.ENDROIT, repetees=[('K', 1)])
    mailles = rang_instructions_to_mailles(r, nb_repetitions=1, nb_mailles_tuile=5, reste=0)
    assert mailles == ['K', 'K', 'K', 'K', 'K']


def test_rang_instructions_to_mailles_complex():
    r = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[('K', 1)],
        repetees=[('P', 2)],
        apres=[('K', 1)],
    )
    mailles = rang_instructions_to_mailles(r, nb_repetitions=2, nb_mailles_tuile=0)
    assert mailles == ['K', 'P', 'P', 'P', 'P', 'K']


def test_motif_to_rangs_and_tuile_to_rangs():
    r1 = RangInstructions(type_rang=TypeRang.ENDROIT, repetees=[('K', 1)])
    r2 = RangInstructions(type_rang=TypeRang.ENVERS, repetees=[('P', 1)])
    motif = Motif(nom_motif='m', instructions=[r1, r2])

    rangs = motif_to_rangs(motif, nb_repetitions=1, nb_mailles_tuile=4)
    assert isinstance(rangs, list)
    assert all('mailles' in r and 'type_rang' in r for r in rangs)

    tr = tuile_to_rangs(motif, nb_rangs_tuile=3, nb_repetitions=1, nb_mailles_tuile=4)
    assert len(tr) == 3
    assert tr[0]['numero'] == 1
    assert tr[2]['numero'] == 3


def test_afficher_tuile_texte_structure():
    r1 = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[('K', 1)],
        repetees=[('P', 2)],
        apres=[],
    )
    r2 = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=[('K', 1)],
        apres=[],
    )
    motif = Motif(nom_motif='m', instructions=[r1, r2])

    lignes = afficher_tuile_texte(motif, nb_rangs_tuile=2, nb_repetitions=1, reste=2)
    assert isinstance(lignes, list)
    assert lignes[0]['numero'] == 1
    assert lignes[0]['type_rang'] in ('endroit', 'envers')
    assert lignes[0]['bordure'] == 'K1'
    assert lignes[0]['avant'] == 'K1'
    assert lignes[0]['milieu'] == 'P2'
    assert lignes[1]['numero'] == 2
