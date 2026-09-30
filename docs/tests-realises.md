# Tests realises

| Test | Commande | Resultat attendu |
| --- | --- | --- |
| Python | `python --version` | Version compatible affichee |
| Pip | `pip --version` | Pip disponible |
| PyTorch | `python scripts/check_cuda.py` | Version PyTorch affichee |
| CUDA | `python scripts/check_cuda.py` | GPU detecte si compatible |
| Calcul GPU | `python scripts/check_cuda.py` | Test matriciel execute sur CUDA si disponible |
| Transformers | `python scripts/check_transformers.py` | Import OK |
| JupyterLab | `jupyter lab` | Interface locale lancee |
| Docker | `docker run hello-world` | Message de validation Docker |
| Docker GPU | `docker run --rm --gpus all ... nvidia-smi` | GPU visible si compatible |
| Ollama | `ollama --version` | Version affichee si installe |

Les resultats locaux ne sont pas publies pour eviter toute information personnelle ou specifique a une machine.
