#!/usr/bin/env python3
import sys
from monitor import print_stats
from experiment import run_experiment, reproduce_experiment


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
	else:
		print("Unknown command")




if __name__ == "__main__":
	main()
