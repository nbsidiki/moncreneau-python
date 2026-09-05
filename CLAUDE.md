# Contexte — moncreneau-python

SDK client officiel Python pour l'API MonCréneau (package `moncreneau`, publié sur PyPI).

## Contenu

Client basé sur clé API (`mk_live_...`), type hints complets, gestion d'erreurs (`MoncreneauError`), vérification de signature webhook. Exemples Flask et Django fournis dans le README. Ressources : `appointments`, `departments`.

## Publication

```bash
cd moncreneau-python
# Update setup.py version to X.Y.Z
python setup.py sdist bdist_wheel
twine upload dist/*
```

Versions déjà publiées trouvées dans `dist/` : jusqu'à 2.1.0.

## Documentation complète

https://moncreneau-docs.vercel.app/docs/v1/sdks/python (voir aussi `moncreneau-docs/`)

## À maintenir en synchro avec

L'API publique exposée par `rdv/` (backend).
