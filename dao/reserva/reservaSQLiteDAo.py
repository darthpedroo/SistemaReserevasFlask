from dao.reserva.reservaDAO import ReservaDao
import sqlite3
from core.reserva import Reserva


class ReservaSqliteDao(ReservaDao):
    def __init__(self, db_path) -> None:
        self.__db_path = db_path
        self.__crear__tabla()

    def __crear__tabla(self):
        with sqlite3.connect(self.__db_path) as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS reservas(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    sala TEXT NOT NULL,
                    usuario TEXT NOT NULL,
                    fecha DATE NOT NULL,
                    hora_inicio TIME NOT NULL,
                    hora_fin TIME NOT NULL,
                    FOREIGN KEY (sala) REFERENCES salas(nombre)
                )
                """
            )

    def get_all_reservas(self):
        with sqlite3.connect(self.__db_path) as conn:
            cursor = conn.execute(
                "SELECT sala,usuario,fecha,hora_inicio, hora_fin FROM reservas"
            )
            reservas = cursor.fetchall()
        return [
            Reserva(*reserva) for reserva in reservas
        ]

    def add_reserva(self, reserva: Reserva):
        with sqlite3.connect(self.__db_path) as conn:
            cursor = conn.execute(
                """INSERT INTO reservas (sala,usuario,fecha,hora_inicio,hora_fin)
	            VALUES (?,?,?,?,?);""", (str(reserva._reservable), str(reserva._usuario_reserva), str(reserva._fecha_reserva), str(reserva._hora_inicio_reserva), str(reserva._hora_fin_reserva))
            )
