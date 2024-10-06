from dao.sala.salaDAO import SalaDao
import sqlite3
from core.sala import Sala

class SalaSqliteDao(SalaDao):
    def __init__(self, db_path) -> None:
        self.__db_path = db_path
        self.__crear__tabla()
    
    def __crear__tabla(self):
        with sqlite3.connect(self.__db_path) as conn:
            conn.execute(
            """
            CREATE TABLE IF NOT EXISTS salas(
            nombre TEXT PRIMARY KEY,
            capacidad_maxima INTEGER NOT NULL
            )
            """
            )

    def get_all_salas(self):
        with sqlite3.connect(self.__db_path) as conn:
            cursor = conn.execute(
                "SELECT * FROM salas"
            )
            salas = cursor.fetchall()
        return [
            Sala(*sala) for sala in salas
        ]

    def add_sala(self, sala: Sala):
        with sqlite3.connect(self.__db_path) as conn:
            cursor = conn.execute(
                """INSERT INTO salas (nombre,capacidad_maxima)
	            VALUES (?,?);""",(str(sala), sala.capacidad_maxima)
            )

