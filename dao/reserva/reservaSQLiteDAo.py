from dao.sala.salaDAO import SalaDao
import sqlite3
from core.reserva import Reserva

class SalaSqliteDao(SalaDao):
    def __init__(self, db_path) -> None:
        self.__db_path = db_path
        self.__crear__tabla()
    
    def __crear__tabla(self):
        with sqlite3.connect(self.__db_path) as conn:
            conn.execute(
            """
            CREATE TABLE IF NOT EXISTS reservas(
            )
            """
            )

    def get_all_reservas(self):
        with sqlite3.connect(self.__db_path) as conn:
            cursor = conn.execute(
                "SELECT * FROM reservas"
            )
            salas = cursor.fetchall()
        return [
            Reserva(*sala) for sala in salas
        ]

    def add_sala(self, sala: Reserva):
        with sqlite3.connect(self.__db_path) as conn:
            cursor = conn.execute(

            )

