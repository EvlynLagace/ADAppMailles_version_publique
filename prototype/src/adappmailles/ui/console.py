
class Console:

    @staticmethod
    def lire_dimensions_couverture(input_func=input):
        largeur_cm = int(input_func("Entrez la largeur de la couverture en cm : "))
        hauteur_cm = int(input_func("Entrez la hauteur de la couverture en cm : "))
        return(largeur_cm, hauteur_cm)

    @staticmethod
    def lire_dimensions_echantillon(input_func=input):
        largeur_cm = int(input_func("Entrez la largeur de l'échantillon en cm : "))
        hauteur_cm = int(input_func("Entrez la hauteur de l'échantillon en cm : "))
        nb_mailles = int(input_func("Entrez le nombre de mailles de l'échantillon : "))
        nb_rangs = int(input_func("Entrez le nombre de rangs de l'échantillon : "))
        return(largeur_cm, hauteur_cm, nb_mailles, nb_rangs)

    def afficher_patron_tuile(self):
        patron= self.generer_patron()
        for index_rang, rang in enumerate(patron):
            ligne = " ".join(str(maille) for maille in rang.construire_rang_complet(self.nb_mailles, self.nb_mailles_compensation))
            print(f"Rang {index_rang + 1} {rang.type_rang.name} : {ligne}")
        print()

    def afficher_couverture_console(couverture):
        print(f"Une couverture de {couverture.largeur_cm} cm de largeur et de {couverture.hauteur_cm} de hauteur")
        print(f"sera constituée de {len(couverture.tuiles)*len(couverture.tuiles[0])} tuiles")
        print()

        for i, ligne in enumerate(couverture.tuiles):
            for j, tuile in enumerate(ligne):
                print(f"Tuile à la position ({i+1}, {j+1}) aura le motif  {tuile.motif.nom_motif}")
                print(f"elle aura {tuile.nb_mailles} mailles sur {tuile.nb_rangs} rangs")
                print(f"Nb de mailles de compensation : {tuile.nb_mailles_compensation}")
                print()
                Console.afficher_patron_tuile(tuile)

    def afficher_echantillon(echantillon):
        print(f"Un échantillon de largeur {echantillon.largeur_cm} cm par {echantillon.hauteur_cm} cm a été instancié.")
        print(f"Il se tricote sur {echantillon.nb_mailles} mailles et sur {echantillon.nb_rangs} rangs.")
        print()

    def afficher_catalogue_console(catalogue):
        for motif in catalogue.motifs:
            print(f"{motif.nom_motif} : multiple de {motif.nb_mailles_repetees} plus {motif.nb_mailles_ajoutees}")

    @staticmethod
    def afficher_motifs_compatibles(motifs):
        print("Les motifs compatibles sont : ")
        for motif in motifs:
            print(f"{motif.nom_motif}")
