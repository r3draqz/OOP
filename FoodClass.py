# import random

class Customer:

    def __init__(self, cid, name, address, email, phone, memstat):
        self.__cid = cid
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__memstat = memstat

    def get_memstat(self):
        return self.__memstat
    
    def getcid(self):
        return self.__cid

    def getname(self):
        return self.__name

    def getphone(self):
        return self.__phone
    


        
class Transaction:

    def __init__(self, date, itemNm, cost, cid):
        self.__date = date
        self.__itemNm = itemNm
        self.__cost = cost
        self.__cid = cid

    def getdate(self):
        return self.__date

    def getitemnm(self):
        return self.__itemNm

    def getcost(self):
        return self.__cost

    def getcid(self):
        return self.__cid
    

        
