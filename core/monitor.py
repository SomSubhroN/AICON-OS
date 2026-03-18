import psutil
import os

def get_stats():
	cpu=psutil.cpu_percent()
	mem=psutil.virtual_memory().percent
	temp=os.popen("vcgencmd measure_temp").readline().strip()
	return {
		"cpu": cpu,
		"memory": mem,
		"temp": temp
	}

def print_stats():
	stats = get_stats()
	print("AICON SYSTEM STATUS")
	print("-------------------")
	print(f"CPU: {stats['cpu']}%")
	print(f"RAM: {stats['memory']}%")
	print(f"{stats['temp']}")
