# Environnement IA local GPU

Projet de laboratoire pour installer, tester et documenter un environnement IA local avec Python, environnement virtuel, PyTorch avec CUDA, Transformers, JupyterLab, YOLO et Ollama.

Ce depot est volontairement generique. Il ne contient aucun secret, aucun chemin local personnel, aucun identifiant et aucune information liee a une entreprise.

## Objectifs

- Creer un environnement Python isole avec `venv`.
- Installer PyTorch avec support GPU CUDA lorsque le materiel est compatible.
- Tester l'acces GPU depuis Python.
- Utiliser JupyterLab pour les notebooks.
- Preparer une base pour Transformers, YOLO et Ollama.
- Documenter les commandes, les tests et les avertissements de securite.

## Architecture

```text
.
|-- README.md
|-- docs/
|   |-- commandes.md
|   |-- securite.md
|   `-- tests-realises.md
|-- notebooks/
|   `-- README.md
|-- scripts/
|   |-- check_cuda.py
|   `-- check_transformers.py
`-- requirements.txt
```

## Prerequis

- Windows 11 ou Linux.
- Python 3.10 ou plus recent.
- Pilote NVIDIA installe si un GPU NVIDIA est utilise.
- Connexion Internet pendant l'installation.

Les versions de PyTorch, CUDA, Transformers, YOLO et Ollama changent regulierement. Toujours verifier les documentations officielles avant une installation definitive.

- PyTorch : <https://pytorch.org/get-started/locally/>
- Transformers : <https://huggingface.co/docs/transformers/installation>
- Ultralytics YOLO : <https://docs.ultralytics.com/>
- Ollama : <https://ollama.com/download>

## Installation Python

```bash
python -m venv .venv
```

Activation Windows PowerShell :

```powershell
.\.venv\Scripts\Activate.ps1
```

Activation Linux / WSL :

```bash
source .venv/bin/activate
```

Mettre les outils Python a jour :

```bash
python -m pip install --upgrade pip setuptools wheel
```

Installer les dependances de base :

```bash
pip install -r requirements.txt
```

## Installation PyTorch GPU

La commande exacte depend de la version CUDA compatible avec la machine.

Exemple a verifier sur le site officiel PyTorch :

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

Si aucun GPU compatible n'est disponible, utiliser l'installation CPU indiquee par PyTorch.

## Tests rapides

Verifier Python :

```bash
python --version
pip --version
```

Verifier PyTorch et CUDA :

```bash
python scripts/check_cuda.py
```

Verifier Transformers :

```bash
python scripts/check_transformers.py
```

Lancer JupyterLab :

```bash
jupyter lab
```

## Securite

Ne jamais publier :

- tokens Hugging Face, OpenAI, GitHub ou autre service ;
- fichiers `.env` reels ;
- chemins locaux personnels ;
- notebooks contenant des cles API ;
- donnees privees d'entrainement ;
- modeles ou datasets soumis a licence non compatible.

Voir [docs/securite.md](docs/securite.md).

## Licence

Ce projet est fourni comme support d'apprentissage. Ajouter une licence explicite avant reutilisation publique dans un contexte professionnel.
