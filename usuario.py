from juego import Juego

class Usuario:
    def __init__(self, nombre):
        self.__nombre = nombre 
        self.__lista_juegos = [] 

    def get_nombre(self):
        return self.__nombre 

    def agregar_juego(self, nuevo_juego): 
        self.__lista_juegos.append(nuevo_juego) 
        # El print de confirmación se eliminó para evitar spam masivo durante la carga del JSON

    def mostrar_mis_juegos(self):
        print(f"--- Juegos de {self.__nombre} ---")
        if len(self.__lista_juegos) == 0:
            print("[Sin juegos registrados]")
        else:
            for juego in self.__lista_juegos:
                print(f"- {juego.get_titulo()} ({juego.get_plataforma()})")

    def buscar_juego(self, titulo_buscar):
        for juego in self.__lista_juegos:
            if juego.get_titulo().upper() == titulo_buscar.upper():
                return True
        return False

    def eliminar_juego(self, titulo_buscar):
        for i, juego in enumerate(self.__lista_juegos):
            if juego.get_titulo().upper() == titulo_buscar.upper():
                del self.__lista_juegos[i]
                return True 
        return False

    def buscar_por_plataforma(self, plataforma_buscar):
        juegos_encontrados = []
        for juego in self.__lista_juegos:
            if juego.get_plataforma().upper() == plataforma_buscar.upper():
                texto = f"{juego.get_titulo()} -- Propietario: {juego.get_propietario()}"
                juegos_encontrados.append(texto)
        return juegos_encontrados

    def obtener_juego(self, titulo_buscar):
        for juego in self.__lista_juegos:
            if juego.get_titulo().upper() == titulo_buscar.upper():
                return juego
        return None
        
    def to_dict(self):
        # Convierte el usuario y toda su lista de objetos Juego a diccionarios
        return {
            "nombre": self.__nombre,
            "juegos": [juego.to_dict() for juego in self.__lista_juegos]
        }