from core.fecha import Fecha
from core.tiempo import Tiempo
from core.usuario import Usuario
from core.reservableprogramado import ReservableProgramado
from core.reservamanager import SingletonReservaManager

class Sala(ReservableProgramado): #UNA SALA ES UNA SALA. UNA SALA NO DEBE TENER HORARIO. 
    def __init__(self,nombre:str, capacidad_maxima:int):
        self._nombre = nombre #Hacer un super de esto
        self._capacidad_maxima = capacidad_maxima

    def __str__(self) -> str:
        return self._nombre

    def usuario_me_realizo_una_reserva(self,usuario:Usuario, fecha_reserva:Fecha, hora_inicio_reserva: Tiempo, hora_fin_reserva: Tiempo):
        """Delega a SingletonReservaManager la creación de una sala"""
        reserva_manager = SingletonReservaManager()
        reserva_manager.crear_reserva(self,
                                      usuario,fecha_reserva,hora_inicio_reserva,hora_fin_reserva)
        return reserva_manager

