class Juego:
    def __init__(self, titulo, plataforma, propietario, formato, estado, horas):
        self.__titulo = titulo #self.titulo almacena el valor que tendrá titulo cuando se ejecute la asignación.
        self.__plataforma = plataforma #el doble "__" vuelve privados los atributos para no acceder a ellos
        self.__propietario = propietario #de manera externa, solo a traves de métodos
        self.__formato = formato
        self.__estado = estado.lower()
        self.__horas = horas 

    def detalles(self):
        print(f"Titulo: {self.__titulo}")
        print(f"Plataforma: {self.__plataforma}")
        print(f"Propietario: {self.__propietario}")
        print(f"Formato: {self.__formato}")
        print(f"Estado: {self.__estado}")
        print(f"Horas: {self.__horas}")

    def get_titulo(self):
        return self.__titulo #Obtiene o lee el valor del dato privado __titulo y lo devuelve.

    def get_plataforma(self):
        return self.__plataforma

    def get_propietario(self):
        return self.__propietario

    def get_formato(self):
        return self.__formato

    def get_estado(self):
        return self.__estado

    def get_horas(self):
        return self.__horas

    def set_estado(self, nuevo_estado):
        estado_limpio = nuevo_estado.lower() #Validamos y guardamos el estado estrictamente en minúsculas.
        if estado_limpio in ["pendiente", "jugando", "terminado"]:
            self.__estado = estado_limpio  # Asignación con '=' simple
            return True
            
        print(f"Error: '{nuevo_estado}' no es un estado válido.")
        return False

    def agregar_horas(self, horas_adicionales):
        if horas_adicionales > 0:
            self.__horas += horas_adicionales
            return True
        print("Error: Las horas adicionales deben ser mayores a 0.")
        return False

rdr2 = Juego("Red dead redemption 2", "PS4", "yo", "digital", "jugando", 30)

print(f"Titulo: {rdr2.get_titulo()}") #comprobamos el estado de los atributos a traves de getters
print(f"Plataforma: {rdr2.get_plataforma()}")
print(f"Propietario: {rdr2.get_propietario()}")
print(f"Formato: {rdr2.get_formato()}")
print(f"Estado: {rdr2.get_estado()}")
print(f"Horas: {rdr2.get_horas()} horas")

rdr2.set_estado("terminado")
rdr2.set_horas(100)

print(f"Estado: {rdr2.get_estado()}")
print(f"Horas: {rdr2.get_horas()} horas")

#hasta aqui es todo POO

def menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Buscar juegos por plataforma compartida")
    print("2. Actualizar progreso de juego (Horas / Estado)")
    print("3. Agregar nuevo juego a un perfil")
    print("4. Eliminar juego de un perfil ")
    print("5. Ver biblioteca completa de juegos")
    print("6. Salir")
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

def actualizar_juego(lista_juegos , titulo, modificacion, valor_nuevo): 
    for juego in lista_juegos: 
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

def eliminar_juego(lista_juegos, nombre_buscar):
    for i, juego in enumerate(lista_juegos): 
        if juego["titulo"].upper() == nombre_buscar.upper():
            del lista_juegos[i] 
            return True 
    return False 

def mostrar_biblioteca(diccionario_biblioteca):
    print("\n========================================")
    print("      BIBLIOTECA ACTUAL DE JUEGOS       ")
    print("========================================")
    for usuario, lista_juegos in diccionario_biblioteca.items(): 
        print("-" * 40)
        if len(lista_juegos) == 0: 
            print("[Sin juegos registrados]")
        else: 
            for i, juego in enumerate(lista_juegos, 1): 
                print(f"{i}. Título: {juego['titulo']}") 
                print(f"Plataforma: {juego['plataforma']} | Propietario: {juego['propietario']}") 
                print(f"Formato: {juego['formato']} | Estado: {juego['estado']}") 
                print(f"Horas Jugadas: {juego['horas']} hrs.") 
                print("  " + "." * 35)
                
    print("========================================\n")

def main():
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
    while True:
        menu()
        opcion = leer_opcion(1,6)
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
                    horas = int(input("Ingrese la cantidad de horas jugadas: "))
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
            while True:
                usuario = input("Ingrese el usuario benjamin/primo: ").lower()
                if usuario != "benjamin" and usuario != "primo":
                    print("Usuario no existe en el sistema")
                else:
                    break
            titulo = input("Ingrese el titulo del juego: ").upper()
            if buscar_juego(biblioteca[usuario], titulo):
                eliminar_juego(biblioteca[usuario], titulo)
                print( "Juego eliminado")
            else:
                print("El juego no existe")
        elif opcion == 5:
            mostrar_biblioteca(biblioteca)
        elif opcion == 6:
            print("Sistema de gestión finalizado.")
            break
if __name__ == "__main__":
    main()




