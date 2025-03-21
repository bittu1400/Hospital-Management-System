from Doctor import Doctor
from Patient import Patient
# from Person import Person

# import os.path

class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login_username(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        #Get the details of the admin

        username = input('Enter the username: ')
        with open("Admin_Username_Database.txt", "r") as f:
        # check if the username and password match the registered ones
            # if username == self.__username and password == self.__password:
            if username != f.read(): #and password == self.__password:
                # print("-----Login-----")
                return False
            else:
                return True
            
    def login_password(self) :
        password = input('Enter the password: ')
        with open("Admin_Password_Database.txt", "r") as f:
            if password != f.read(): #and password == self.__password:
                return False
            else:
                return True
        
        #ToDo1
        # pass

    def find_index(self, index, doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        input_first_name = input("Enter the first name: ")
        input_surname = input("Enter your surname: ")
        input_speciality = input("Enter the speciality: ")
        doctor = Doctor(input_first_name, input_surname, input_speciality)
        first_name = doctor.get_first_name()
        surname = doctor.get_surname()
        speciality = doctor.get_speciality()
        return first_name, surname, speciality
        # ToDo2
        # pass

    def patient_database(self, patients):
        file_path = "Patient_Database.txt"

       # with open(file_path, "r") as f:
        #     line_count = sum(1 for _ in f)l̥

        with open(file_path, "w") as f: 
                for patient in patients: #[line_count:]:  
                    details = patient.extra_detail()
                    f.write(f"{patient.full_name()}, {details[0]}, {details[1]}, {details[2]}, {details[3]}\n")
                    
        print("Database has been Loaded.\n")


    def view_patient_database(self):
        print("Patient Database")
        with open("Patient_Database.txt", "r")as f:
            print(f.read())

    def relocate_doctor(self, patients, doctors):

        print("----- Relocation -----")
        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            patient_index = int(patient_index) -1

            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return 

        except ValueError: 
            print('The id entered is incorrect')
            return 

        print("----- Re-Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms()

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                doctor_full_name = doctors[doctor_index].full_name()
                patients[patient_index].link(doctor_full_name)
                patient_full_name = patients[patient_index].full_name()
                doctors[doctor_index].add_patient(patient_full_name)
                # link the patients to the doctor and vice versa
                #ToDo11
                # pass
                print('The patient is now relocated to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect') 
            return
       
    def management_report(self, doctors, patients):
        while True:    
            print("Management Report")
            print("1: Total number of doctors in the system")
            print("2: Total number of patients per doctor")
            print("3: Total number of appointments per month per doctor")
            print("4: Total number of patients based on the illness type")
            print("5: Quit")
            input_choice = input("Enter your choice: ")
            if input_choice == '1':
                print(f"Total number of doctors: {len(doctors)}")
            elif input_choice == '2':
                for doctor in doctors:
                    print(f"Total number of patients of Dr.{doctor.full_name()}:\n{doctor.number_of_patients()[0]}")
                    print(f"Patients: {doctor.number_of_patients()[1]}")
            elif input_choice == '3':
                for doctor in doctors:
                    print(f"Total number of appointment of Dr.{doctor.full_name()}:\n{doctor.number_of_appointments()}")
            elif input_choice == '4':
                k = 1
                for patient in patients:
                    print(f"Total number of patients with {patient.disease(k).strip()}:\n{0}")
                    k += 1
            elif input_choice == '5':
                break
            else:
                print("Invalid Input!\n")

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')
        op = input("Enter your choice: ")
        #ToDo3
        # pass


        # register
        if op == '1':
            print("-----Register-----")
            print("Enter the doctor's details:\n")
            first_name = input("Enter the first name: ")
            surname = input("Enter the surname: ")
            specialty = input("Enter the speciality: ")
            # get the doctor details
            #ToDo4
            # pass

            # check if the name is already registered
            name_exists = False
            # count = 0
            # number = len(doctors)

            with open("Doctor_Database.txt", "r") as f:
                line = f.readlines()
                for l in line:
                    if first_name in l and surname in l:
                        print('Name already exists.')
                        return
            # count += 1

            doctors.append(Doctor(first_name, surname, specialty))
            with open(f"Doctor_Database.txt", "a") as f:
                f.write(f"{first_name},{surname},{specialty}\n")
            print("Doctor Registered.")

                    #ToDo5
                    # pass # save time and end the loop
            #ToDo6
            # pass# add the doctor ...
                                                         # ... to the list of doctors
            # print('Doctor registered.')

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            print('ID |          Full name           |  Speciality')
            self.view(doctors)

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index = self.find_index(index,doctors)
                    if doctor_index!=False:
                        break
                        
                    else:
                        print("Doctor not found")
                        # doctor_index is the ID mines one (-1)
                        

                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')
                    return

            # menu
            print('Choose the field to be updated:')
            print(' 1 :First name')
            print(' 2 :Surname')
            print(' 3 :Speciality')
            try:    
                op = int(input('Input: ')) # make the user input lowercase
                if op == 1:
                    
                    new_first_name = input("Enter the first name: ")
                    doctors[index].set_first_name(new_first_name)
                    print("Doctor first name Updated") 
                    # del doctors[name] (update not remove)
                elif op == 2:
                    new_surname = input("Enter the surname: ")
                    doctors[index].set_surname(new_surname)
                    print("Doctor surname Updated") 
                    # del doctors[last_name] (update not remove)
                elif op == 3:
                    new_specialty = input("Enter the specialty: ")
                    doctors[index].set_speciality(new_specialty)
                    print("Doctor specialty Updated") 
                    # del doctors[_specialty] (update not remove)
                else:
                    print("Invalid Input!")
            except ValueError:
                    print('The choice entered is incorrect')
                    return
            #ToDo8
            # pass

        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)
            try:
                doctor_index = int(input('Enter the ID of the doctor to be deleted: ')) - 1
                check_doctor_index = self.find_index(doctor_index,doctors)
                if check_doctor_index!= False:
                    del doctors[doctor_index]         
                else:
                    print("The id entered was not found")
            except ValueError:
                    print('The ID entered is incorrect')
                    return
            #ToDo9
            # pass

           
            # print('The id entered is incorrect')

        # if the id is not in the list of patients
        else:
            print('Invalid operation choosen. Check your spelling!')


    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        #ToDo10
        self.view(patients)

    def add_patients(self, patients):
        
        try:
            print("-----Register-----")
            print("Enter the Patients' details:\n")
            first_name = input("Enter the first name: ")
            surname = input("Enter the surname: ")
            age = int(input("Enter the age: "))
            mobile = input("Enter the mobile: ")
            post_code = input("Enter the post code: ")
            symptoms = input("Enter the symptoms of the patient: ")
            with open("Patient_Database.txt", "r") as f:
                line = f.readlines()
                for l in line:
                    if first_name + " " + surname in l and str(age) in l and mobile in l and post_code in l:
                        print(f"The patient {first_name} {surname} already exists.")
                        return

            patients.append(Patient(first_name, surname, age, mobile, post_code, symptoms))
            # with open("Patient_Symptoms_Database.tx"), "a") as f:
            #     f.write(symptoms)
            print("Patient Registered.")

        except ValueError:
            print('Please enter a valid age')
            return

    def view_patients_same_family(self, patients):
        fnd = []
        li = []
        for _patient in patients:
            if _patient.get_surname() in li:
                continue
            li.append(_patient.get_surname())
        print(li)
        # self.view(patients)
        check_family = input("Enter the surname of the patient: ")

        for _patient in patients:
            if _patient.get_surname() == check_family: #and _patient.get_surname() in check.values():
                fnd.append(_patient)

        if fnd:
            self.view(fnd)
            return
        
        print("No patient with the same family.")       

        #
        # else:
        #     continue
        # return id

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1
            # patients[patient_index].print_symptoms(patient_index)
            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        # print(patients[patient_index].)
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                doctor_full_name = doctors[doctor_index].full_name()
                patients[patient_index].link(doctor_full_name)
                patient_full_name = patients[patient_index].full_name()
                doctors[doctor_index].add_patient(patient_full_name)
                # link the patients to the doctor and vice versa
                #ToDo11
                # pass
                print('The patient is now assign to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')
            return


    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        # self.view(patients)
        try:
            print("-----Discharge Patient-----")
            patient_index = int(input('Please enter the patient ID: ')) - 1
            yes_no = input("Do you want to discharge this patient(Y/N): ").lower()
            
            if self.find_index(patient_index,patients) != False: 
                while True:    
                    if yes_no == "yes" or yes_no == "y":
                        print(f"{patients[patient_index].full_name()}has been discharged.")
                        discharge_patients = patients[patient_index]
                        break   
                    elif yes_no == "no" or yes_no == "n":
                        break
                    else:
                        print("Please provide a valid answer (yes/no).")
                        continue
            else:
                print('The id entered was not found.')
            
            return discharge_patients, patient_index, yes_no
        
        except ValueError: 
            print('The id entered is incorrect')
            return
        #ToDo12
        # pass

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(discharged_patients)
        #ToDo13
        # pass

    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        try:
            op = int(input('Input: '))

            if op == 1:

                username = input('Enter the new username: ')
                if username == input('Enter the new username again: '):
                    with open("Admin_Username_Database.txt", "w") as f:
                        f.write(f"{username}")
                        self.__username = username
                else:
                    print("Wrong username!")
                #ToDo14
                # pass

            elif op == 2:
                password = input('Enter the new password: ')
                # validate the password
                if password == input('Enter the new password again: '):
                    with open("Admin_Password_Database.txt", "w") as f:
                        f.write(f"{password}")
                        self.__password = password
                else:
                    print("Wrong password!")

            elif op == 3:

                address = input('Enter the new address: ')
                if address == input('Enter the new address again: '):
                        self.__address = address
                else:
                    print("Wrong address!")
                #ToDo15
                # pass

            else:
                print("Please enter a valid number from 1-3.")
                #ToDo16
                # pass
        
        except ValueError: 
            print('The id entered is incorrect')
            return

