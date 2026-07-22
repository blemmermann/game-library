#biblioteca {"usuario": ["titulo", "plataforma, "propietario", "formato", "estado, "horas]}

biblioteca = { 
"benjamin": [ 
{"titulo": "Red Dead Redemption 2", "plataforma": "PS4", "propietario": "yo", "formato": "fisico", 
"estado": "jugando", "horas": 120}, 
{"titulo": "Diablo 4", "plataforma": "PC", "propietario": "yo", "formato": "digital", "estado": 
"terminado", "horas": 300} 
    ], 
"primo": [ 
{"titulo": "Infamous 2", "plataforma": "PS4", "propietario": "primo", "formato": "fisico", "estado": 
"pendiente", "horas": 0} 
    ] 
        } 


def menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Buscar juegos por plataforma compartida")
    print("2. Actualizar progreso de juego (Horas / Estado)")
    print("3. Agregar nuevo juego a un perfil")
    print("4. Eliminar juego de un perfil ")
    print("5. Salir")
    print("=====================================")

def leer_opcion(min , max):
    try:
        opt = int(input("Ingrese la opcion deseada: "))
        if opt < min or opt > max:
            print("Debes ingresar una opcion dentro del rango")
        else:
            return opt
    except ValueError:
        print("Debes ingresar datos numericos")

def buscar_juego(lista_juegos, titulo): 
    for juego in lista_juegos: 
        if juego["titulo"].upper() == titulo.upper(): 
            return True 
    else:
        return False

def buscar_plataforma(biblioteca, plataforma):
    lista = []
    for clave, valor in biblioteca.items(): 
        usuario = clave
        lista_juegos = valor 
        for juego in lista_juegos:
            if juego["plataforma"].upper() == plataforma.upper():
                titulo = juego["titulo"]
                lista.append(f"{titulo} -- Dueño del perfil: {usuario}")
    return lista

def actualizar_juego(lista_juegos , titulo, modificacion, valor_nuevo): #lista_juegos siempre sera remplasada por biblioteca[usuario]
    for juego in lista_juegos: #la recorremos completa
        if juego["titulo"].upper() == titulo.upper():
            if modificacion == "horas":
                juego["horas"] += valor_nuevo
            elif modificacion == "estado":
                juego["estado"] = valor_nuevo
            return True
    return False 

def agregar_juego(lista_juegos, titulo, plataforma, propietario, formato, estado, horas):
    nuevo_juego = {
                    "titulo" : titulo,
                    "plataforma" : plataforma,
                    "propietario" : propietario,
                    "formato" : formato,
                    "estado" : estado,
                    "horas" : horas
        }
    lista_juegos.append(nuevo_juego) 
    return True

def validar_titulo(titulo):
    if len(titulo) == 0:
        return False
    else:
        return True

def validar_plataforma(plataforma):
    if plataforma.upper() == "PS4" or plataforma.upper() == "PC":
        return True
    else:
        return False

def validar_propietario(propietario):
    if propietario.lower() == "yo" or propietario.lower() == "primo":
        return True
    else:
        return False

def validar_formato(formato):
    if formato.lower() == "fisico" or formato.lower() == "digital":
        return True
    else:
        return False

def validar_estado(estado): 
    if estado.lower() == "pendiente" or estado.lower() == "jugando" or estado.lower() == "terminado":
        return True
    else:
        return False
    
def validar_horas(horas):
    if horas >= 0:
        return True
    else:
        return False

def main():

    #aca va el diccionario de ejemplo

    while True:
        menu()

        opcion = leer_opcion(1,5)
        if opcion == 1:
            plataforma = input("Ingrese el nombre de la plataforma a buscar: ")
            lista = buscar_plataforma(biblioteca, plataforma)
            if len(lista) == 0:
                print("No hay juegos para esta plataforma") 
            else:
                print(f"Juegos encontrados en {plataforma}")
                for i in lista:
                    print(i)
        elif opcion == 2:
            while True:
                usuario = input("Ingrese el usuario benjamin/primo: ").lower()
                if usuario != "benjamin" and usuario != "primo":
                    print("Usuario no existe en el sistema")
                else:
                    break
            titulo = input("Ingrese el nombre del titulo a actualizar: ")
            validacion = buscar_juego(biblioteca[usuario], titulo)
            if validacion:
                while True:
                    print("¿Que desea actualizar?")
                    print("1.- Horas Jugadas")
                    print("2.- Estado del Juego")
                    try:
                        option = int(input("Ingrese la opcion que desea: "))
                        if option == 1:
                            while True:
                                try:
                                    horas = int(input("Ingrese las horas adicionales: "))
                                    if horas < 0:
                                        print("Debes ingresar un entero positivo")
                                    else:
                                        if actualizar_juego(biblioteca[usuario], titulo, "horas", horas):
                                            print("Progreso actualizado con éxito.")
                                        break
                                except ValueError:
                                    print("Solo debes ingresar datos numericos")
                            break
                        elif option == 2:
                            while True:
                                estado = input("Ingrese la actualizacion de estado del juego: pendiente/jugando/terminado: ").lower()
                                if estado == "pendiente" or estado == "jugando" or estado == "terminado":
                                    if actualizar_juego(biblioteca[usuario], titulo, "estado", estado):
                                        print("Progreso actualizado con éxito.")
                                        break
                                else:
                                    print("Solo puedes ingresar pendiente/jugando/terminado")
                            break
                        else:
                            print("Ingresaste una opcion fuera de rango")
                    except ValueError:
                        print("Solo puedes ingresar datos numericos")
            else:
                print("El juego no existe en este perfil")
        elif opcion == 3:
            while True:
                usuario = input("Ingrese el usuario benjamin/primo: ").lower()
                if usuario != "benjamin" and usuario != "primo":
                    print("Usuario no existe en el sistema")
                else:
                    break
            proceso_activo = True
            if proceso_activo:
                titulo = input("Ingrese el titulo del videojuego a agregar: ").strip()
                validacion = validar_titulo(titulo)
                if not validacion:
                    print("Error el titulo no cumple con los requisitos. Proceso cancelado")
                    proceso_activo = False
                else:
                    if buscar_juego(biblioteca[usuario], titulo):
                        print("Error: el titulo ya existe en la coleccion de juegos")
                        proceso_activo = False
            if proceso_activo:
                plataforma = input("Ingrese la plataforma del juego PS4/PC: ").upper()
                if not validar_plataforma(plataforma):
                    print("Error la plataforma no cumple con los requisitos. Proceso cancelado")
                    proceso_activo = False
            if proceso_activo:
                propietario = input("Ingrese el propietario del juego yo/primo: ").lower()
                if not validar_propietario(propietario):
                    print("Error el propietario no cumple con los requisitos. Proceso cancelado")
                    proceso_activo = False
            if proceso_activo:
                formato = input("Ingrese el formato del juego fisico/digital: ").lower()
                if not validar_formato(formato):
                    print("Error el formato no cumple con los requisitos. Proceso cancelado")
                    proceso_activo = False
            if proceso_activo:
                estado = input("Ingrese el estado del juego pendiente/jugando/terminado: ").lower()
                if not validar_estado(estado):
                    print("Error el estado no cumple con los requisitos. Proceso cancelado")
                    proceso_activo = False
            if proceso_activo: 
                try:
                    horas = int(input("Ingrese la cantidad de horas del juego: "))
                    if not validar_horas(horas):
                        print("Error las horas no cumplen con los requisitos. Proceso cancelado")
                        proceso_activo = False
                except ValueError:
                    print("Debes ingresar datos numericos")
                    proceso_activo = False
            if proceso_activo:
                agregar_juego(biblioteca[usuario], titulo, plataforma, propietario, formato, estado, horas)
                print("Juego agregado")
        elif opcion == 4:
            pass
        elif opcion == 5:
            print("Sistema de gestión finalizado.")
            break

if __name__ == "__main__":
    main()




