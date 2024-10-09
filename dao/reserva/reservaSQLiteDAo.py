from dao.reserva.reservaDAO import ReservaDao
import sqlite3
from core.reserva import Reserva
from core.usuario import Usuario
from core.sala import Sala
from core.helpers import parse_fecha, parse_hora


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
                "SELECT id, sala,usuario,fecha,hora_inicio, hora_fin FROM reservas"
            )
            reservas = cursor.fetchall()
            
            all_reservas = []
            for reserva in reservas:
                id_reserva, sala, usuario_nombre, fecha, hora_inicio, hora_fin = reserva

                new_fecha = parse_fecha(fecha)
                new_hora_inicio = parse_hora(hora_inicio)
                new_hora_fin = parse_hora(hora_fin)
                
                all_reservas.append(Reserva(id_reserva, Sala(sala,10), Usuario(usuario_nombre), new_fecha, new_hora_inicio, new_hora_fin))
            return all_reservas


    def add_reserva(self, reserva: Reserva):
        
        with sqlite3.connect(self.__db_path) as conn:
            cursor = conn.execute(
                """INSERT INTO reservas (sala,usuario,fecha,hora_inicio,hora_fin)
	            VALUES (?,?,?,?,?);""", (str(reserva._reservable), str(reserva._usuario_reserva), str(reserva._fecha_reserva), str(reserva._hora_inicio_reserva), str(reserva._hora_fin_reserva))
            )
    
    def borrar_reserva(self, reserva: Reserva):
        
        with sqlite3.connect(self.__db_path) as conn:
            cursor = conn.execute(
                """DELETE FROM reservas
                WHERE id=?;""", 
                (reserva._id)
            )
            conn.commit()  

    def count_reserva(self):
        with sqlite3.connect(self.__db_path) as conn:
            cursor = conn.execute(
                """SELECT COUNT(id)
                FROM reservas;
                        """
            )
            count = cursor.fetchone()[0]  
            return count


        
        
        


