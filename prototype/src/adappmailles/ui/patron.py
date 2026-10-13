import math
from tkinter import Canvas, Toplevel

from adappmailles.modele.maille import TypeMaille
from adappmailles.modele.rang import TypeRang
from adappmailles.services.format_texte import motif_vers_texte
from adappmailles.ui.constants import *


def afficher_patron_tuile_tk(tuile) -> None:

    rangs = tuile.rangs

    print("\n=== PATRON TEXTE ===")
    print(tuile.motif.nom_motif)
    print(motif_vers_texte(tuile))

    fenetre = Toplevel()
    fenetre.title(f"Tuile - Motif: {tuile.motif.nom_motif if tuile.motif else 'N/A'}")

    #nombre mailles effectives, puis mailles_effectives partout ou tuile.nb_mailles ?

    largeur_px = math.ceil(tuile.nb_mailles / tuile.motif.coefficient) * TILE_CELL_SIZE
    hauteur_px = tuile.nb_rangs * TILE_CELL_SIZE

    canvas = Canvas(
        fenetre,
        width=largeur_px + 2 * CANVAS_MARGIN,
        height=hauteur_px + 2 * CANVAS_MARGIN,
        bg="white"
    )
    canvas.pack()

    canvas.create_rectangle(
        CANVAS_MARGIN,
        CANVAS_MARGIN,
        largeur_px + CANVAS_MARGIN,
        hauteur_px + CANVAS_MARGIN,
        outline="black",
        width=2
    )

    # -------------------------
    # AFFICHAGE DES RANGS
    # -------------------------
    for index_rang, rang in enumerate(rangs):

        y0 = CANVAS_MARGIN + (tuile.nb_rangs - 1 - index_rang) * TILE_CELL_SIZE
        y1 = y0 + TILE_CELL_SIZE
        y_centre = (y0 + y1) / 2

        # numéro de rang
        canvas.create_text(
            CANVAS_MARGIN - 5 if rang.type_rang == TypeRang.ENVERS else largeur_px + CANVAS_MARGIN + 5,
            y_centre,
            text=str(index_rang + 1),
            anchor="e" if rang.type_rang == TypeRang.ENVERS else "w"
        )

        # mailles
        for index_maille, maille in enumerate(rang.mailles):

            if rang.type_rang == TypeRang.ENDROIT:
                x0 = CANVAS_MARGIN + (math.ceil(tuile.nb_mailles / tuile.motif.coefficient) - index_maille - 1) * TILE_CELL_SIZE
            else:
                x0 = CANVAS_MARGIN + index_maille * TILE_CELL_SIZE

            x1 = x0 + TILE_CELL_SIZE

            couleur = "lightblue"
            if rang.type_rang == TypeRang.ENDROIT and maille.type_maille == TypeMaille.ENVERS:
                couleur = "pink"
            if rang.type_rang == TypeRang.ENVERS and maille.type_maille == TypeMaille.ENDROIT:
                couleur = "pink"

            canvas.create_rectangle(x0, y0, x1, y1, outline="red", fill=couleur)

            canvas.create_text(
                x0 + 5,
                y0 + 5,
                text=str(maille)
            )

    # -------------------------
    # NUMÉROS COLONNES
    # -------------------------
    for index_maille in range(math.ceil(tuile.nb_mailles/tuile.motif.coefficient)):
        x0 = CANVAS_MARGIN + index_maille * TILE_CELL_SIZE
        x1 = x0 + TILE_CELL_SIZE

        canvas.create_text(
            (x0 + x1) / 2,
            CANVAS_MARGIN + tuile.nb_rangs * TILE_CELL_SIZE + 5,
            text=str(math.ceil(tuile.nb_mailles/tuile.motif.coefficient)- index_maille),
            anchor="n"
        )