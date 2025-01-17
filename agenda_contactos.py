
def mostrar_menu():
    print("\n Agenda de contactos:" )
    print("1. Agregar nuevo contacto" )
    print("2. Eliminar contacto" )
    print("3. Buscar contacto" )
    print("4. Lista de contactos:" )
    print("5. Salir del programa" )

def agregar_contacto(agenda):
    nombre = input("Por favor ingresa el nombre completo del contacto: ")
    telefono = input("Por favor ingresa el teléfono del contacto: ")
    email = input("Por favor ingresa el email del contacto: ")
    agenda[nombre] = {"telefono": telefono, "email": email}
    print(f"¡Se ha agregado el contacto {nombre} exitosamente!")

def eliminar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto a eliminar")
    if nombre in agenda:
        del agenda[nombre]
        print(f"El contacto de {nombre} ha sido eliminado correctamente")
    else:
        print(f"No se ha encontrado un contacto con el nombre {nombre}") 


def buscar_contacto(agenda):
    nombre = input("Por favor ingrese el nombre del contacto a buscar: ")
    if nombre in agenda:
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {agenda[nombre]["telefono"]}")
        print(f"Email: {agenda[nombre]["email"]}")
    else:
        print(f"El contacto {nombre} que has buscado no se encuentra en tu agenda")

def listar_contacto(agenda):
    if agenda:
        print("\nLista de contactos: ")
        for nombre,info in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Teléfono: {info["telefono"]}")
            print(f"Teléfono: {info["telefono"]}")
            print("-" * 20)
    else:
        print("La agenda aún está vacía, agrega a más amigos")


def agenda_contactos():
    agenda = {}

    while True:
        mostrar_menu()
        print("\n")
        opcion = input("Por favor elija una opción ")
        print("\n")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            eliminar_contacto(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            listar_contacto(agenda)
        elif opcion == "5":
            print("Saliendo de la agenda de contactos ¡Hasta pronto!")
            break
        else:
            print("Por favor selecciona una opción válida, selecciona una opción del 1 al 5")

agenda_contactos()