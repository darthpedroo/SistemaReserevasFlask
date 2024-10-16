from dao.reserva.reservaDAO import ReservaDao
import json
import os
from dao.helpers import crear_json_dao
from core.reserva import Reserva
from core.usuario import Usuario
from core.sala import Sala
from core.helpers import parse_fecha, parse_hora



class ReservaJsonDao(ReservaDao):
    def __init__(self, json_path: str) -> None:
        self.__json_path = json_path
        self.__crear__json()

    def __crear__json(self):
        try:
            crear_json_dao(self.__json_path)
        except ValueError:
            os.remove(self.__json_path)
            self.__crear__json()

    def get_reserva(self, reserva_id: int):
        for reserva in self.__get_all_reservas_json():
            if reserva['id'] == reserva_id:
                return reserva
            continue

    def get_all_reservas(self):
        try:
            with open(self.__json_path, 'r') as data_file:
                data = json.load(data_file)
                reservas = []
                for reserva in data['reservas']:
                    reservas.append(Reserva(reserva.get("id"), Sala(reserva.get(
                        "sala"),10), Usuario(reserva.get("usuario")), parse_fecha(reserva.get("fecha")), parse_hora(reserva.get("hora_inicio")), parse_hora(reserva.get("hora_fin"))))
                return reservas
        except ValueError:
            os.remove(self.__json_path)
            self.__crear__json()
            return self.get_all_reservas()

    def __get_all_reservas_json(self):
        try:
            with open(self.__json_path, 'r') as data_file:
                data = json.load(data_file)
                return data
        except ValueError:
            os.remove(self.__json_path)
            self.__crear__json()
            return self.__get_all_reservas_json()

    def add_reserva(self, reserva: "Reserva"):

        data = self.__get_all_reservas_json()
        new_reserva = {
            "id": reserva._id,
            "sala": reserva._reservable._nombre,
            "usuario": reserva._usuario_reserva.nombre,
            "fecha": str(reserva._fecha_reserva),
            "hora_inicio": str(reserva._hora_inicio_reserva),
            "hora_fin": str(reserva._hora_fin_reserva)
        }
        data['reservas'].append(new_reserva)

        with open(self.__json_path, "w") as outfile:
            json.dump(data, outfile, indent=4)

    def borrar_reserva(self, current_reserva: "Reserva"):
        print("todas las reservas: ", self.__get_all_reservas_json()['reservas'])
        for reserva in self.__get_all_reservas_json()['reservas']:
            if reserva["id"] == current_reserva._id[0]:  
                data = self.__get_all_reservas_json()
                data['reservas'].remove(reserva)  
                with open(self.__json_path, "w") as outfile:
                    json.dump(data, outfile, indent=4)
                break
