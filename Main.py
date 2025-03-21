# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient
# import os.path
# from Person import Person

def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
    doctors = load_doctor_data()
    patients = load_patient_data()
    discharged_patients = []
    # family_list = {"Sara Smith" :[Patient('Sara','Smith', 20, '07012345678','B1 234'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC')]}
    # running = True
    # keep trying to login tell the login details are correct
    while True:
        admin_password = admin.login_username()
        admin_login = admin.login_password()
        # print(admin_login)
        # print(admin_password)
        if admin_login == True and admin_password == True:
            running = True # allow the program to run
            print("-----Login-----")
            break
        else:
            print('Incorrect username or password.')

    while running:
        # print the menu
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- View/ Discharge patients')
        print(' 3- View discharged patient')
        print(' 4- Assign doctor to a patient')
        print(' 5- Update admin detais')
        print(' 6- Add patients')
        print(' 7- View patients of same family')
        print(' 8- Store patient data')
        print(' 9- View patient database (To get the latest data, please call no.8)')
        print(' 10- Relocate Doctor')
        print(' 11- Management Report')
        print(' 12- Quit')

        # get the option
        op = input('Option: ')
        if op == '1':
            admin.doctor_management(doctors)
            # 1- Register/view/update/delete doctor
            #ToDo1
            # pass
        

        elif op == '2':
            admin.view_patient(patients)
            # 2- View or discharge patients
            #ToDo2
            # pass

            while True:
                op = input('Do you want to discharge a patient(Y/N):').lower()

                if op == 'yes' or op == 'y':
                    discharge_patient = None
                    discharge_patients = admin.discharge(patients, discharge_patient)
                    if discharge_patients[2] == "no" or discharge_patients[2] == "n":  
                        break
                    else:
                        discharged_patients.append(discharge_patients[0])
                        del patients[discharge_patients[1]] 
                        break
                    #ToDo3
                    # pass

                elif op == 'no' or op == 'n':
                    break

                # unexpected entry
                else:
                    print('Please answer by yes or no.')
        
        elif op == '3':
            admin.view_discharge(discharged_patients)
            # 3 - view discharged patients
            #ToDo4
            # pass

        elif op == '4':
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '5':
            # 5- Update admin detais
            admin.update_details()

        elif op == '6':
            admin.add_patients(patients)

        elif op == '7':
            admin.view_patients_same_family(patients)
        
        elif op == '8':
            admin.patient_database(patients)

        elif op == '9':
            admin.view_patient_database()

        elif op == '10':
            admin.relocate_doctor(patients, doctors)

        elif op == '11':
            admin.management_report(doctors, patients)

        elif op == '12':
            running = False
            # 6 - Quit
            #ToDo5
            # pass

        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

def load_patient_data():
    with open("Patient_Database.txt") as s:
        data = s.readlines()

    _r_data = []

    for _line in data:
        _line  = [_.strip() for _ in _line.split(",")]

        name = _line[0]
        age = _line[1]
        no = _line[2]
        postcode = _line[3]
        symptoms = _line[4]
        fname = name.split(" ")
        lname = fname[1]
        fname = fname[0]

        _r_data.append(Patient(
            first_name=fname,
            surname=lname,
            age=age,
            mobile=no,
            postcode=postcode,
            symptoms= symptoms
        ))

    return _r_data

def load_doctor_data():
    with open("Doctor_Database.txt") as s:
        data = s.readlines()

    _r_data = []

    for _line in data:
        _line  = [_.strip() for _ in _line.split(",")]
        # print(_line)
        fname = _line[0]
        lname = _line[1]
        spec = _line[2]

        _r_data.append(Doctor(
            first_name=fname,
            surname=lname,
            speciality=spec
        ))

    return _r_data

if __name__ == '__main__':
    main()
