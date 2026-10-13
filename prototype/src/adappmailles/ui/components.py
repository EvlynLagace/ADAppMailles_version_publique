def afficher_parametres_couverture(label, controleur):
    largeur = controleur.valeurs.get("largeur_couverture")
    hauteur = controleur.valeurs.get("hauteur_couverture")

    if largeur and hauteur :
        txt_parametres_couverture = f"Couverture : {largeur} x {hauteur} cm"
    else :
        txt_parametres_couverture = "Couverture non définie"

    label.config(text=txt_parametres_couverture)

def afficher_parametres_echantillon(label, controleur):
    largeur_echantillon = controleur.valeurs.get("largeur_echantillon")
    hauteur_echantillon = controleur.valeurs.get("hauteur_echantillon")
    mailles_echantillon = controleur.valeurs.get("nb_mailles_echantillon")
    rangs_echantillon = controleur.valeurs.get("nb_rangs_echantillon")

    txt_parametres_echantillon = f"Echantillon :{largeur_echantillon} x {hauteur_echantillon} cm sur {mailles_echantillon} mailles et {rangs_echantillon} rangs"

    label.config(text = txt_parametres_echantillon)