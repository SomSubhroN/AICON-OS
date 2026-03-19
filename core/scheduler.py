import os
import json
import time
import psutil
from experiment import run_experiment

JOB_DIR = os.path.expanduser("~/aicon/jobs")

def ensure_jobs():
	os.makedirs(JOB_DIR, exist_ok=True)

def create_job(script, args):
	ensure_jobs()
	job = {
		"script": script,
		"args": args,
		"status": "pending"
		}
	filename = f"job_{int(time.time())}.json"
	path = os.path.join(JOB_DIR, filename)
	with open(path, "w") as f:
		json.dump(job, f, indent=4)
	print(f"Job submitted: {filename}")

def get_next_job():
	ensure_jobs()
	for file in sorted(os.listdir(JOB_DIR)):
		path = os.path.join(JOB_DIR, file,)
		with open(path, "r") as f:
			job = json.load(f)
		if job.get("status") == "running":
			print(f"Fixing stuck job: {file}")
			job["status"] = "pending"
			with open(path, "w") as fw:
				json.dump(job, fw, indent=4)
		if job["status"] == "pending":
			return file, job
	return None, None

def update_job(filename, job):
	path = os.path.join(JOB_DIR, filename)
	with open(path, "w") as f:
		json.dump(job, f, indent=4)

def scheduler_loop():
	print("AICON Scheduler Started...")
	try:
		while True:
			cpu = psutil.cpu_percent(interval=1)
			if cpu < 40:
				filename, job = get_next_job()
				if job and job["status"] != "pending":
					continue
				if job:
					print(f"Running job: {filename}")
					job["status"] = "running"
					update_job(filename, job)
					try:
						run_experiment(job["script"], job["args"])
						job["status"] = "done"
					except Exception as e:
						print("Job failed: ", e)
						job["status"] = "failed"
					update_job(filename, job)
				else:
					print("No Pending jobs")
			else:
				print(f"CPU busy: {CPU}%")
			time.sleep(5)
	except KeyboardInterrupt:
		print("\nScheduler stopped safely.")

def list_jobs():
	ensure_jobs()
	for file in sorted(os.listdir(JOB_DIR)):
		path = os.path.join(JOB_DIR, file)
		with open(path, "r") as f:
			job = json.load(f)
		print(f"{file} -> {job['status']}")
