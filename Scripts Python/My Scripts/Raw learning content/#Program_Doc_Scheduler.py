#Program_Doc_Scheduler 

import datetime, time

all_doctors = {}
all_patients = {}

class Patient():
    
    def __init__(self,name):

            self.id = 0
            self.full_name = name.title()
            self.name = self.full_name.split()[0]
        
class Doctor():
    
    def __init__(self,name, specialty = "General Practitioner - G.P"):
        
        self.id = 0
        self.full_name = name.title()
        self.name = self.full_name.split()[0]
        self.specialty = specialty.title()
        self.schedule = {8:"",8.5:"",9:"",9.5:"",10:"",10.5:"",11:"",11.5:"",14:"",14.5:"",15:"",15.5:"",16:"",16.5:"",17:"",17.5:""}


    def __str__(self):

        return self.name


def check_choice(choice):
    pass

def new_patient_doctor(input):

    in_data = False
    if type(input) == Patient:  
        for patient in all_patients.values():
            if input.full_name.title() == patient.full_name:
                in_data = True
                break

        if not in_data:
            input.id = len(all_patients)+1
            all_patients[input.id] = input

    if type(input) == Doctor:  
        for doctor in all_doctors.values():
            if input.full_name.title() == doctor.full_name:
                in_data = True
                break

        if not in_data:
            input.id = len(all_doctors)+1
            all_doctors[input.id] = input

def check_for_docs():

    avaiable_docs = {}
    for id, doctor in all_doctors.items():
        if "" in doctor.schedule.values():
            print(f"{doctor.id} - Dr(a). {doctor.name}\t Specialty: {doctor.specialty}")
            avaiable_docs[id] = doctor
        else:
            print(f"Dr(a). {doctor.name}\t Specialty: {doctor.specialty} is not avaiable today.\n")

    return avaiable_docs

def appointment(doctor, patient):
    print("Choose from the avaiable options in the schedule:\n")
    for hour, name in doctor.schedule.items():
        if name == "":
            f_hour = str(datetime.time(int(hour//1),int((hour%1)*60)))[:5]
            print(f_hour) 

    while True:
        try:
            appoint = input("Choose from avaiable hours: Format 24h hh:mm")
            if ":" in appoint:
                appoint = appoint.split(":")
                appoint = float(appoint[0]) + float(appoint[1])/60
            else:
                appoint = int(appoint)

            f_hour = str(datetime.time(int(appoint//1),int((appoint%1)*60)))[:5]

            if doctor.schedule[appoint] == "":
                doctor.schedule[appoint] = patient.full_name
                print(f"Appointment scheduled to {f_hour} tonight")
                break
            else:
                print("Not avaiable")
                continue 
        except:
            if appoint == "0" or appoint == 0:
                break
            else:
                print("Imcopatible format, try hh:mm. Ex: 15:30")
                continue

def check_appoint(user):

    total_appoint = 0
    for doctors in all_doctors.values():
        for hours, patient in doctors.schedule.items():
            if user.full_name == patient:
                f_hour = str(datetime.time(int(hours//1),int((hours%1)*60)))[:5]
                print(f" You have an appointment with Dr.{doctors.name} Specialist in {doctors.specialty}\t at {f_hour}")
                total_appoint += 1

    if total_appoint == 0:
        print("You do not have any appointments today.")

if __name__ == "__main__":

    doc1 = Doctor("Lucas Moura")
    doc2 = Doctor("Rafael Silva",specialty = "Dermatology")
    doc3 = Doctor("Luciano Alves",specialty = "Psicology")
    new_patient_doctor(doc1)
    new_patient_doctor(doc2)
    new_patient_doctor(doc3)
    
    menu_on = True
    user = Patient(input("Welcome to clinic X. Please insert your full name "))
    new_patient_doctor(user)
    print(f"Welcome {user.name}, how can we help you? Please insert only the number of the desired option.")
    while menu_on:
        print("\nOption 1 - I'd like to make an appointment")
        print("Option 2 - Check for my appointments")
        print("Option 0 - Quit")
        try:
            choice = int(input())
            if choice not in [0,1,2]:
                print("\nInvalid option, try again.")
                continue
        except:
            print("\nInvalid option, try again.")
            continue

        if choice == 0:
            print("Until next time. :)")
            menu_on = False
    
        if choice == 1:
            # Display Doctors and Specialty
            avaiable_docs = check_for_docs()
            print("0 - Back")
            while choice != 0:
                try:
                    # Choose one
                    choice = int(input(f"Please choose an avaiable doctor: 0 - Quit"))
                    if choice not in avaiable_docs.keys():
                        print("Doctor unavailable.")
                        continue
                    else:
                        doctor = all_doctors[choice]
                        # Display any schedule avaiable
                        appointment(doctor,user)
                        choice = 0
                except:
                    print("\nInvalid option, try again.")
                    continue      
        if choice == 2:
            # Check for appointment on pacient's name
            check_appoint(user)
            # Display appointment or lack of it
            