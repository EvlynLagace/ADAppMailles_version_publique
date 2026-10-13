from appTricot.services.motifs_service import afficher_motif_texte, charger_motifs
from appTricot.domaine.rang_instructions import RangInstructions
from appTricot.domaine.rang import TypeRang
from appTricot.domaine.motif import Motif


def test_afficher_motif_texte_basic():
    r1 = RangInstructions(
        type_rang=TypeRang.ENDROIT,
        avant=[('K', 1)],
        repetees=[('P', 2)],
        apres=[('K', 1)],
    )

    r2 = RangInstructions(
        type_rang=TypeRang.ENVERS,
        avant=[],
        repetees=[('K', 1)],
        apres=[],
    )

    motif = Motif(nom_motif="test", instructions=[r1, r2])

    lignes = afficher_motif_texte(motif)

    assert lignes[0] == "Rang 1(endroit) : K1 * P2 * K1"
    assert lignes[1] == "Rang 2(envers) :  * K1 * "


def test_afficher_motif_texte_empty():
    motif = Motif(nom_motif="vide", instructions=[])
    assert afficher_motif_texte(motif) == []


def test_charger_motifs_loads_catalogue():
    motifs = charger_motifs()
    assert isinstance(motifs, list)
    assert any(getattr(m, 'nom_motif', None) == 'Jersey' for m in motifs)
