mensaje_menu_principal = "--Menu Principal\n" \
                         "1) Universidad\n" \
                         "2) Salir\n"

mensaje_menu_universidad = "--Menu Universidad\n" \
                           "1) Datos\n" \
                           "2) Ajustes\n" \
                           "3) Salir\n"

mensaje_ajustes_universidad = "--Ajustes Universidad\n" \
                              "1) Cambiar Direccion\n" \
                              "2) Cambiar Telefono\n" \
                              "3) Salir\n"


def menu(mensaje):
    print(mensaje)
    opcion = input("Seleccione una opcion -> ")
    return opcion


def cambiar_direccion_universidad(universidad):
    print("Cambiando la direccion...")
    universidad.address = input("Ingrese la nueva direccion de la Universidad: ")
    print("Direccion cambiada...")


def cambiar_telefono_universidad(universidad):
    print("Cambiando el numero de telefono...")
    universidad.phone_number = input("Ingrese el nuevo numero de telefono de la Universidad: ")
    print("Telefono cambiado...")
