"""Módulo que contiene el DAO para la Reserva"""

import sqlite3


class ReservaDAO:
    """Data Access Object (DAO) para manejar las reservas de las salas."""

    def __init__(self, db_path):
        """Inicializa el DAO y crea la tabla si no existe."""
        self.__db_path = db_path
        self.__crear_tabla()

    def __crear_tabla(self):
        with sqlite3.connect(self.__db_path) as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS reservas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    FOREIGN KEY (sala_nombre) REFERENCES salas(nombre),
                    fecha_reserva TEXT,
                    hora_inicio TEXT,
                    hora_fin TEXT, 
                )"""
            )

    def agregar_reserva(self, nombre_sala: str, reserva: "Reserva"):
        """
        Agrega una reserva a la base de datos.

        Args:
            nombre_sala (str): Nombre de la sala.
            reserva (Reserva): Reserva a agregar.
        """
        with sqlite3.connect(self.__db_path) as conn:
            conn.execute(
                "INSERT INTO reservas (sala_nombre, inicio, fin) VALUES (?, ?, ?)",
                (nombre_sala, str(reserva.inicio), str(reserva.fin)),
            )

    def listar_reservas(self, sala_nombre: str) -> list["Reserva"]:
        """
        Recupera todas las reservas de una sala almacenadas en la base de datos.

        Args:
            sala_nombre (str): Nombre de la sala.
        """
        with sqlite3.connect(self.__db_path) as conn:
            cursor = conn.execute(
                "SELECT inicio, fin FROM reservas WHERE sala_nombre = ?",
                (sala_nombre,),
            )
            reservas = cursor.fetchall()

        return [
            Reserva(inicio=dt.from_string(row[0]), fin=dt.from_string(row[1])) for row in reservas
        ]

    def eliminar_reserva(self, nombre_sala: str, reserva: "Reserva"):
        """
        Elimina una reserva de la base de datos.

        Args:
            nombre_sala (str): Nombre de la sala.
            reserva (Reserva): Reserva a eliminar.
        """
        # ????
