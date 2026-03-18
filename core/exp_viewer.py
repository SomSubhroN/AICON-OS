import os
import json

EXP_DIR	 = os.path.expanduser("~/aicon/experiments")

def list_experiments():
	if not os.path.exists(EXP_DIR):
		print("No experiments found")
		return
	files = sorted(os.listdir(EXP_DIR))
	print("Experiments:")
	for f in files:
		if f.endswith(".json"):
			print(f"- {f}")
def show_experiments(filename):
	filepath = os.path.join(EXP_DIR, filename)
	if not os.path.exists(filepath):
		print("Experiment not found")
		return

	with open(filepath, "r") as f:
		exp = json.load(f)

	print("\n=== Experiment Details ===")
	print(f"Script: {exp.get('script')}")
	print(f"Env: {exp.get('env')}")
	print(f"Dataset: {exp.get('dataset')}")
	print(f"Params: {exp.get('parameters')}")
	print(f"Runtime: {exp.get('runtime_seconds')} sec")
	print(f"Status: {exp.get('status')}")

	print("\n --- System ---")
	sysinfo = exp.get("system", {})
	print(f"CPU: {sysinfo.get('cpu_usage')}%")
	print(f"Memory: {sysinfo.get('memory_usage')}%")
	print("\n--- Packages ---")
	pkgs = exp.get("env_packages", [])
	for p in pkgs[:10]:
		print(p)
	if len(pkgs)>10:
		print("... (more)")
