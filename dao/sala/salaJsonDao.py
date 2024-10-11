from dao.sala.salaDAO import SalaDao
from core.sala import Sala
import json
import os
from dao.helpers import crear_json_dao


class SalaJsonDao(SalaDao):
    def __init__(self, json_path) -> None:
        self.__json_path = json_path
        self.__crear__json()

    def __crear__json(self):
        try:
            crear_json_dao(self.__json_path)
        except ValueError:
            os.remove(self.__json_path)
            self.__crear__json()

    def __get_all_salas_json(self):
        try:
            with open(self.__json_path, 'r') as data_file:
                data = json.load(data_file)
                return data
        except ValueError:
            os.remove(self.__json_path)
            self.__crear__json()
            return self.__get_all_salas_json()

    def get_all_salas(self):
        try:
            with open(self.__json_path, 'r') as data_file:
                data = json.load(data_file)
                salas = []
                for sala in data['salas']:
                    salas.append(
                        Sala(sala.get("nombre"), sala.get("capacidad_maxima")))
                return salas

        except ValueError:
            os.remove(self.__json_path)
            self.__crear__json()
            return self.get_all_salas()

    def add_sala(self, sala: Sala):
        data = self.__get_all_salas_json()

        new_sala = {
            "nombre": sala._nombre,
            "capacidad_maxima": sala._capacidad_maxima
        }
        data['salas'].append(new_sala)

        with open(self.__json_path, "w") as outfile:
            json.dump(data, outfile, indent=4)
