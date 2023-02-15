from datetime import date


class Student:

    def __init__(self, stuID, nm, dob, classif):
        self.__StudentID = stuID
        self.__Name = nm
        self.__dob = dob
        self.__classification = classif
        self.__age = 0
        self.__regDate = ''

    def calc_age(self):
        today = date.today()
        today_year = today.year
        dob = self.__dob.split('/')
        dob_year = int(dob[2])
        self.__age = today_year - dob_year
        
    def calc_reg(self):
        if self.__classification == 'senior':
            self.__regDate = '4/1 to 4/3'
        elif self.__classification == 'junior':
            self.__regDate = '4/4 to 4/6'
        elif self.__classification == 'sophomore':
            self.__regDate = '4/7 to 4/9'
        elif self.__classification == 'freshman':
            self.__regDate = '4/10 to 4/12'
        else:
            self.__regDate = 'Classification not found'

    def get_age(self):
        return self.__age

    def get_regDate(self):
        return self.__regDate