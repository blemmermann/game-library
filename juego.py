class Juego:
    def __init__(self, titulo, plataforma, propietario, formato, estado, horas):
        self.__titulo = titulo 
        self.__plataforma = plataforma 
        self.__propietario = propietario 
        self.__formato = formato
        self.__estado = estado.lower()
        self.__horas = horas 

    def get_titulo(self):
        return self.__titulo 

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
        estado_limpio = nuevo_estado.lower() 
        if estado_limpio in ["pendiente", "jugando", "terminado"]:
            self.__estado = estado_limpio  
            return True
            
        print(f"Error: '{nuevo_estado}' no es un estado válido.")
        return False

    def agregar_horas(self, horas_adicionales):
        if horas_adicionales > 0:
            self.__horas += horas_adicionales
            return True
        print("Error: Las horas adicionales deben ser mayores a 0.")
        return False

    def to_dict(self):
        return {
            "titulo": self.__titulo,
            "plataforma": self.__plataforma,
            "propietario": self.__propietario,
            "formato": self.__formato,
            "estado": self.__estado,
            "horas": self.__horas
        }

if __name__ == "__main__":
    rdr2 = Juego("Red dead redemption 2", "PS4", "yo", "digital", "jugando", 30)

    print(f"Titulo: {rdr2.get_titulo()}") 
    print(f"Plataforma: {rdr2.get_plataforma()}")
    print(f"Propietario: {rdr2.get_propietario()}")
    print(f"Formato: {rdr2.get_formato()}")
    print(f"Estado: {rdr2.get_estado()}")
    print(f"Horas: {rdr2.get_horas()} horas")

    rdr2.set_estado("terminado")
    rdr2.agregar_horas(100)

    print(f"Estado: {rdr2.get_estado()}")
    print(f"Horas: {rdr2.get_horas()} horas")

