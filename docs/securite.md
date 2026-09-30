# Securite

Ce depot ne doit pas contenir de donnees sensibles.

## Ne pas publier

- tokens API ;
- fichiers `.env` reels ;
- cles SSH ;
- notebooks avec secrets ;
- chemins locaux personnels ;
- donnees privees d'entrainement ;
- datasets soumis a restriction ;
- sorties contenant informations personnelles.

## Bonnes pratiques

- Utiliser `.env.example` au lieu de `.env`.
- Garder les datasets hors du depot.
- Documenter les sources des modeles et datasets.
- Verifier les licences avant publication.
- Nettoyer les notebooks avant commit.
