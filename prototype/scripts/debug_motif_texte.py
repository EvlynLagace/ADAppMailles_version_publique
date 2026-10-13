from adappmailles.controleur.application import ApplicationControleur
from adappmailles.services.format_texte import motif_vers_texte


def main():
    app = ApplicationControleur()
    app.configurer()

    # génération complète
    couverture = app.generer()

    # récupérer une tuile
    tuile = couverture.tuiles[0][0]

    print("=== MOTIF ===")
    print(tuile.motif.nom_motif)

    print("\n=== TEXTE ===")
    print(motif_vers_texte(tuile))

if __name__ == "__main__":
    main()