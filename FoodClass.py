class customer:

    def __init__(self, cid, name, address, email, phone, memstat):
        self.__cid = cid
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__memstat = memstat

    def get_memstat(self, discount):
        if self.__memstat == True:
            discount = .2
        else:
            discount = 0

        return discount

    
class transaction:

    def __init__(self, date, itemNm, cost, cid):
        self.__date = date
        self.__itemNm = itemNm
        self.__cost = cost
        self.__cid = cid
    
