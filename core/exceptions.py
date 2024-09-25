class ReservableYaReservado(Exception):
    def __init__(self):
        super().__init__("El Reservable ya ha sido reservado para la fecha y horario indicados")

class NoExisteLaReserva(Exception):
    def __init__(self):
        super().__init__("La Reserva No Existe")

class ReservaPerteneceOtroUsuario(Exception):
    def __init__(self):
        super().__init__("La Reserva Pertenece a otro usuario")

class NumeroMenorAZero(Exception):
    def __init__(self):
        super().__init__("Numero es Menor A Cero")

class HoraDeInicioDebeSerMenorAHoraFinal(Exception):
    def __init__(self):
        super().__init__("La hora de inicio debe ser mayor a la hora final")

class FechaInvalida(Exception):
    def __init__(self):
        super().__init__("La Fecha es invalida")