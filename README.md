# Correction TP Github Actions

## Question 3

Vous pouvez tester votre code avec la commande suivant

```bash
python3 -m unittest math.py
```

## Question 4

L'ajout d'un fichier yaml dans le répertoire .github/workflows permet de définir des actions dans le menu Actions de votre repository sur Github

## Question 6

Il faut ajouter une nouvelle step dans le fichier .yaml

```bash
python3 -m pip install pylint # Permet d'installer l'outil de lint pylint
pylint --exit-zero math.py # Vérifie le code du fichier math.py. L'option --exit-zero permet de continuer la CI de l'application en renvoyant un code de retour 0
```