# AdappMailles - Prototype

L'application génèrera le patron d'une couverture tricotée. Les instructions seront présentées en format texte et en format grille de tricot. L'ouvrage sera composé de tuiles auxquelles un motif aura été assigné, et ce sans que deux tuiles soient identiques.

L'interface de ce prototype sera développée en tKinter, permettant de valider les algolrithmes utilisés, le modèle et la logique métier de génération de la couverture et des tuiles.

## Fonctionnalités

<img width="847" height="911" alt="image" src="https://github.com/user-attachments/assets/d75ae643-5aca-4f24-941d-9aedc1aa42bb" />

## Installation et lancement

```bash
cd prototype
uv run src/adappamailles/main.py
```
## Structure
```
src/
└── adappmailles/
    ├── assets/
    │   └── images/
    ├── controleur/
    │   └── application.py
    ├── data/
    │   └── catalogue.json
    ├── modele/
    │   ├── motif.py
    │   ├── rang.py
    │   ├── rang_instructions.py
    │   ├── couverture.py
    │   └── tuile.py
    ├── services/
    │   ├── conversion_motif.py
    │   ├── generateur_patron.py
    │   └── generateur_tuile.py
    ├── tests/
    ├── ui/
    │   ├── accueil.py
    │   ├── couverture_tk.py
    │   └── afficher_motif_detail_tk.py
    └── main.py
```

## Contexte

Projet de fin d'études dans le cadre du programme de Majeure en informatique à la TÉLUQ
