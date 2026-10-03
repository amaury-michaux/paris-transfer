# Paris Transfer

Projet de conduite simulée en 2D, construit progressivement en Python. L'objectif est d'étudier la généralisation d'un conducteur neuronal à des routes inconnues et sa récupération après une déviation, avec un réseau implémenté en NumPy.

## État actuel

Ce premier prototype Pygame affiche une route droite, une ligne centrale discontinue et une voiture représentée par un rectangle. La voiture est encore immobile : la dynamique, les capteurs et le conducteur neuronal ne sont pas encore implémentés. Aucun résultat d'apprentissage ou de généralisation n'est disponible à ce stade.

## Installation et lancement

L'environnement de développement actuel utilise Python 3.14.6. Depuis la racine du dépôt :

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m scripts.demo
```

Le lancement interactif nécessite un environnement graphique.

## Commandes

- `R` : réinitialiser la position de la voiture.
- `Échap` ou fermeture de la fenêtre : quitter.

## Vérification du prototype

Un contrôle sans fenêtre, avec les pilotes SDL `dummy`, a exécuté le dessin d'une image, la touche de réinitialisation, la sortie par `Échap` et la fermeture de Pygame. La cohérence des dépendances installées a également été vérifiée avec `python -m pip check`. Ce contrôle ne valide pas l'apparence de la fenêtre sur un écran réel.

## Prochaine étape

Ajouter le déplacement du véhicule avec des unités explicites et un pas de simulation fixe, puis vérifier son mouvement rectiligne. Le rendu devra lire l'état de la simulation afin que les futures évaluations puissent fonctionner sans fenêtre.
