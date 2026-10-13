from tkinter import Button, Canvas, Label

from adappmailles.ui.constants import *
from adappmailles.ui.patron import afficher_patron_tuile_tk
from adappmailles.ui.utils import clear_root
from adappmailles.ui import components


def afficher_couverture_tk(root, couverture, controleur, retour_accueil) -> None:
    """Affiche le plan de la couverture avec les tuiles."""

    clear_root(root)
    root.title("Couverture")

    # Dimensions globales
    largeur_px = couverture.largeur_cm * DEFAULT_SCALE
    hauteur_px = couverture.hauteur_cm * DEFAULT_SCALE

    canvas = Canvas(root, width=largeur_px, height=hauteur_px, bg="white")
    canvas.pack()

    canvas.create_rectangle(0, 0, largeur_px, hauteur_px, outline="black", width=2)

    # --- Dessin des tuiles ---
    for index_ligne, ligne in enumerate(couverture.tuiles):
        for index_colonne, tuile in enumerate(ligne):

            motif = tuile.motif

            # Sécurité : motif peut ne pas être encore assigné
            couleur = motif.couleur_motif if motif else "lightgrey"
            nom = motif.nom_motif if motif else "?"

            x0 = index_colonne * tuile.largeur_cm * DEFAULT_SCALE
            y0 = index_ligne * tuile.hauteur_cm * DEFAULT_SCALE
            x1 = x0 + tuile.largeur_cm * DEFAULT_SCALE
            y1 = y0 + tuile.hauteur_cm * DEFAULT_SCALE

            canvas.create_rectangle(
                x0, y0, x1, y1,
                outline="blue",
                fill=couleur
            )

            canvas.create_text(
                x0 + TILE_TEXT_OFFSET,
                y0 + TILE_TEXT_OFFSET,
                text=f"({index_ligne},{index_colonne})\n{nom}",
                anchor="nw"
            )

    # --- Clic sur une tuile ---
    def on_click(event):
        x = event.x
        y = event.y

        largeur_tuile_px = couverture.tuiles[0][0].largeur_cm * DEFAULT_SCALE
        hauteur_tuile_px = couverture.tuiles[0][0].hauteur_cm * DEFAULT_SCALE

        index_colonne = int(x // largeur_tuile_px)
        index_ligne = int(y // hauteur_tuile_px)

        if (0 <= index_ligne < len(couverture.tuiles) and
                0 <= index_colonne < len(couverture.tuiles[0])):

            tuile = couverture.tuiles[index_ligne][index_colonne]

            # sécurité : motif peut être None
            if tuile.motif:
                afficher_patron_tuile_tk(tuile)
            else:
                print("Tuile sans motif (pas encore générée)")

    canvas.bind("<Button-1>", on_click)

    # --- Boutons bas de page ---
    Button(root, text="Nouvelle couverture", command=retour_accueil).pack(pady=10)

    label_couverture = Label(root, text="")
    label_couverture.pack()

    label_echantillon = Label(root, text="")
    label_echantillon.pack()

    components.afficher_parametres_couverture(label_couverture, controleur)
    components.afficher_parametres_echantillon(label_echantillon, controleur)