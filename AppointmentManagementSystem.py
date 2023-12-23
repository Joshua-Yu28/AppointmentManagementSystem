#AppointmentManagementSystem.py
#Zhuocheng Yu
#Dec 8 2023

"""
A program for appointment management system. The system will manage appointment information 
for multiple users. Each user will have his/her own appointment diary. An appointment diary will 
allow the user to maintain their appointments from now until December 31st,2024. (This is a soft
deadline. At least dates until the end of 2024 must be supported. If your implementation supports 
more than that, no problem.) Each appointment entry in the diary contains information about date,
time, and purpose of the appointment. 
"""

from Appointment import Appointment
from Date import Date
from Time import Time
from User import User
import re
def main():
    userNameList = []
    user_dict = {}
    while True:
        print("Welcome to Appointment Management System! What would you like to do?\n")
        print("-  [a] Add new user")
        print("-  [d] Delete an existing user")
        print("-  [l] List existing users")
        print("-  [s] Schedule an appointment")
        print("-  [c] Cancel an appointment")
        print("-  [f] Check for appointment on certain date and time")
        print("-  [p] Retrieve purpose of an appointment")
        print("-  [r] Reschedule an existing appointment")
        print("-  [x] Exit the system")
        choice = input()# get the input from user
        L=['a','d','l','s','c','f','p','r','x']
        
        if choice not in L:
            print("Invalid Option,")


        elif choice == 'a':#Add new user
            userName = input("Enter a new username:")
            userNameLow = userName.lower()# change the name to lower case
            if userNameLow in userNameList:
                print("The username has been used. Please try again!")
            else:
                for char in userNameLow:
                    if not (char.isalnum() or char in [".","_"]):
                        print("Sorry, usernames only consist of alphabets, numbers, dots, and underscores. Please try again!")
                        break
                else:    
                    userNameList.append(userNameLow)
                    userInstance = User(userNameLow) #create a new User instance
                    user_dict[userNameLow] = userInstance #store the User instance into dictionary
                    print("Adding is successful!")
                    

        elif choice == 'd':#Delete an existing user
            delUserName = input("Which username do you want to delete?")
            if delUserName in userNameList:
                userNameList.remove(delUserName)
                user_dict.get(delUserName,None).diary.appointmentList = []
                print(f"Username {delUserName} is deleted successfully!")
            else:
                print(f"Username {delUserName} is not found.")
        

        elif choice == 'l':#List existing users 
            userNameList = sorted(userNameList)
            print(userNameList)
        

        elif choice == 's':#Schedule an appointment
            userNameSearch = input("Please enter username:")
            
            #make sure input userName is valid
            for char in userNameSearch:
                    if not (char.isalnum() or char in [".","_"]):
                        print("Sorry, usernames only consist of alphabets, numbers, dots, and underscores. Please try again!") 
                        break
            if userNameSearch not in userNameList:
                print("The user isn't in the list, please enter another one.")
                continue
            
            #make sure input date is valid 
            date = input("Please enter the date YYYY-MM-DD :")
            date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
            if not date_pattern.match(date):
                print("Invalid date.")
                continue
            datePart = date.split('-')
            dateValue=Date(int(datePart[0]),int(datePart[1]),int(datePart[2]))
            if not dateValue.dateValid():
                print("Invalid date.")
                continue

            #make sure input time is valid
            st = input("Please enter the start time HH:MM AM/PM :")
            et = input("Please enter the end time HH:MM AM/PM :")
            time_pattern = re.compile(r'^\d{1,2}:\d{2} [APM]{2}$')
            if not time_pattern.match(st) or not time_pattern.match(et):
                print("Invalid time.")
                continue
            st_parts = st.split()
            stPart = st_parts[0].split(':')
            et_parts = et.split()
            etPart = et_parts[0].split(':')
            stValue = Time(int(stPart[0]),int(stPart[1]),st_parts[1])
            etValue = Time(int(etPart[0]),int(etPart[1]),et_parts[1])
            if not stValue.timeValid() or not etValue.timeValid():
                print("Invalid time.")
                continue

            #If endtime is earlier than starttime, print "Invalid time."
            if st_parts[1] == 'PM' and et_parts[1] == 'AM':
                print("Invalid time.")
                continue
            if st_parts[1] == et_parts[1]:
                if int(stPart[0]) > int(etPart[0]) or (int(stPart[0]) == int(etPart[0]) and int(stPart[1]) > int(etPart[1])):
                    print("Invalid time.")
                    continue
            purpose = input("Please enter your purpose:")

            #make sure that the appointment does not conflict with an existing appointment
            if st_parts[1] == 'PM':
                stTime = 12*60+int(stPart[0])*60+int(stPart[1])
            else:
                stTime = int(stPart[0])*60+int(stPart[1])
            if et_parts[1] == 'PM':
                etTime = 12*60+int(etPart[0])*60+int(etPart[1])
            else:
                etTime = int(etPart[0])*60+int(etPart[1])

            flag = False# make sure when time conflicts, the program can return to the welcome page.
            for x in user_dict.values():
                for c in x.diary.appointmentList:
                    if c[0] == date:
                        c1_parts = c[1].split()
                        c1Part = c1_parts[0].split(':')
                        c2_parts = c[2].split()
                        c2Part = c2_parts[0].split(':')
                        if c1_parts[1] == 'PM':
                            c1Time = 12*60+int(c1Part[0])*60+int(c1Part[1])
                        else:
                            c1Time = int(c1Part[0])*60+int(c1Part[1])
                        if c2_parts[1] == 'PM':
                            c2Time = 12*60+int(c2Part[0])*60+int(c2Part[1])
                        else:
                            c2Time = int(c2Part[0])*60+int(c2Part[1])
                        
                        if (c1Time - etTime)*(c2Time - stTime) <= 0: #make sure that when time conflicts, the program can make a response
                            print("Time conflict!")
                            flag = True
                            break
                if flag == True:
                    break
            if flag == True:    
                continue        
            user_dict.get(userNameSearch,None).diary.appointmentList.append(Appointment(date,st,et,purpose).toList())
            print(Appointment(date,st,et,purpose).toList())
            print(user_dict.get(userNameSearch,None).diary.appointmentList)
        
        
        elif choice == 'c':#Cancel an appointment
            #make sure input userName is valid
            userNameCancel= input("What's your userName?")
            for char in userNameCancel:
                    if not (char.isalnum() or char in [".","_"]):
                        print("Sorry, usernames only consist of alphabets, numbers, dots, and underscores. Please try again!") 
                        break
            if userNameCancel not in userNameList:
                print("The user isn't in the list, please enter another one.")
                continue
            
            #make sure input date is valid 
            dateCancel = input("What's your appointment date?")
            date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
            if not date_pattern.match(dateCancel):
                print("Invalid date.")
                continue
            datePart = dateCancel.split('-')
            dateValue=Date(int(datePart[0]),int(datePart[1]),int(datePart[2]))
            if not dateValue.dateValid():
                print("Invalid date.")
                continue

            #make sure input time is valid
            stCancel = input("What's your starting time?")
            time_pattern = re.compile(r'^\d{1,2}:\d{2} [APM]{2}$')
            if not time_pattern.match(stCancel):
                print("Invalid time.")
                continue
            st_parts = stCancel.split()
            stPart = st_parts[0].split(':')
            stValue = Time(int(stPart[0]),int(stPart[1]),st_parts[1])
            if not stValue.timeValid():
                print("Invalid time.")
                continue

            for c in user_dict.get(userNameCancel,None).diary.appointmentList:
                if c[0] == dateCancel and c[1] == stCancel:
                    user_dict.get(userNameCancel,None).diary.appointmentList.remove(c)
                    print("Cancel successfully!")
                    break
            else:
                print("No such appointment found!")


        elif choice == 'f':#Check for appointment on certain date and time
            userNameCheck= input("What's your userName?")
            dateCheck = input("What's your appointment date?")
            stCheck = input("What's your starting time?")
            #make sure input userName is valid
            for char in userNameCheck:
                    if not (char.isalnum() or char in [".","_"]):
                        print("Sorry, usernames only consist of alphabets, numbers, dots, and underscores. Please try again!") 
                        break
            if userNameCheck not in userNameList:
                print("The user isn't in the list, please enter another one.")
                continue
            
            #make sure input date is valid 
            date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
            if not date_pattern.match(dateCheck):
                print("Invalid date.")
                continue
            datePart = dateCheck.split('-')
            dateValue=Date(int(datePart[0]),int(datePart[1]),int(datePart[2]))
            if not dateValue.dateValid():
                print("Invalid date.")
                continue

            #make sure input time is valid
            time_pattern = re.compile(r'^\d{1,2}:\d{2} [APM]{2}$')
            if not time_pattern.match(stCheck):
                print("Invalid time.")
                continue
            st_parts = stCheck.split()
            stPart = st_parts[0].split(':')
            stValue = Time(int(stPart[0]),int(stPart[1]),st_parts[1])
            if not stValue.timeValid():
                print("Invalid time.")
                continue

            for c in user_dict.get(userNameCheck,None).diary.appointmentList:
                if c[0] == dateCheck and c[1] == stCheck:
                    print("Appointment found!",c)
                    break
            else:
                print("No such appointment found!")


        elif choice == 'p':#Retrieve purpose of an appointment
            #make sure input userName is valid
            userNameRetrieve= input("What's your userName?")
            for char in userNameRetrieve:
                    if not (char.isalnum() or char in [".","_"]):
                        print("Sorry, usernames only consist of alphabets, numbers, dots, and underscores. Please try again!") 
                        break
            if userNameRetrieve not in userNameList:
                print("The user isn't in the list, please enter another one.")
                continue
            
            #make sure input date is valid 
            dateRetrieve = input("What's your appointment date?")
            date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
            if not date_pattern.match(dateRetrieve):
                print("Invalid date.")
                continue
            datePart = dateRetrieve.split('-')
            dateValue=Date(int(datePart[0]),int(datePart[1]),int(datePart[2]))
            if not dateValue.dateValid():
                print("Invalid date.")
                continue

            #make sure input time is valid
            stRetrieve = input("What's your starting time?")
            time_pattern = re.compile(r'^\d{1,2}:\d{2} [APM]{2}$')
            if not time_pattern.match(stRetrieve):
                print("Invalid time.")
                continue
            st_parts = stRetrieve.split()
            stPart = st_parts[0].split(':')
            stValue = Time(int(stPart[0]),int(stPart[1]),st_parts[1])
            if not stValue.timeValid():
                print("Invalid time.")
                continue

            for c in user_dict.get(userNameRetrieve,None).diary.appointmentList:
                if c[0] == dateRetrieve and c[1] == stRetrieve:
                    print("Purpose is:",c[3])
                    break
            else:
                print("No such appointment found!")


        elif choice == 'r':#Reschedule an existing appointment
            #make sure input userName is valid
            userNamereschedule= input("What's your userName?")
            for char in userNamereschedule:
                    if not (char.isalnum() or char in [".","_"]):
                        print("Sorry, usernames only consist of alphabets, numbers, dots, and underscores. Please try again!") 
                        break
            if userNamereschedule not in userNameList:
                print("The user isn't in the list, please enter another one.")
                continue
            
            #make sure input date is valid 
            dateOld = input("What's your appointment date?")
            date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
            if not date_pattern.match(dateOld):
                print("Invalid date.")
                continue
            datePart = dateOld.split('-')
            dateValue=Date(int(datePart[0]),int(datePart[1]),int(datePart[2]))
            if not dateValue.dateValid():
                print("Invalid date.")
                continue

            #make sure input time is valid
            stOld = input("What's your starting time?")
            time_pattern = re.compile(r'^\d{1,2}:\d{2} [APM]{2}$')
            if not time_pattern.match(stOld):
                print("Invalid time.")
                continue
            st_parts = stOld.split()
            stPart = st_parts[0].split(':')
            stValue = Time(int(stPart[0]),int(stPart[1]),st_parts[1])
            if not stValue.timeValid():
                print("Invalid time.")
                continue

            for c in user_dict.get(userNamereschedule,None).diary.appointmentList:
                if c[0] == dateOld and c[1] == stOld:
                    L = list(c)# store c temporarily, if new appointment not valid, append L again
                    purpose = L[3]
                    user_dict.get(userNamereschedule,None).diary.appointmentList.remove(c)

                    #make sure input date is valid 
                    date = input("Please enter the new date YYYY-MM-DD :")
                    date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
                    if not date_pattern.match(date):
                        print("Invalid date.")
                        user_dict.get(userNamereschedule,None).diary.appointmentList.append(L)
                        continue
                    datePart = date.split('-')
                    dateValue=Date(int(datePart[0]),int(datePart[1]),int(datePart[2]))
                    if not dateValue.dateValid():
                        user_dict.get(userNamereschedule,None).diary.appointmentList.append(L)
                        print("Invalid date.")
                        continue

                    #make sure input time is valid
                    st = input("Please enter the new start time HH:MM AM/PM :")
                    et = input("Please enter the new end time HH:MM AM/PM :")
                    time_pattern = re.compile(r'^\d{1,2}:\d{2} [APM]{2}$')
                    if not time_pattern.match(st) or not time_pattern.match(et):
                        user_dict.get(userNamereschedule,None).diary.appointmentList.append(L)
                        print("Invalid time.")
                        continue
                    st_parts = st.split()
                    stPart = st_parts[0].split(':')
                    et_parts = et.split()
                    etPart = et_parts[0].split(':')
                    stValue = Time(int(stPart[0]),int(stPart[1]),st_parts[1])
                    etValue = Time(int(etPart[0]),int(etPart[1]),et_parts[1])
                    if not stValue.timeValid() or not etValue.timeValid():
                        user_dict.get(userNamereschedule,None).diary.appointmentList.append(L)
                        print("Invalid time.")
                        continue

                    #If endtime is earlier than starttime, print "Invalid time."
                    if st_parts[1] == 'PM' and et_parts[1] == 'AM':
                        user_dict.get(userNamereschedule,None).diary.appointmentList.append(L)
                        print("Invalid time.")
                        continue
                    if st_parts[1] == et_parts[1]:
                        if int(stPart[0]) > int(etPart[0]) or (int(stPart[0]) == int(etPart[0]) and int(stPart[1]) > int(etPart[1])):
                            user_dict.get(userNamereschedule,None).diary.appointmentList.append(L)
                            print("Invalid time.")
                            continue
                    

                    #make sure that the appointment does not conflict with an existing appointment
                    if st_parts[1] == 'PM':
                        stTime = 12*60+int(stPart[0])*60+int(stPart[1])
                    else:
                        stTime = int(stPart[0])*60+int(stPart[1])
                    if et_parts[1] == 'PM':
                        etTime = 12*60+int(etPart[0])*60+int(etPart[1])
                    else:
                        etTime = int(etPart[0])*60+int(etPart[1])

                    flag = False# make sure when time conflicts, the program can return to the welcome page.
                    for x in user_dict.values():
                        for c in x.diary.appointmentList:
                            if c[0] == date:
                                c1_parts = c[1].split()
                                c1Part = c1_parts[0].split(':')
                                c2_parts = c[2].split()
                                c2Part = c2_parts[0].split(':')
                                if c1_parts[1] == 'PM':
                                    c1Time = 12*60+int(c1Part[0])*60+int(c1Part[1])
                                else:
                                    c1Time = int(c1Part[0])*60+int(c1Part[1])
                                if c2_parts[1] == 'PM':
                                    c2Time = 12*60+int(c2Part[0])*60+int(c2Part[1])
                                else:
                                    c2Time = int(c2Part[0])*60+int(c2Part[1])
                                
                                if (c1Time - etTime)*(c2Time - stTime) <= 0: #make sure that when time conflicts, the program can make a response
                                    user_dict.get(userNamereschedule,None).diary.appointmentList.append(L)
                                    print("Time conflict!")
                                    flag = True
                                    break
                        if flag == True:
                            break
                    if flag == True:    
                        break
                  
                    user_dict.get(userNamereschedule,None).diary.appointmentList.append(Appointment(date,st,et,purpose).toList())
                    print(Appointment(date,st,et,purpose).toList())
                    print(user_dict.get(userNamereschedule,None).diary.appointmentList)
            
                    break
            else:
                print("No such appointment found!")

        elif choice == 'x':
            print("Goodbye!, thank you for using the appointment management system!")
            exit()

if __name__ == '__main__':
    main()


