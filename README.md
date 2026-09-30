# Environnement IA local GPU

Projet de laboratoire pour installer, tester et documenter un environnement IA local avec Python, environnement virtuel, PyTorch avec CUDA, Transformers, JupyterLab, YOLO et Ollama.

Ce depot est volontairement generique. Il ne contient aucun secret, aucun chemin local personnel, aucun identifiant et aucune information liee a une entreprise.

## Objectifs

- Creer un environnement Python isole avec `venv`.
- Installer PyTorch avec support GPU CUDA lorsque le materiel est compatible.
- Tester l'acces GPU depuis Python.
- Verifier Docker avec un conteneur de test et un conteneur CUDA.
- Utiliser JupyterLab pour les notebooks.
- Preparer une base pour Transformers, Datasets, Accelerate, YOLO, OpenCV, PEFT, TRL, bitsandbytes et Ollama.
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

## Verification Docker et GPU

Verifier Docker :

```bash
docker run hello-world
```

Tester un conteneur CUDA NVIDIA :

```bash
docker run --rm --gpus all nvidia/cuda:12.8.1-base-ubuntu24.04 nvidia-smi
```

Si la commande affiche le GPU, Docker peut lancer des conteneurs capables d'utiliser l'acceleration materielle.

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

## Hugging Face

Les bibliotheques principales sont :

- `transformers` pour charger et utiliser des modeles pre-entraines ;
- `datasets` pour manipuler les jeux de donnees ;
- `accelerate` pour simplifier l'execution CPU/GPU ;
- `safetensors` pour charger des poids de modeles dans un format plus sur ;
- `sentencepiece` pour certains tokenizers.

Exemple de test :

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis", device=0)
print(classifier("ROS 2 and robotics are fascinating."))
```

## Fine-tuning

Le depot prepare aussi une base pour etudier :

- LoRA / QLoRA avec `peft` ;
- entrainement et adaptation de modeles avec `trl` ;
- quantification 8 bits ou 4 bits avec `bitsandbytes`.

Ces approches permettent de reduire les besoins memoire lors d'experiences sur des GPU limites.

## Vision par ordinateur

OpenCV et Ultralytics permettent de preparer des projets de vision :

```python
import cv2
from ultralytics import YOLO
```

YOLO peut ensuite servir a la detection d'objets, la segmentation, la classification ou le suivi.

## Ollama

Ollama permet d'executer localement des modeles de langage quantifies.

Exemple generique :

```bash
ollama pull qwen3:4b
ollama run qwen3:4b
```

Selon le GPU disponible, une partie ou la totalite du modele peut etre chargee en memoire video.

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
