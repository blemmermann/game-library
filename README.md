# Biblioteca de Videojuegos

Backlog personal de PS4/PC, compartido con mi primo.

**Tecnologías:** Python 3
**Cómo ejecutar:** `python main.py`

## Versión 2 POO (Completada) 

El sistema fue refactorizado a Programación Orientada a Objetos (POO). Se separaron las entidades en módulos independientes (juego.py y usuario.py) y se implementó composición.

Próximo paso (V3): Implementar persistencia de datos leyendo y escribiendo archivos JSON.

## Versión 3 — Persistencia de Datos (Completada)
✔ Arquitectura POO consolidada (Biblioteca → Usuario → Juego)
✔ Carga automática y autoguardado de datos mediante `json`
✔ Exportación de reportes de inventario mediante `csv`
✔ `.gitignore` implementado para proteger datos locales

**Próximo paso (V4):** Migrar el almacenamiento a bases de datos relacionales con SQLite.
