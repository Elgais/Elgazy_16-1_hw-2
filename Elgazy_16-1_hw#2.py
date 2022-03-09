class Person:

    def __init__(self, last_name,first_name):
        self.last_name= last_name
        self.first_name = first_name


class Jack(Person):



    def __init__(self, last_name, first_name,phone_number,balance):
        super().__init__(last_name, first_name)
        self.phone_number= phone_number
        self.balance=balance


bal= Jack('Isaev','Elgazy','+996151112',400)
low=bal.balance

class Vito(Jack):
    _n_number = 50

    def __init__(self, last_name, first_name, phone_number, balance):
        super().__init__(last_name, first_name, phone_number, balance)

    def min(self):
        fir = bal.balance - self._n_number
        sec = self.balance + fir
        print(f'{bal.balance} - {self._n_number} = {sec} \nOn balance Vito was {bal2.balance}')
bal2 = Vito('poe','vito','+99650123132',10)
Vito.min(bal2)
