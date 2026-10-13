from tkinter import Button, Entry, Label, Toplevel, messagebox


def lire_dimensions_tk(root) -> tuple[int, int]:
    """Affiche une fenêtre pour saisir les dimensions de la couverture.
    
    Returns:
        tuple[int, int]: (largeur_cm, hauteur_cm) ou (None, None) si annulée
    """
    resultat = {"largeur_cm": 200, "hauteur_cm": 60}

    def valider_couverture():
        """Valide les entrées et ferme la fenêtre."""
        try:
            largeur = int(saisie_largeur.get())
            hauteur = int(saisie_hauteur.get())
            
            if largeur <= 0 or hauteur <= 0:
                messagebox.showerror(
                    "Erreur",
                    "Les dimensions doivent être positives."
                )
                return
            
            resultat["largeur_cm"] = largeur
            resultat["hauteur_cm"] = hauteur
            fenetre.destroy()
        except ValueError:
            messagebox.showerror(
                "Erreur",
                "Veuillez entrer des nombres entiers valides."
            )

    fenetre = Toplevel()
    fenetre.title("Dimensions de la couverture")

    Label(fenetre, text="Largeur en cm : ").grid(row=0, column=0, padx=5, pady=5)
    Label(fenetre, text="Hauteur en cm : ").grid(row=1, column=0, padx=5, pady=5)

    saisie_largeur = Entry(fenetre)
    saisie_hauteur = Entry(fenetre)
    saisie_largeur.grid(row=0, column=1, padx=5, pady=5)
    saisie_hauteur.grid(row=1, column=1, padx=5, pady=5)
    saisie_largeur.insert(0, "200")
    saisie_hauteur.insert(0, "60")

    Button(fenetre, text="Valider", command=valider_couverture).grid(
        row=2, column=0, columnspan=2, pady=10
    )

    fenetre.wait_window()
    return resultat.get("largeur_cm"), resultat.get("hauteur_cm")

def lire_parametres_echantillon_tk(root) -> tuple[int, int, int, int]:
    """Affiche une fenêtre pour saisir les paramètres de l'échantillon.
    
    Returns:
        tuple[int, int, int, int]: (largeur_cm, hauteur_cm, nb_mailles, nb_rangs)
    """
    resultat = {"largeur_cm":10, "hauteur_cm":10, "nb_mailles":10,"nb_rangs":10}

    def valider_echantillon():
        """Valide les entrées et ferme la fenêtre."""
        try:
            largeur = int(saisie_largeur.get())
            hauteur = int(saisie_hauteur.get())
            mailles = int(saisie_mailles.get())
            rangs = int(saisie_rangs.get())

            if largeur <= 0 or hauteur <= 0 or mailles <= 0 or rangs <= 0:
                messagebox.showerror(
                    "Erreur",
                    "Tous les paramètres doivent être positifs."
                )
                return

            resultat["largeur_cm"] = largeur
            resultat["hauteur_cm"] = hauteur
            resultat["nb_mailles"] = mailles
            resultat["nb_rangs"] = rangs
            fenetre.destroy()
        except ValueError:
            messagebox.showerror(
                "Erreur",
                "Veuillez entrer des nombres entiers valides."
            )

    fenetre = Toplevel()
    fenetre.title("Paramètres de l'échantillon")

    Label(fenetre, text="Largeur en cm : ").grid(row=0, column=0, padx=5, pady=5)
    Label(fenetre, text="Hauteur en cm : ").grid(row=1, column=0, padx=5, pady=5)
    Label(fenetre, text="Nombre de mailles : ").grid(row=2, column=0, padx=5, pady=5)
    Label(fenetre, text="Nombre de rangs : ").grid(row=3, column=0, padx=5, pady=5)

    saisie_largeur = Entry(fenetre)
    saisie_hauteur = Entry(fenetre)
    saisie_mailles = Entry(fenetre)
    saisie_rangs = Entry(fenetre)
    saisie_largeur.grid(row=0, column=1, padx=5, pady=5)
    saisie_hauteur.grid(row=1, column=1, padx=5, pady=5)
    saisie_mailles.grid(row=2, column=1, padx=5, pady=5)
    saisie_rangs.grid(row=3, column=1, padx=5, pady=5)
    saisie_largeur.insert(0, "10")
    saisie_hauteur.insert(0, "10")
    saisie_mailles.insert(0, "10")
    saisie_rangs.insert(0, "10")

    Button(fenetre, text="Valider", command=valider_echantillon).grid(row=4, column=0, columnspan=2, pady=10)

    fenetre.wait_window()
    return resultat.get("largeur_cm"), resultat.get("hauteur_cm"), resultat.get("nb_mailles"), resultat.get("nb_rangs")