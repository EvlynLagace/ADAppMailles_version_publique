from adappmailles.data.motifs_test_listes import get_motifs_test_listes
from adappmailles.modele.catalogue import Catalogue
from adappmailles.services.conversion_motif import pattern_to_mailles
from adappmailles.modele.rang import TypeRang


def afficher_mailles(mailles):
    return [m.type_maille.value for m in mailles]


def debug_pattern(pattern, nb_repetitions, reste):
    print("\n--- DEBUG PATTERN ---")
    print("Type rang:", pattern.type_rang)
    print("Avant:", pattern.avant)
    print("Repetees:", pattern.repetees)
    print("Apres:", pattern.apres)
    print("Nb répétitions:", nb_repetitions)
    print("Reste:", reste)

    mailles = pattern_to_mailles(pattern, nb_repetitions, reste)

    print("Mailles:", afficher_mailles(mailles))
    print("Total:", len(mailles))


def main():
    motifs = get_motifs_test_listes()

    # 🔥 Choisis un motif problématique ici
    motif = next(m for m in motifs if m.nom_motif == "TV Static")

    print("=== MOTIF:", motif.nom_motif, "===")

    for i, pattern in enumerate(motif.instructions):
        debug_pattern(pattern, nb_repetitions=3, reste=2)

    catalogue = Catalogue.from_json_file(
    "src/adappmailles/data/catalogue.json"
)

    print(catalogue.motifs[1].nom_motif)


if __name__ == "__main__":
    main()