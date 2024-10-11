from core.reservableprogramado import ReservableProgramado, ReservableSinHora, Reservable
# from core.reservamanager import SingletonReservaManager
from core.reserva import Reserva
from core.fecha import Fecha
from core.tiempo import Tiempo


class Usuario:
    def __init__(self, nombre) -> None:
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    def __eq__(self, value: "Usuario") -> bool:
        if not isinstance(value, Usuario):
            raise NotImplementedError
        return self.__nombre == value.__nombre

    def __str__(self) -> str:
        return self.__nombre

    def realizar_reserva_programada(self, index: int, reservable_programado: ReservableProgramado, fecha_reserva: Fecha, hora_inicio_reserva: Tiempo, hora_fin_reserva: Tiempo):
        """Realiza una reserva del Tipo ReservableProgramado"""
        return reservable_programado.usuario_me_realizo_una_reserva(self, index, fecha_reserva, hora_inicio_reserva, hora_fin_reserva)

    def cancelar_reserva_programada(self, reserva: Reserva, reserva_manager):
        "Cancela una Reserva"

        reserva._reservable.usuario_me_cancelo_una_reserva(
            self, reserva, reserva_manager)
