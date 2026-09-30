# Commandes reproductibles

## Creer l'environnement

```bash
python -m venv .venv
```

## Activer l'environnement

Windows PowerShell :

```powershell
.\.venv\Scripts\Activate.ps1
```

Linux / WSL :

```bash
source .venv/bin/activate
```

## Installer les dependances

```bash
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

## Installer PyTorch GPU

Verifier la commande officielle sur :

```text
https://pytorch.org/get-started/locally/
```

Exemple :

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

## Tester

```bash
python scripts/check_cuda.py
python scripts/check_transformers.py
jupyter lab
```

## Tester Docker

```bash
docker run hello-world
docker run --rm --gpus all nvidia/cuda:12.8.1-base-ubuntu24.04 nvidia-smi
```

## Tester un pipeline Transformers

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis", device=0)
print(classifier("ROS 2 and robotics are fascinating."))
```

## Ollama

Apres installation officielle d'Ollama :

```bash
ollama --version
ollama pull qwen3:4b
ollama run qwen3:4b
```
