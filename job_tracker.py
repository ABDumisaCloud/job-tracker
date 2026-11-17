import json
import os
FILENAME = "jobs.json"

def load_jobs():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r")as f:
        return json.load(f)
    
def save_jobs(jobs):
    with open(FILENAME, "w") as f:
        json.dump(jobs, f, indent=2)

def add_job():
        jobs = load_jobs()
        company = input("Company: ")
        role = input("Role: ")
        status = input("Status: ")
        jobs.append({"company":company, "role": role,"status": status})
        save_jobs(jobs)
        print("Job saved!")

def view_jobs():
     jobs = load_jobs()
     for job in jobs:
          print(f"{job['company']}-{job['role']}-{job['status']}")
def update_job():
     jobs = load_jobs()
     for i, job in enumerate(jobs):
          print(f"{i+1}.{job['company']}-{job['role']}-{job['status']}")
     choice = int(input("Enter job number to update: "))
     jobs[choice-1]['status']=input("Enter new status: ")

     save_jobs(jobs)
def delete_job():
    jobs = load_jobs()
    for i, job in enumerate(jobs):
     print(f"{i+1}.{job['company']}-{job['role']}-{job['status']}")
     choice = int(input("Enter job number to delete: "))
    del jobs[choice-1]
    save_jobs(jobs)
    print("Job deleted!")

while True:
     print("\n1. Add job")
     print("2. view jobs")
     print("3.update job")
     print("4. Delete job")
     print("5. Exit")
     choice = input("Choose: ")
     if choice == "1":
          add_job()
     elif choice == "2":
       view_jobs()
     elif choice == "3":
          update_job()
     elif choice=="4":
         delete_job()  
     elif choice=="5":
          break
     
          _