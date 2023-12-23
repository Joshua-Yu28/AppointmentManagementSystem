#AppointmentManagementSystem.py
#Zhuocheng Yu
#Dec 8 2023
"""
    Represents a date.
       m : index of month [int]
       d : day  [int]
       y : year [int]
"""
class Date:
    def __init__(self,y,m,d):
        self.year = y
        self.month = m
        self.day = d

    def __eq__(self,other):
        """If two given days are the same day, return True."""
        return self.year == other.year and self.month == other.month and self.day == other.day

    def dateValid(self):
        """ Returns True if the date is valid. False otherwise"""
        y, m, d = self.year, self.month, self.day
        if m < 1 or m > 12:
            return False  # Month should be between 1 and 12
        if d < 1:
            return False  # Day should be greater than 0
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.isLeapYear() and m == 2:
            days_in_month[2] = 29  # Update days in February for a leap year
        if d > days_in_month[m]:
            return False  # Day exceeds the maximum for the given month
        return True  # If all checks pass, the date is valid
        
    def isLeapYear(self):
        """ Returns True if y is a leap year. False otherwise"""
        y = self.year
        return ((y%100>0) and y%4==0) or ((y%100==0) and (y%400==0))

    def __str__(self):
        """Print in the format of YYYY-MM-DD."""
        return f'{self.y:04d}-{self.m:02d}-{self.day:02d}'