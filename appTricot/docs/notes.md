## Conventions pour les noms des branches de Git

fonctionnalite : nouvelle fonctionnalité ou évolution
correction
amelioration : par exemple affichage des numeros de rangs envers
refactorisation
essai
documentation
tests

## Points à auditer

### Sauvegarde / chargement JSON
- [ ] Vérifier la gestion des JSON invalides
- [ ] Vérifier les fichiers absents ou corrompus
- [ ] Vérifier la validation des données reçues

### Génération PDF
- [ ] Vérifier les exceptions de génération
- [ ] Vérifier les ressources manquantes (CSS, images, polices)
- [ ] Vérifier le comportement si un motif n'existe pas

### Views.py
- [x] Classer les imports
- [ ] Page 404
- [ ] raise Http404 partout plutôt que parfois HttpresponseNotFound

## WeasyPrint

- [ ] Vérifier l'ordre d'initialisation DLL Windows
- [ ] Réfléchir à déplacer la configuration WeasyPrint hors de views.py