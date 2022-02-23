class Patient:
    #initialize class
    def __init__(self, ID, name, address, phone, veteran_status):
        self.__ID = ID
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__veteran_status = veteran_status
    
    #NOT NEEDED
    # #set individual attributes
    # def set_ID(self, ID):
    #     self.__ID = ID
    # def set_name(self, name):
    #     self.__name = name
    # def set_address(self, address):
    #     self.__address = address
    # def set_phone(self, phone):
    #     self.__phone = phone
    # def set_veteran_status(self, veteran_status):
    #     self.__veteran_status = veteran_status

    #view individual attributes
    def get_ID(self):
        return self.__ID
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_phone(self):
        return self.__phone
    def get_veteran_status(self):
        return self.__veteran_status
    
    