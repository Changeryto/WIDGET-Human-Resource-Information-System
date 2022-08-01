class Employe:
    def __init__(self, name, phone, comment):
        self.__name = name
        self.__phone = phone
        self.__comment = comment

    def comprobation(self):
        return f"\n\nNew employee saved\nName: {self.__name} \nPhone: {self.__phone} \nComment: {self.__comment}\n"

    def file(self):
        return f"{self.__name} - {self.__phone} - {self.__comment}\n"