from Person import Person
class Doctor (Person):
    """A class that deals with the Doctor operations"""


    def __init__(self, first_name, surname, speciality):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            speciality (string): Doctor`s speciality
        """
        super().__init__(first_name, surname)
        # print(self._first_name)
        # self.__first_name = first_name
        # self.__surname = surname
        self.__speciality = speciality
        self.__patients = []
        self.__appointments = []
    
    # def full_name(self) :
    #     return self.__first_name + " " + self.__surname
    #     # pass

    # def get_first_name(self) :
    #     return self.__first_name
    #     #ToDo2
    #     # pass

    # def set_first_name(self, new_first_name):
    #     self.__first_name = new_first_name
    #     return self.__first_name
    #     #ToDo3
    #     # pass

    # def get_surname(self) :
    #     return self.__surname
    #     #ToDo4
    #     # pass

    # def set_surname(self, new_surname):
    #     self.__surname = new_surname
    #     return self.__surname
    #     # ToDo5
    #     # pass

    def get_speciality(self) :
        return self.__speciality
        #ToDo6
        # pass

    def set_speciality(self, new_speciality):
        self.__speciality = new_speciality
        return self.__speciality
        #ToDo7
        # pass

    def add_patient(self, patient):
        return self.__patients.append(patient), self.__appointments.append(patient)

    def number_of_patients(self):
        number = len(self.__patients)
        return number, self.__patients
    
    def number_of_appointments(self):
        number = len(self.__appointments)
        return number

    def __str__(self) :
        return f'{self.full_name():^30}|{self.__speciality:^15}'

# doctor = Doctor("Bittu", "Sah", "Neurology")
# print(doctor.__str__())
# doctor.set_first_name("bittu")
# doctor.set_surname("sah")
# doctor.set_speciality("neurology")
# print(doctor.__str__())
# doctor.add_patient("Puspe")
# doctor.add_patient("Sanju")
# doctor.add_patient("Puspa")
# print(doctor.number_of_patients())
# print(doctor.number_of_appointments())







