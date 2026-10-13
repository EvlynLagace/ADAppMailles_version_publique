import os
from tkinter import Button, Label


from adappmailles.ui.afficher_catalogue_motifs_tk import afficher_catalogue_motifs_tk
from adappmailles.ui.components import afficher_parametres_couverture, afficher_parametres_echantillon
from adappmailles.ui.couverture_tk import afficher_couverture_tk
from adappmailles.ui.dialogs import lire_dimensions_tk, lire_parametres_echantillon_tk

from .utils import charger_image, clear_root



def fenetre_accueil(root, controleur):

    image_path = os.path.join(os.path.dirname(__file__), "../assets/images/pelote-de-laine.png")

    tk_image = charger_image(image_path, (250,250))

    # Vide la racine
    clear_root(root)
    
    root.title("Accueil")
    titre = Label(root, text="Bienvenue dans mon application de tricot !", font=("Helvetica", 24, "bold"))
    titre.pack(pady=20)

    label_image = Label(root, image=tk_image)
    label_image.image = tk_image  # garder la référence
    label_image.pack(pady=10)
  
    def generer_couverture():
        controleur.configurer()
        controleur.generer()

        couverture=controleur.couverture

        afficher_couverture_tk(root, couverture, controleur, retour_accueil=lambda: fenetre_accueil(root, controleur))

    def definir_couverture():
        largeur, hauteur = lire_dimensions_tk(root)
        controleur.valeurs["largeur_couverture"] = largeur
        controleur.valeurs["hauteur_couverture"] = hauteur

        afficher_parametres_couverture(label_couverture, controleur)

    def definir_echantillon():
        l, h, nb_m, nb_r = lire_parametres_echantillon_tk(root)
        controleur.valeurs["largeur_echantillon"] = l
        controleur.valeurs["hauteur_echantillon"] = h
        controleur.valeurs["nb_mailles_echantillon"] = nb_m
        controleur.valeurs["nb_rangs_echantillon"] = nb_r

        afficher_parametres_echantillon(label_echantillon, controleur)

    Button(
        root,
        text="Voir catalogue motifs",
        command=lambda: afficher_catalogue_motifs_tk(
            root,
            controleur.catalogue,
            retour_accueil=lambda: fenetre_accueil(root, controleur)
        )
    ).pack(pady=5)
    
    Button(root, text="Définir dimensions couverture", command=definir_couverture).pack(pady=5)
    Button(root, text="Définir paramètres échantillon", command=definir_echantillon).pack(pady=5)
    Button(root, text="Générer la couverture", command=generer_couverture).pack(pady=5)
    
    label_couverture = Label(root, text="")
    label_couverture.pack()

    label_echantillon = Label(root, text="")
    label_echantillon.pack()

    afficher_parametres_couverture(label_couverture, controleur)
    afficher_parametres_echantillon(label_echantillon, controleur)

