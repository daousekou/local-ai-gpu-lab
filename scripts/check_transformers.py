try:
    import transformers
except ImportError:
    print("Transformers is not installed.")
    raise SystemExit(1)


print(f"Transformers version: {transformers.__version__}")
print("Transformers import test: OK")
