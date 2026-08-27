# Ressources fournies

> Ces fichiers sont le **point de départ** du projet. Tu les copies dans ton dossier de travail `velos-api`, puis tu les versionnes. Tu n'as pas à réécrire ce code : ce n'est pas ce qui est évalué.

| Fichier | Rôle |
| --- | --- |
| `app.py` | L'application. Trois routes fournies, une quatrième à ajouter par tes soins au jalon 3 |
| `requirements.txt` | Les deux dépendances de l'application |
| `db/init.sql` | Le jeu de données initial : huit stations, quatre quartiers |

## Ce qu'il faut avoir lu dans `app.py` avant de commencer

1. **La source des données dépend d'une variable d'environnement.** Sans configuration, l'application répond avec un jeu de secours et l'annonce dans le champ `source`. C'est ce champ qui te dira, à chaque étape du projet, si tu parles vraiment à la base.
2. **L'application écoute sur toutes les interfaces.** Tu sais depuis le Jour 2 pourquoi ce détail décide du succès ou de l'échec d'une publication de port.
3. **La route de santé ne sert pas aux humains.** Elle servira à la pile de conteneurs, puis au cluster, puis au pipeline.
4. **Le bloc de commentaire vers la fin du fichier** t'indique où ajouter ta route `/alertes`. Le seuil d'alerte est de deux vélos disponibles ou moins.

## Ce qui n'est pas fourni, et qui est à toi

Le fichier d'exclusion Git, la recette de construction de l'image, le fichier d'exclusion de construction, le fichier de composition de la pile, les manifestes du cluster, les tests et la description du pipeline. Autrement dit : **tout ce qui a été appris pendant trois jours**.
