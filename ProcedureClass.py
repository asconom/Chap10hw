class Procedure:
    def __init__(self, name, date, practitioner, charges, id):
        self.__proc_name = name
        self.__proc_date = date
        self.__practitioner = practitioner
        self.__charges = charges
        self.__patient_id = id

    def get_name(self):
        return self.__proc_name
    def get_date(self):
        return self.__proc_date
    def get_practitioner(self):
        return self.__practitioner
    def get_charges(self):
        return self.__charges
    def get_patient_id(self):
        return self.__patient_id
    