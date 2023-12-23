#AppointmentManagementSystem.py
#JoshuaY
#Dec 8 2023
""" 
Represents a time in the format of HH:MM AM/PM.
"""
class Time:
    def __init__(self,h,m,apm):
        self.hour = h
        self.min = m
        self.apm = apm
        
    def timeValid(self):
        """ Returns True if the time is valid. False otherwise"""
        if not (1 <= self.hour <= 12):
            return False  # Hour should be between 1 and 12
        if not (0 <= self.min < 60):
            return False  # Minute should be between 0 and 59
        if self.apm not in ['AM', 'PM']:
            return False  # AM/PM should be either 'AM' or 'PM'
        return True  # If all checks pass, the time is valid
    
    def __eq__(self,other):
        """Return True if two time are the same."""
        return self.apm == other.apm and self.hour == other.hour and self.min == other.min
   
    def __str__(self):
        """ Returns a string representation of the time"""
        return f"{self.hour:02d}:{self.min:02d} {self.apm}"
