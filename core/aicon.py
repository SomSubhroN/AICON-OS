#!/usr/bin/env python3
import sys
from monitor import print_stats
from experiment import run_experiment, reproduce_experiment
from env_manager import create_env, list_envs, install_package, activate_help
from dataset import register_dataset, list_datasets
from exp_viewer import list_experiments, show_experiments

def main():
	if len(sys.argv) < 2:
		print("AICON OS CLI")
		return
	command = sys.argv[1]
	if command == "version":
		print("AICON OS v0.1")
	elif command == "status":
		print("System active")
	elif command == "monitor":
		print_stats()
	elif command == "run":
		if len(sys.argv) < 3:
			print("Usage: aicon run script.py [args]")
			return
		script = sys.argv[2]
		args = sys.argv[3:]
		run_experiment(script, args)
	elif command == "reproduce":
		if len(sys.argv) < 3:
			print("Usage: aicon reproduce exp_file.json")
			return
		filename = sys.argv[2]
		reproduce_experiment(filename)
	elif command == "env":
		if len(sys.argv) < 3:
			print("Usage: aicon env [create/list/install/activate]")
			return
		sub = sys.argv[2]
		if sub == "create":
			create_env(sys.argv[3])
		elif sub == "list":
			list_envs()
		elif sub == "install":
			install_package(sys.argv[3], sys.argv[4])
		elif sub == "activate":
			activate_help(sys.argv[3])
	elif command == "dataset":
		sub = sys.argv[2]
		if sub == "register":
			name = sys.argv[3]
			path = sys.argv[4]
			register_dataset(name, path)
		elif sub == "list":
			list_datasets()
	elif command == "exp":
		if len(sys.argv)<3:
			print("Usage: aicon exp [list/show]")
			return
		sub = sys.argv[2]
		if sub == "list":
			list_experiments()
		elif sub == "show":
			filename = sys.argv[3]
			show_experiment(filename)
	else:
		print("Unknown command")



if __name__ == "__main__":
	main()

