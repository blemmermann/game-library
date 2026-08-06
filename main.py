from juego import Juego
from usuario import Usuario
from biblioteca import Biblioteca # Importamos la nueva clase gestora

def menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Buscar juegos por plataforma")
    print("2. Actualizar progreso de juego (Horas / Estado)")
    print("3. Agregar nuevo juego")
    print("4. Eliminar juego")
    print("5. Ver biblioteca completa de juegos")
    print("6. Exportar inventario a CSV")
    print("7. Salir")
    print("=====================================")

def leer_opcion(min_val, max_val):
    try:
        opt = int(input("Ingrese la opcion deseada: "))
        if opt < min_val or opt > max_val:
            print(f"Debes ingresar una opcion dentro del rango ({min_val}-{max_val})")
            return None
        return opt
    except ValueError:
        print("Debes ingresar datos numericos")
        return None

# --- Funciones de validación (Se mantienen intactas) ---
def validar_titulo(titulo):
    return len(titulo) > 0

def validar_plataforma(plataforma):
    return plataforma.upper() in ["PS4", "PC"]

def validar_propietario(propietario):
    return propietario.lower() in ["yo", "primo"]

def validar_formato(formato):
    return formato.lower() in ["fisico", "digital"]

def validar_estado(estado): 
    return estado.lower() in ["pendiente", "jugando", "terminado"]
    
def validar_horas(horas):
    return horas >= 0

def main():
    # 1. Instanciamos la biblioteca. Al hacerlo, automáticamente intentará cargar el archivo JSON.
    mi_biblioteca = Biblioteca()
    
    # 2. Obtenemos el usuario activo (tú) para trabajar con él en el menú
    usuario_activo = mi_biblioteca.get_usuario_principal()

    print("¡Bienvenido al Gestor de Biblioteca de Videojuegos!")
    print(f"Datos cargados para el perfil: {usuario_activo.get_nombre()}")

    while True:
        menu()
        opcion = leer_opcion(1, 7)
        
        if opcion is None:
            continue

        if opcion == 1:
            plataforma = input("Ingrese el nombre de la plataforma a buscar (PS4/PC): ").strip().upper()
            lista_total = usuario_activo.buscar_por_plataforma(plataforma)

            if len(lista_total) == 0:
                print(f"No hay juegos para esta plataforma") 
            else:
                print(f"\nJuegos encontrados en {plataforma}:")
                for resultado in lista_total:
                    print(f"- {resultado}")
                    
        elif opcion == 2:
            titulo = input("Ingrese el nombre del titulo a actualizar: ").strip()
            juego_encontrado = usuario_activo.obtener_juego(titulo)

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
                                if juego_encontrado.agregar_horas(horas):
                                    print("Progreso de horas actualizado con éxito.")
                                    mi_biblioteca.guardar_datos() # ¡Guardamos el cambio!
                            except ValueError:
                                print("Solo debes ingresar datos numericos")
                            break
                            
                        elif option == 2:
                            nuevo_estado = input("Ingrese el estado (pendiente/jugando/terminado): ").lower()
                            if juego_encontrado.set_estado(nuevo_estado):
                                print("Estado actualizado con éxito.")
                                mi_biblioteca.guardar_datos() # ¡Guardamos el cambio!
                            break
                        else:
                            print("Ingresaste una opcion fuera de rango")
                    except ValueError:
                        print("Solo puedes ingresar datos numericos")
            else:
                print("El juego no existe en la biblioteca.")
                
        elif opcion == 3:
            proceso_activo = True
            
            titulo = input("Ingrese el titulo del videojuego a agregar: ").strip()
            if not validar_titulo(titulo):
                print("Error: El titulo no puede estar vacío. Proceso cancelado.")
                proceso_activo = False
            elif usuario_activo.buscar_juego(titulo):
                print("Error: El titulo ya existe en la colección.")
                proceso_activo = False
                    
            if proceso_activo:
                plataforma = input("Ingrese la plataforma del juego (PS4/PC): ").upper()
                if not validar_plataforma(plataforma):
                    print("Error: Plataforma inválida. Proceso cancelado.")
                    proceso_activo = False
                    
            if proceso_activo:
                propietario = input("Ingrese el propietario del juego (yo/primo): ").lower()
                if not validar_propietario(propietario):
                    print("Error: Propietario inválido. Proceso cancelado.")
                    proceso_activo = False
                    
            if proceso_activo:
                formato = input("Ingrese el formato del juego (fisico/digital): ").lower()
                if not validar_formato(formato):
                    print("Error: Formato inválido. Proceso cancelado.")
                    proceso_activo = False
                    
            if proceso_activo:
                estado = input("Ingrese el estado del juego (pendiente/jugando/terminado): ").lower()
                if not validar_estado(estado):
                    print("Error: Estado inválido. Proceso cancelado.")
                    proceso_activo = False
                    
            if proceso_activo: 
                try:
                    horas = int(input("Ingrese la cantidad de horas jugadas: "))
                    if not validar_horas(horas):
                        print("Error: Las horas deben ser 0 o más. Proceso cancelado.")
                        proceso_activo = False
                except ValueError:
                    print("Error: Debes ingresar datos numéricos para las horas.")
                    proceso_activo = False
                    
            if proceso_activo:
                nuevo_juego = Juego(titulo, plataforma, propietario, formato, estado, horas)
                usuario_activo.agregar_juego(nuevo_juego)
                print(f"Juego '{titulo}' agregado con éxito.") # El print que borramos de usuario.py lo ponemos aquí
                mi_biblioteca.guardar_datos() # ¡Guardamos el nuevo juego!
                
        elif opcion == 4:
            titulo = input("Ingrese el titulo del juego a eliminar: ").strip()

            if usuario_activo.eliminar_juego(titulo):
                print("Juego eliminado con éxito.")
                mi_biblioteca.guardar_datos() # ¡Guardamos la eliminación!
            else:
                print("El juego no existe en la biblioteca.")
                
        elif opcion == 5:
            print("\n========================================")
            print("      BIBLIOTECA ACTUAL DE JUEGOS       ")
            print("========================================")
            usuario_activo.mostrar_mis_juegos()
            print("========================================\n")
            
        elif opcion == 6:
            # Nueva opción para usar nuestro módulo CSV
            mi_biblioteca.exportar_csv()
            
        elif opcion == 7:
            print("Datos guardados. Sistema de gestión finalizado.")
            break

if __name__ == "__main__":
    main()