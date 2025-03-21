class Person:
    def __init__(self, first_name, surname):
        self.__first_name = first_name
        self.__surname = surname

    def full_name(self) :
        return self.__first_name + " " + self.__surname
        # pass

    def get_first_name(self) :
        return self.__first_name
        #ToDo2
        # pass

    def set_first_name(self, new_first_name):
        self.__first_name = new_first_name
        return self.__first_name
        #ToDo3
        # pass

    def get_surname(self) :
        return self.__surname
        #ToDo4
        # pass

    def set_surname(self, new_surname):
        self.__surname = new_surname
        return self.__surname
        #ToDo5
        # pass