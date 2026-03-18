import os
import json

DATASET_DIR = os.path.expanduser("~/aicon/datasets")
REGISTRY_FILE = os.path.join(DATASET_DIR, "registry.json")

def ensure_registry():
	os.makedirs(DATASET_DIR, exist_ok=True)
	if not os.path.exists(REGISTRY_FILE):
		with open(REGISTRY_FILE, "w") as f:
			json.dump({}, f)

def register_dataset(name, path, version="v1"):
	ensure_registry()
	with open(REGISTRY_FILE, "r") as f:
		data = json.load(f)
	data[name] = {
		"path": path,
		"version": version
	}
	with open(REGISTRY_FILE, "w") as f:
		json.dump(data, f, indent=4)
	print(f"Dataset '{name}' registered")

def list_datasets():
	ensure_registry()
	with open(REGISTRY_FILE, "r") as f:
		data = json.load(f)
	return data.get(name)

def get_dataset(name):
	ensure_registry()
	with open(REGISTRY_FILE, "r") as f:
		data = json.load(f)
	return data.get(name)
