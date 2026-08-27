# velos-api

API de suivi des stations de velos en libre-service.

## Routes

- `/sante` : etat de sante de l'application
- `/stations` : liste des stations avec quartier et velos disponibles
- `/disponibilite` : taux d'occupation moyen du parc
- `/alertes` : stations avec 1 velo disponible ou moins (seuil strict, a venir)

## Variables d'environnement

- `DATABASE_URL` : si definie, l'API lit PostgreSQL. Sinon, jeu de donnees en memoire.
- `PORT` : port d'ecoute (defaut 8000).
