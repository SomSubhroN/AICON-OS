#!/usr/bin/env python3
import sys
def main():
	if len(sys.argv) < 2:
		print("AICON OS CLI")
		return
	command = sys.argv[1]
	if command == "version":
		print("AICON OS v0.1")
	elif command == "status":
		print("System active")
	else:
		print("Unknown command")
if __name__ == "__main__":
	main()
