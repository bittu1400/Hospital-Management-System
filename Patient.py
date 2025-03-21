from Person import Person
class Patient (Person):
    """Patient class"""

    
    def __init__(self, first_name, surname, age, mobile, postcode, symptoms):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """
        super().__init__(first_name, surname)
        # self.__first_name = first_name
        # self.__surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__symptoms = symptoms
        #ToDo1
        # pass
        self.__doctor = 'None'

    # def check_family_name(self):
    #     return self.__surname
    
    # def full_name(self) :
    #     """full name is first_name and surname"""
    #     return self.__first_name + " " + self.__surname
        #ToDo2
        # pass

    def extra_detail(self) :
        """full name is first_name and surname"""
        return self.__age, self.__mobile, self.__postcode, self.__symptoms

    def get_doctor(self) :
        return self.__doctor
        #ToDo3
        # pass

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor
        return self.__doctor

    def disease(self, index):
        disease = [    "Common Cold",
    "Seasonal Allergies (Hay Fever)",
    "Mild Food Poisoning",
    "Athlete's Foot",
    "Pink Eye (Viral Conjunctivitis)",
    "Cold Sores",
    "Mild Ear Infection",
    "Dandruff",
    "Skin Warts",
    "Hiccups" ]
        return disease[index]
    
    def symptoms(self):
        return self.__symptoms

    def print_symptoms(self):
        """prints all the symptoms"""
        print(self.__symptoms)
    
    def __str__(self):
        return f'{self.full_name():^30}|{str(self.__doctor):^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'

# patient1 = Patient("Suraj", "Sah", 20, 9876543210, 46500)
# patient1.link("Bittu")
# print(patient1.__str__())
# patient1.print_symptoms(int(input("Enter from 1-3: ")))

