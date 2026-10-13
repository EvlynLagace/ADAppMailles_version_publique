from tkinter import Button, Label, Frame

from adappmailles.ui.afficher_patron_motif_tk import afficher_patron_motif_tk


def afficher_catalogue_motifs_tk(root, catalogue, controleur=None, retour_accueil=None):
    from adappmailles.ui.utils import clear_root

    clear_root(root)
    root.title("Catalogue des motifs")

    Label(root, text="Motifs disponibles", font=("Helvetica", 18, "bold")).pack(pady=10)

    frame = Frame(root)
    frame.pack()

    def ouvrir_motif(motif):
        afficher_patron_motif_tk(motif)

    for motif in catalogue.motifs:
        Button(
            frame,
            text=motif.nom_motif,
            command=lambda m=motif: ouvrir_motif(m)
        ).pack(pady=3)

    Button(root, text="Retour", command=retour_accueil).pack(pady=10)