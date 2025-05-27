
# Parking Électrique

Application Python de gestion d'un parking de voitures électriques avec interface graphique Tkinter.

## Fonctionnalités

- Affichage graphique du parking et des voitures selon leur état de charge
- Visualisation des places, pourcentages de batterie et temps de charge restant
- Interface de messagerie simple
- Gestion dynamique des voitures

## Prérequis

- Python 3.13 (ou version compatible avec Tkinter et Pillow)
- [Git](https://git-scm.com/) pour cloner le dépôt

## Installation

1. **Cloner le dépôt :**

   ```bash
   git clone https://github.com/votre-utilisateur/p2i-noah.git
   cd p2i-noah
   ```

2. **Créer un environnement virtuel (recommandé) :**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate     # Windows
   ```

3. **Installer les dépendances :**

   ```bash
   pip install -r requirements.txt
   ```

## Lancement de l'application

```bash
python main.py
```

L'application s'ouvre dans une fenêtre graphique. Entrez votre nom et prénom pour commencer.

## Structure du projet

```
p2i-noah/
│
├── assets/                # Images utilisées par l'application
│   ├── background.png
│   ├── blue_car.png
│   ├── green_car.png
│   ├── red_car.png
│   └── yellow_car.png
│
├── Car.py                 # Classe représentant une voiture
├── ImagePath.py           # Chemins des images
├── main.py                # Point d'entrée principal
├── requirements.txt       # Dépendances Python
├── utils.py               # Fonctions utilitaires
├── Window.py              # Interface graphique principale
└── README.md
```

## Dépendances principales

- [Tkinter](https://docs.python.org/3/library/tkinter.html) (inclus avec Python)
- [Pillow](https://python-pillow.org/) pour la gestion des images

## Remarques

- Les images doivent être présentes dans le dossier `assets/` à la racine du projet.
- Si vous rencontrez des problèmes d'affichage, vérifiez que toutes les dépendances sont bien installées et que vous utilisez la bonne version de Python.

## Auteurs

- Projet développé par [Lorem Ipsum]
