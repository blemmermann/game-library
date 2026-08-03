from juego import Juego # del archivo juego importa la clase Juego

class Usuario:
    def __init__(self, nombre):
        self.__nombre = nombre 
        self.__lista_juegos = [] 

    def get_nombre(self):
        return self.__nombre 

    def agregar_juego(self, nuevo_juego): 
        self.__lista_juegos.append(nuevo_juego) 
        print(f"Juego agregado con exito al perfil de {self.__nombre}")

    def mostrar_mis_juegos(self):
        print(f"--- Juegos de {self.__nombre} ---")
        if len(self.__lista_juegos) == 0:
            print("[Sin juegos registrados]")
        else:
            for juego in self.__lista_juegos:
                print(f"- {juego.get_titulo()} ({juego.get_plataforma()})")

    def buscar_juego(self, titulo_buscar):
        for juego in self.__lista_juegos: # Usamos el getter get_titulo() porque el atributo es privado
            if juego.get_titulo().upper() == titulo_buscar.upper():
                return True # El juego ya existe
        return False # El juego no existe

    def eliminar_juego(self, titulo_buscar):
        for i, juego in enumerate(self.__lista_juegos): # Usamos el getter porque __titulo es privado en la clase Juego
            if juego.get_titulo().upper() == titulo_buscar.upper():
                del self.__lista_juegos[i]
                return True # Se eliminó con éxito
        return False # No se encontró el juego

    def buscar_por_plataforma(self, plataforma_buscar):
        juegos_encontrados = []
        for juego in self.__lista_juegos:
            if juego.get_plataforma().upper() == plataforma_buscar.upper(): # Comparamos ignorando mayúsculas/minúsculas
                texto = f"{juego.get_titulo()} -- Dueño del perfil: {self.__nombre}" # Construimos el mismo texto anterior
                juegos_encontrados.append(texto)
        return juegos_encontrados