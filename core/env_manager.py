import os
import subprocess

BASE_ENV_PATH = os.path.expanduser("~/aicon/envs")

def ensure_base():
	os.makedirs(BASE_ENV_PATH, exist_ok=True)

def create_env(name):
	ensure_base()
	path = os.path.join(BASE_ENV_PATH, name)
	if os.path.exists(path):
		print("Environment already exists")
		return
	subprocess.run(["python3", "-m", "venv", path])
	print(f"Envirnment '{name}' created")

def list_envs():
	ensure_base()
	envs = os.listdir(BASE_ENV_PATH)
	print("Available environments:")
	for env in envs:
		print(f"- {env}")

def install_package(env, package):
	path = os.path.join(BASE_ENV_PATH, env, "bin", "pip")
	if not os.path.exists(path):
		print("Environment not found.")
		return
	subprocess.run([path, "install", package])

def activate_help(env):
	path = os.path.join(BASE_ENV_PATH, env, "bin", "activate")
	if not os.path.exists(path):
		print("Environment not found")
		return
	print(f"Run this command: \nsource {path}")
