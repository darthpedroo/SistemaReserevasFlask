from core.fecha import Fecha
from core.tiempo import Tiempo
from core.usuario import Usuario
from core.reservableprogramado import ReservableProgramado
from core.reservamanager import SingletonReservaManager

DB_PATH = "./data/boiler.db"

class Sala(ReservableProgramado): #UNA SALA ES UNA SALA. UNA SALA NO DEBE TENER HORARIO. 
    def __init__(self,nombre:str, capacidad_maxima:int):
        self._nombre = nombre #Hacer un super de esto
        self._capacidad_maxima = capacidad_maxima

    def __str__(self) -> str:
        return self._nombre

    @property
    def capacidad_maxima(self):
        return self._capacidad_maxima

    def __eq__(self, otra_sala: "Sala"):
        return self._nombre == otra_sala._nombre

    def nombre_eq_string(self, nombre:str):
        return self._nombre == nombre

    def usuario_me_realizo_una_reserva(self,index:int, usuario:Usuario, fecha_reserva:Fecha, hora_inicio_reserva: Tiempo, hora_fin_reserva: Tiempo):
        """Delega a SingletonReservaManager la creación de una sala"""
        reserva_manager = SingletonReservaManager()
        reserva_manager.crear_reserva(self, index,
                                      usuario,fecha_reserva,hora_inicio_reserva,hora_fin_reserva)
        return reserva_manager

    def usuario_me_cancelo_una_reserva(self,usuario: Usuario, reserva: "Reserva", reserva_manager):
        reserva_manager = SingletonReservaManager()
        print("len()", reserva_manager.cantidad_reservas())
        return reserva_manager.cancelar_reserva(usuario, reserva)
