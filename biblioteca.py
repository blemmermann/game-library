import json
import csv
from usuario import Usuario
from juego import Juego

class Biblioteca:
    def __init__(self):
        self.__usuarios = []
        self.__archivo_datos = "datos_biblioteca.json"
        
        # Estado base: te creas a ti mismo por defecto
        self.__usuario_principal = Usuario("benjamin")
        self.__usuarios.append(self.__usuario_principal)
        
        # Apenas nace la biblioteca, intenta cargar el JSON para reemplazar el estado base
        self.cargar_datos()

    def get_usuario_principal(self):
        return self.__usuario_principal

    def cargar_datos(self):
        try:
            # Intentamos leer el archivo en modo lectura ("r")
            with open(self.__archivo_datos, "r") as archivo:
                datos_importados = json.load(archivo)
                
                # Vaciamos la lista por defecto para no duplicar si el JSON trae datos
                self.__usuarios = [] 
                
                # Reconstruimos los objetos desde los diccionarios del JSON
                for data_usuario in datos_importados:
                    nuevo_usuario = Usuario(data_usuario["nombre"])
                    
                    for data_juego in data_usuario["juegos"]:
                        # Usamos los datos del diccionario para instanciar el Juego
                        nuevo_juego = Juego(
                            data_juego["titulo"],
                            data_juego["plataforma"],
                            data_juego["propietario"],
                            data_juego["formato"],
                            data_juego["estado"],
                            data_juego["horas"]
                        )
                        nuevo_usuario.agregar_juego(nuevo_juego)
                        
                    self.__usuarios.append(nuevo_usuario)
                    
                # Actualizamos el puntero para que main.py sepa quién es el usuario activo
                if len(self.__usuarios) > 0:
                    self.__usuario_principal = self.__usuarios[0]
                    
        except FileNotFoundError:
            # El archivo no existe (primera ejecución). Seguimos con el usuario por defecto sin lanzar error.
            pass

    def guardar_datos(self):
        # Convertimos todos los objetos de la lista en diccionarios puros gracias a to_dict()
        datos_exportar = [usuario.to_dict() for usuario in self.__usuarios]
        
        # Abrimos en modo escritura ("w") para sobreescribir el archivo con la lista actualizada
        with open(self.__archivo_datos, "w") as archivo:
            json.dump(datos_exportar, archivo, indent=4)

    def exportar_csv(self):
        # Genera el reporte extra en CSV
        with open("reporte_juegos.csv", "w", newline="") as archivo_csv:
            escritor = csv.writer(archivo_csv)
            # Fila 1: Encabezados limpios y precisos
            escritor.writerow(["Perfil", "Titulo", "Plataforma", "Propietario", "Formato", "Estado", "Horas"])
            
            # Recorremos la biblioteca usando los diccionarios para facilitar el acceso
            for usuario in self.__usuarios:
                datos_usuario = usuario.to_dict()
                for j in datos_usuario["juegos"]:
                    escritor.writerow([
                        datos_usuario["nombre"],
                        j["titulo"], 
                        j["plataforma"], 
                        j["propietario"], 
                        j["formato"], 
                        j["estado"], 
                        j["horas"]
                    ])
        print("Reporte CSV generado exitosamente como 'reporte_juegos.csv'.")