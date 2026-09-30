try:
    import torch
except ImportError:
    print("PyTorch is not installed.")
    raise SystemExit(1)


print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")

if torch.cuda.is_available():
    print(f"CUDA version: {torch.version.cuda}")
    print(f"GPU count: {torch.cuda.device_count()}")
    print(f"GPU name: {torch.cuda.get_device_name(0)}")
    device = torch.device("cuda:0")
    sample = torch.randn((1024, 1024), device=device)
    result = sample @ sample
    torch.cuda.synchronize()
    print(f"Matrix test device: {result.device}")
else:
    print("No CUDA GPU detected by PyTorch.")
