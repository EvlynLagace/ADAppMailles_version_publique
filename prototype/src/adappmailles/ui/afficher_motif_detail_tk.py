from tkinter import Canvas, Label, Button, Toplevel

def afficher_motif_detail_tk(root, motif, catalogue, retour_catalogue):

    from adappmailles.ui.constants import TILE_CELL_SIZE
    from adappmailles.ui.utils import clear_root

    clear_root(root)
    root.title(motif.nom_motif)

    # -------------------------
    # TEXTE DEBUG
    # -------------------------
    texte = f"""
Nom : {motif.nom_motif}
Mailles répétées : {motif.nb_mailles_repetees}
Mailles ajoutées : {motif.nb_mailles_ajoutees}
Minimum : {motif.nb_mailles_minimum}
"""

    Label(root, text=texte, justify="left").pack(pady=10)

    # -------------------------
    # GRILLE
    # -------------------------
    grille = motif.patron
    nb_rangs = len(grille)
    nb_mailles = motif.nb_mailles_minimum

    canvas = Canvas(
        root,
        width=nb_mailles * TILE_CELL_SIZE,
        height=nb_rangs * TILE_CELL_SIZE,
        bg="white"
    )
    canvas.pack()

    for i, rang_modele in enumerate(grille):
        for j, maille in enumerate(
            rang_modele.avant + rang_modele.repetees + rang_modele.apres
        ):

            x0 = j * TILE_CELL_SIZE
            y0 = i * TILE_CELL_SIZE
            x1 = x0 + TILE_CELL_SIZE
            y1 = y0 + TILE_CELL_SIZE

            couleur = "lightblue" if maille.type_maille.name == "ENDROIT" else "pink"

            canvas.create_rectangle(x0, y0, x1, y1, fill=couleur, outline="black")

    # -------------------------
    Button(
        root,
        text="Retour catalogue",
        command=retour_catalogue
    ).pack(pady=10)