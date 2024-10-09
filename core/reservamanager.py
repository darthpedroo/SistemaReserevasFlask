from core.reserva import Reserva
from core.reservableprogramado import Reservable
from core.fecha import Fecha
from core.tiempo import Hora
from core.exceptions import ReservableYaReservado, NoExisteLaReserva, ReservaPerteneceOtroUsuario
from dao.reserva.reservaSQLiteDAo import ReservaSqliteDao

# from core.sala import Sala

# from usuario import Usuario
DB_PATH = "./data/boiler.db"


class ReservaManager:

    def __init__(self) -> None:
        self._todas_las_reservas: list[Reserva] = []
        self._todas_las_salas = []

    @property
    def todas_las_reservas(self):
        return self._todas_las_reservas

    @property
    def todas_las_salas(self):
        return self._todas_las_salas

    def agregar_sala(self, sala: "Sala"):
        self._todas_las_salas.append(sala)

    def encontrar_sala_from_string(self, sala_str: str):
        for sala in self.todas_las_salas:
            if sala.nombre_eq_string(sala_str):
                return sala
        return None

    def load_salas(self, salas: list["Sala"]):
        """Toma una lista de salas y las carga self._todas_las_salas

        Args:
            salas (list[&quot;Sala&quot;]): _description_
        """

        for sala in salas:
            self._todas_las_salas.append(sala)

    def load_reservas(self, reservas: list[Reserva]):
        for reserva in reservas:
            self._todas_las_reservas.append(reserva)

    def get_reserva_by_id(self, id: int):
        try:
            return self._todas_las_reservas[id]
        except ValueError:
            raise NoExisteLaReserva

    def get_reservas_activas_dia_especifico(self, fecha: Fecha):
        """Obtiene la reserva de un dia específico"""
        reservas_dia_especifico = []
        for reserva in self._todas_las_reservas:
            if reserva.esta_reservada_para_la_fecha(fecha):
                reservas_dia_especifico.append(reserva)
        return reservas_dia_especifico

    def reserva_esta_ocupada(self, otra_reserva: Reserva):
        """Devuelve True si una reserva ya está ocupada en un dia especifico"""
        for reserva in self._todas_las_reservas:
            if otra_reserva.esta_en_el_intervalo_de(reserva):
                return True
            continue
        return False

    def __get_reserva_especifica(self, otra_reserva: Reserva):
        """Obtiene una reserva de un día especifico"""

        print("Todas las reseeeeerecaaas boeee", self._todas_las_reservas)
        for reserva in self._todas_las_reservas:
            if otra_reserva == reserva:
                return reserva
        return None

    def __borrar_reserva_especifica(self, reserva: Reserva):
        """Borra una reserva de un día especifico"""
        self._todas_las_reservas.remove(reserva)

    def crear_reserva(self, reservable: Reservable, usuario: "Usuario", fecha_reserva: Fecha, hora_inicio_reserva: Hora, hora_fin_reserva: Hora):
        """Crea una reserva"""

        # MEDIO TROLL PERO SI NO ESTÁ ESTO NO ANDA NADA
        reserva_dao = ReservaSqliteDao(DB_PATH)
        todas_las_reservas = reserva_dao.get_all_reservas()
        self.load_reservas(todas_las_reservas)
        # MEDIO TROLL PERO SI NO ESTÁ ESTO NO ANDA NADA

        reserva = Reserva(reservable, usuario, fecha_reserva,
                          hora_inicio_reserva, hora_fin_reserva)
        if self.reserva_esta_ocupada(reserva):
            raise ReservableYaReservado
        self._todas_las_reservas.append(reserva)
        print("Todas las reservas", self._todas_las_reservas)

    def cancelar_reserva(self, usuario: "Usuario", reserva: Reserva):
        """Cancela una reserva"""

        reserva_dao = ReservaSqliteDao(DB_PATH)
        todas_las_reservas = reserva_dao.get_all_reservas()
        self.load_reservas(todas_las_reservas)

        reserva = self.__get_reserva_especifica(reserva)

        if not reserva:
            raise NoExisteLaReserva
        if not reserva.es_el_mismo_usuario(usuario):
            raise ReservaPerteneceOtroUsuario

        self.__borrar_reserva_especifica(reserva)


class SingletonReservaManager(ReservaManager):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SingletonReservaManager, cls).__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self):
        if not self.__initialized:
            super().__init__()
            self.__initialized = True
