from GUI import \
    menu, mensaje_menu_universidad, mensaje_ajustes_universidad, mensaje_menu_principal, \
    cambiar_direccion_universidad, cambiar_telefono_universidad
from Universidad import Universidad


def inicio():
    print("Welcome...\n")
    universidad = Universidad("Universidad de Costa Rica", "Pavas", 87878787)
    control_menu_principal(universidad)


def control_menu_principal(universidad):
    end = False
    while not end:
        opcion = int(menu(mensaje_menu_principal))
        if opcion == 1:
            control_universidad(universidad)
        elif opcion == 2:  # Salir
            end = True


def control_universidad(universidad):
    end = False
    while not end:
        option = int(menu(mensaje_menu_universidad))
        if option == 1:
            universidad.imprime_universidad()
        elif option == 2:
            control_ajustes_universidad(universidad)
        elif option == 3:  # Salir
            end = True


def control_ajustes_universidad(universidad):
    end = False
    while not end:
        option = int(menu(mensaje_ajustes_universidad))
        if option == 1:
            cambiar_direccion_universidad(universidad)
        elif option == 2:
            cambiar_telefono_universidad(universidad)
        elif option == 3:  # Salir
            end = True
