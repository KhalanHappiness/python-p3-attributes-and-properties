#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    
    def __init__(self, name ="Penninah", job ="Sales"):
        self.name = None
        self.job = None
        self.set_name(name)
        self.set_job(job)

    def set_name(self, value):
        if isinstance(value, str) and 1<= len(value) <= 25 :
            self.name = value.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    def set_job(self, value):
        
        if value in APPROVED_JOBS:
            self.job = value
        else:
            print("Job must be in list of approved jobs.")
        


    
        
