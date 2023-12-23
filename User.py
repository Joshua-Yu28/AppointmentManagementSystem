#AppointmentManagementSystem.py
#JoshuaY
#Dec 8 2023
"""
i. User name
ii. AppointmentDiary object representing the user’s diary
"""
import AppointmentDiary
class User:
    def __init__(self,userName):
        self.userName = userName
        self.diary = AppointmentDiary.AppointmentDiary()
