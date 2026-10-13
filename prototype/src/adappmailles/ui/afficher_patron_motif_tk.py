from adappmailles.modele.maille import TypeMaille
from adappmailles.services.generateur_patron import GenerateurPatron
from adappmailles.ui.constants import CANVAS_MARGIN, TILE_CELL_SIZE


def afficher_patron_motif_tk(motif):
    from tkinter import Canvas, Toplevel

    fenetre = Toplevel()
    fenetre.title(f"Motif : {motif.nom_motif}")

    generateur = GenerateurPatron()
    patron = generateur.generer(motif)

    nb_mailles = len(list(patron[0]))
    nb_rangs = len(patron)   

    largeur_px = nb_mailles * TILE_CELL_SIZE
    hauteur_px = nb_rangs * TILE_CELL_SIZE

    canvas = Canvas(
        fenetre,
        width=largeur_px + 2 * CANVAS_MARGIN,
        height=hauteur_px + 2 * CANVAS_MARGIN,
        bg="white"
    )
    canvas.pack()

    for index_rang, rang in enumerate(patron):

        y0 = CANVAS_MARGIN + (nb_rangs - 1 -index_rang) * TILE_CELL_SIZE
        y1 = y0 + TILE_CELL_SIZE
        y_centre = (y0 + y1) / 2

        # numéro de rang
        canvas.create_text(
            CANVAS_MARGIN - 5 if rang.est_envers else largeur_px + CANVAS_MARGIN + 5,
            y_centre,
            text=str(index_rang + 1),
            anchor="e" if rang.est_envers else "w"
    )

        mailles = list(rang)

        if rang.est_endroit:
            mailles = list(reversed(mailles))

        for index_maille, maille in enumerate(mailles):

            x0 = CANVAS_MARGIN + index_maille * TILE_CELL_SIZE

            x1 = x0 + TILE_CELL_SIZE

            if (rang.est_endroit and maille.type_maille == TypeMaille.ENDROIT) or \
                (rang.est_envers and maille.type_maille == TypeMaille.ENVERS):
                couleur = "lightblue"
            else:
                couleur = "pink"

            canvas.create_rectangle(x0, y0, x1, y1, fill=couleur, outline="black")