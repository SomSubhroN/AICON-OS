import os
import json

EXP_DIR = os.path.expanduser("~/aicon/experiments")

def load_exp(filename):
	path = os.path.join(EXP_DIR, filename)
	if not os.path.exists(path):
		print(f"{filename} not found")
		return None
	try:
		with open(path, "r") as f:
			return json.load(f)
	except Exception as e:
		print(f"Error loading {filename}: {e}")
		return None

def compare_values(key, v1, v2):
	if v1 != v2:
		print(f"{key}: {v1} -> {v2}")

def compare_experiments(f1, f2):
	exp1 = load_exp(f1)
	exp2 = load_exp(f2)
	if not exp1 or not exp2:
		return
	print("\n=== AICON EXPERIMENT COMPARISON ===\n")
	print("SCRIPT")
	compare_values("script", exp1.get("script"), exp2.get("script"))
	print("\n ENVIRONMENT")
	compare_values("env", exp1.get("env"), exp2.get("env"))
	print("\n DATASET")
	compare_values("dataset", exp1.get("dataset"), exp2.get("dataset"))
	print("\n PARAMETERS")
	p1 = set(exp1.get("parameters", []))
	p2 = set(exp2.get("parameters", []))
	print("Only in exp1:", list(p1-p2))
	print("Only in exp2:", list(p2-p1))
	print("\n RUNTIME")
	compare_values("runtime_seconds", exp1.get("runtime_seconds"), exp2.get("runtime_seconds"))
	print("\n STATUS")
	compare_values("status", exp1.get("status"), exp2.get("status"))
	print("\n DEPENDENCIES")
	d1 = set(exp1.get("env_packages", []))
	d2 = set(exp2.get("env_packages", []))
	print("Removed: ", list(d1-d2)[:10])
	print("Added: ", list(d2-d1)[:10])
