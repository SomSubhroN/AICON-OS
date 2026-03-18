import subprocess
import sys
import time
import json
import os
import psutil
import datetime

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
	start_time = time.time()
	process = subprocess.run(["python3", script] + args)
	end_time = time.time()
	exp = {
		"script": script,
		"parameters": args,
		"start_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
		"runtime_seconds": round(end_time - start_time, 2),
		"status": "success" if process.returncode == 0 else "failed",
		"system": get_system_info()
	}

	filename = f"exp_{int(time.time())}.json"
	filepath = os.path.join(EXP_DIR, filename)
	with open(filepath, "w") as f:
		json.dump(exp, f, indent=4)
	print(f"\nExperiment logged: {filename}")

def reproduce_experiment(filename):
	filepath = os.path.join(EXP_DIR, filename)
	if not os.path.exists(filepath):
		print("Experiment not found")
		return
	with open(filepath, "r") as f:
		exp = json.load(f)
	script = exp["script"]
	args = exp["parameters"]
	print("\nReproducing experiment...")
	print(f"Script: {script}")
	print(f"Parameters: {args}\n")
	run_experiment(script, args)
