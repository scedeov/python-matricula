class Universidad:
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number

    def imprime_universidad(self):
        print("El nombre de la Universidad es %s\n"
              "La direccion de la Universidad es %s\n"
              "El numero de telefono de la Universidad es %s\n"
              % (self.name, self.address, self.phone_number))
