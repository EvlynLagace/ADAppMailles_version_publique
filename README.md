# ADAppMailles

ADAppMailles génère les instructions permettant de confectionner une couverture « patchwork » en utilisant différents motifs de tricot.

Son nom est inspiré par Ada Lovelace, pionnière de l'informatique.

Ce projet a débuté par un prototype afin d'explorer et de valider la modélisation du domaine.

Le prototype est conservé dans le répertoire prototype/ du présent dépôt.

## Documentation

- [Tutoriel](appTricot/docs/guide/tutoriel.md)
  
## Installation et lancement de l'application

L'application utilise uv pour gérer son environnement et ses dépendances.

À partir du dossier racine du projet:
```
uv venv

uv sync

uv run manage.py migrate

uv run manage.py runserver
```
### Accès

Une fois l'application lancée, elle est accessible à l'adresse suivante :

```
http://127.0.0.1:8000/appTricot

```
## Technologies

- Python 3.14 / Django 6
- JavaScript / React 18
- HTML / CSS
- SQLite
- uv

## Déploiement

L'application est accessible en ligne :
- [ADAppMailles](https://adappmailles.ca)
  
## Contexte
Projet de fin d'études, supervisé par M. Christian Jauvin, dans le cadre du programme de Majeure en informatique à la TÉLUQ.

## License

Licence MIT

Copyright (c) 2026 Evlyn Lagacé

L’autorisation est accordée, gratuitement, à toute personne obtenant une copie de cette application et des fichiers de documentation associés (l’« Application »), de traiter l’Application sans restriction, notamment les droits de l’utiliser, de la copier, de la modifier, de la fusionner, de la publier, de la distribuer, de la sous-licencier et/ou d’en vendre des copies, ainsi que d’autoriser les personnes auxquelles l’Application est fournie à faire de même, sous réserve des conditions suivantes :

La présente mention de droit d’auteur et la présente autorisation doivent être incluses dans toutes les copies ou parties substantielles de l’Application.

L’APPLICATION EST FOURNIE « TELLE QUELLE », SANS AUCUNE GARANTIE, EXPRESSE OU IMPLICITE, NOTAMMENT SANS GARANTIE DE QUALITÉ MARCHANDE, D’ADÉQUATION À UN USAGE PARTICULIER OU D’ABSENCE DE CONTREFAÇON. EN AUCUN CAS LES AUTEURS OU LES TITULAIRES DU DROIT D’AUTEUR NE POURRONT ÊTRE TENUS RESPONSABLES DE TOUTE RÉCLAMATION, DE TOUT DOMMAGE OU DE TOUTE AUTRE RESPONSABILITÉ, QUE CE SOIT DANS LE CADRE D’UNE ACTION CONTRACTUELLE, DÉLICTUELLE OU AUTRE, DÉCOULANT DE L’APPLICATION, DE SON UTILISATION OU DE TOUTE AUTRE OPÉRATION LIÉE À L’APPLICATION.

Traduction libre en français de la licence MIT. En cas de divergence, le texte original anglais fait foi.