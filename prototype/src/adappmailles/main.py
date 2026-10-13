from tkinter import Tk 
from adappmailles.controleur.application import ApplicationControleur
from adappmailles.ui.accueil import fenetre_accueil

def main():
    root = Tk()
    
    app = ApplicationControleur()
    app.configurer()
  
    fenetre_accueil(root, app)
   
    root.mainloop()
    
if __name__ == "__main__":
    main()