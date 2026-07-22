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
            pass
        elif opcion == 2:
            pass
        elif opcion == 2:
            pass
        elif opcion == 5:
            print("Sistema de gestión finalizado.")
            break

if __name__ == "__main__":
    main()




