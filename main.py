from juego import Juego
from usuario import Usuario

biblioteca = []

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

    usuario_benjamin = Usuario("benjamin")
    usuario_primo = Usuario("primo")

    rdr2 = Juego("Red dead redemtion 2", "PS4", "yo", "digital", "jugando", 30)
    diablo = Juego("Diablo IV", "PC", "yo", "digital", "terminado", 100)
    infamous = Juego("Infamous second son", "PS4", "primo", "fisico", "pendiente", 0)

    usuario_benjamin.agregar_juego(rdr2)
    usuario_benjamin.agregar_juego(diablo)
    usuario_primo.agregar_juego(infamous)

    while True:
        menu()
        opcion = leer_opcion(1,6)
        if opcion == 1:
            plataforma = input("Ingrese el nombre de la plataforma a buscar: ").strip().upper()
            
            lista_benjamin = usuario_benjamin.buscar_por_plataforma(plataforma) # Cada objeto/instancia busca en su propia lista privada
            lista_primo = usuario_primo.buscar_por_plataforma(plataforma)
            
            lista_total = lista_benjamin + lista_primo # Unimos los resultados de todos los perfiles
            
            if len(lista_total) == 0:
                print(f"No hay juegos para esta plataforma") 
            else:
                print(f"\nJuegos encontrados en {plataforma}")
                for resultado in lista_total:
                    print(resultado)
                print("") # Un salto de línea estético
        elif opcion == 2:
            while True:
                usuario_elegido = input("Ingrese el usuario benjamin/primo: ").lower()
                if usuario_elegido in ["benjamin", "primo"]:
                    break
                print("Usuario no existe en el sistema")

            objeto_usuario = usuario_benjamin if usuario_elegido == "benjamin" else usuario_primo
            titulo = input("Ingrese el nombre del titulo a actualizar: ").strip()
            
            juego_encontrado = objeto_usuario.obtener_juego(titulo) # Pedimos el objeto al usuario

            if juego_encontrado:
                while True:
                    print("\n¿Que desea actualizar?")
                    print("1.- Horas Jugadas")
                    print("2.- Estado del Juego")
                    try:
                        option = int(input("Ingrese la opcion que desea: "))
                        
                        if option == 1:
                            try:
                                horas = int(input("Ingrese las horas adicionales: "))
                                if juego_encontrado.agregar_horas(horas): # Delegamos la actualización y validación directamente al objeto Juego
                                    print("Progreso de horas actualizado con éxito.")
                            except ValueError:
                                print("Solo debes ingresar datos numericos")
                            break
                            
                        elif option == 2:
                            nuevo_estado = input("Ingrese el estado (pendiente/jugando/terminado): ").lower()
                            if juego_encontrado.set_estado(nuevo_estado): # El setter set_estado() valida internamente si el string es correcto
                                print("Estado actualizado con éxito.")
                            break
                        else:
                            print("Ingresaste una opcion fuera de rango")
                    except ValueError:
                        print("Solo puedes ingresar datos numericos")
            else:
                print("El juego no existe en este perfil")
        elif opcion == 3:
            while True:
                usuario_elegido = input("Ingrese el usuario benjamin/primo: ").lower()
                if usuario_elegido != "benjamin" and usuario_elegido != "primo":
                    print("Usuario no existe en el sistema")
                else:
                    break
            
            objeto_usuario = usuario_benjamin if usuario_elegido == "benjamin" else usuario_primo # Determinamos cuál es el objeto contenedor objetivo
            proceso_activo = True
            
            if proceso_activo:
                titulo = input("Ingrese el titulo del videojuego a agregar: ").strip()
                if not validar_titulo(titulo):
                    print("Error el titulo no cumple con los requisitos. Proceso cancelado")
                    proceso_activo = False
                elif objeto_usuario.buscar_juego(titulo):
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
                nuevo_juego = Juego(titulo, plataforma, propietario, formato, estado, horas) # Instanciamos el objeto Juego
                objeto_usuario.agregar_juego(nuevo_juego) # Lo guardamos en el usuario mediante composición
        elif opcion == 4:
            while True:
                usuario_elegido = input("Ingrese el usuario benjamin/primo: ").lower()
                if usuario_elegido in ["benjamin", "primo"]:
                    break
                print("Usuario no existe en el sistema")

            objeto_usuario = usuario_benjamin if usuario_elegido == "benjamin" else usuario_primo # Determinamos cuál es el objeto contenedor objetivo
            titulo = input("Ingrese el titulo del juego a eliminar: ").strip()

            if objeto_usuario.eliminar_juego(titulo): # Le pedimos al objeto que intente eliminar el juego de su propia lista
                print("Juego eliminado con éxito.")
            else:
                print("El juego no existe en este perfil.")
        elif opcion == 5:
            print("\n========================================")
            print("      BIBLIOTECA ACTUAL DE JUEGOS       ")
            print("========================================")
            usuario_benjamin.mostrar_mis_juegos()
            print("-" * 40)
            usuario_primo.mostrar_mis_juegos()
            print("========================================\n")
        elif opcion == 6:
            print("Sistema de gestión finalizado.")
            break
if __name__ == "__main__":
    main()




