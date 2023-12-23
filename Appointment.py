#AppointmentManagementSystem.py
#JoshuaY
#Dec 8 2023
"""
Store 
i. Date of appointment
ii. Time of appointment (start time and end time)
iii. Purpose of appointment
valus."""
class Appointment:
    def __init__(self,date,st,et,purpose):
        self.date = date
        self.st = st
        self.et = et
        self.purpose = purpose

    def toList(self):
        return [self.date,self.st,self.et,self.purpose]
