from adappmailles.data.motifs_test_listes import get_motifs_test_listes
from adappmailles.modele.tuile import Tuile
from adappmailles.modele.echantillon import Echantillon
from adappmailles.services.generateur_tuile import GenerateurTuile


def afficher_mailles(mailles):
    return [m.type_maille.value for m in mailles]


def debug_tuile(tuile):
    print("\n========================")
    print("TUILE")
    print("mailles:", tuile.nb_mailles)
    print("rangs:", tuile.nb_rangs)
    print("motif:", tuile.motif.nom_motif)

    print("\nSTRUCTURE:")
    print(tuile.motif_structure)

    print("\nRANGS:")
    for i, rang in enumerate(tuile.rangs):
        print(f"\n--- Rang {i} ---")
        print("Type:", rang.type_rang)
        print("Nb mailles:", len(rang.mailles))
        print("Mailles:", afficher_mailles(rang.mailles))


def main():
    # 🔧 setup minimal
    motifs = get_motifs_test_listes()

    echantillon = Echantillon(10,10,10,10)

    tuile = Tuile(largeur_cm=20, hauteur_cm=20)
    tuile.initialiser_dimensions(echantillon)

    # 🔥 choisir un motif (change ici)
    motif = next(m for m in motifs if m.nom_motif == "Seed Blocks")
    tuile.motif = motif

    generateur = GenerateurTuile()

    # ⚙️ calcul
    generateur.calculer_structure_motif(tuile)
    generateur.construire_rangs(tuile)

    # 🔍 debug
    debug_tuile(tuile)


if __name__ == "__main__":
    main()