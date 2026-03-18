import subprocess
import sys
import time
import json
import os
import psutil
import datetime
from dataset import get_dataset

EXP_DIR = os.path.expanduser("~/aicon/experiments")

def ensure_dir():
	os.makedirs(EXP_DIR, exist_ok=True)

def get_system_info():
	return {
		"cpu_usage": psutil.cpu_percent(),
		"memory_usage": psutil.virtual_memory().percent
	}

def run_experiment(script, args):
	ensure_dir()
	dataset_name = None
	if "--dataset" in args:
		idx = args.index("--dataset")
		dataset_name = args[idx+1]
	env_name = None
	if "--env" in args:
		idx = args.index("--env")
		env_name = args[idx+1]
		args = args[:idx] + args[idx+2:]
	start_time = time.time()
	if env_name:
		python_path = os.path.expanduser(f"~/aicon/envs/{env_name}/bin/python")
	else:
		python_path = "python3"
	process = subprocess.run([python_path, script]+args)
	end_time = time.time()
	exp = {
		"script": script,
		"parameters": args,
		"env": env_name if env_name else "system",
		"runtime_seconds": round(end_time-start_time, 2),
		"status": "success" if process.returncode == 0 else "failed",
		"system": get_system_info(),
		"env_packages": get_env_packages(env_name)
	}
	filename = f"exp_{int(time.time())}.json"
	filepath = os.path.join(EXP_DIR, filename)

	with open(filepath, "w") as f:
		json.dump(exp, f, indent=4)
	print(f"\n Experiment logged: {filename}")

def reproduce_experiment(filename):
	filepath = os.path.join(EXP_DIR, filename)
	packages = exp.get("env_packages", [])
	env = exp.get("env")
	if env and env!= "system":
		restore_environment(env, packages)
	if not os.path.exists(filepath):
		print("Experiment not found")
		return
	with open(filepath, "r") as f:
		exp = json.load(f)
	script = exp["script"]
	args = exp["parameters"]
	env = exp.get("env")
	print("\nReproducing experiment...")
	print(f"Script: {script}")
	print(f"Parameters: {args}\n")
	if env and env != "system":
		python_path = os.path.expanduser(f"~/aicon/envs/{env}/bin/python")
	else:
		python_path = "python3"
	subprocess.run([python_path, script] + args)
	dataset_name = exp.get("dataset")
	if dataset_name:
		dataset_info = get_dataset(dataset_name)
		if not dataset_info:
			print(f"Dataset: '{dataset_name}' ({dataset_info['path']})")

def get_env_packages(env_name):
	if not env_name or env_name == "system":
		return
	pip_path = os.path.expanduser(f"~/aicon/envs/{env_name}/bin/pip")
	if not os.path.exists(pip_path):
		return []
	result = subprocess.run([pip_path, "freeze"], capture_output=True, text=True)
	return result.stdout.splitlines()

def restore_environment(env_name, packages):
	env_path = os.path.expanduser(f"~/aicon/envs/{env_name}")
	if not os.path.exists(env_path):
		print(f"Creating environment: {env_name}")
		subprocess.run(["python3", "-m", "venv", env_path])
	pip_path = os.path.join(env_path, "bin", "pip")
	print("Installing packages...")
	for pkg in packages:
		subprocess.run([pip_path, "install", pkg])
