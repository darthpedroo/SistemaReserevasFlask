from dao.sala.salaDAO import SalaDao
from core.sala import Sala
import json
import os


class SalaJsonDao(SalaDao):
    def __init__(self, json_path) -> None:
        self.__json_path = json_path
        self.__crear__json()
    
    def __crear__json(self):
        try:
            if not os.path.exists(self.__json_path):
                sala_structure = {"salas": []}
                with open(self.__json_path, "w") as outfile:
                    json.dump(sala_structure, outfile)
        except ValueError:
            os.remove(self.__json_path)
            self.__crear__json()
    
    def get_all_salas(self):
        try:
            with open(self.__json_path, 'r') as data_file:
                data = json.load(data_file)
                return data
        except ValueError:
            os.remove(self.__json_path)
            self.__crear__json()
            return self.get_all_salas()
    
    def add_sala(self, sala: Sala):
        data = self.get_all_salas()
        
        new_sala = {
            "nombre": sala._nombre,
            "capacidad_maxima": sala._capacidad_maxima
        }
        data['salas'].append(new_sala)

        with open(self.__json_path, "w") as outfile:
            json.dump(data, outfile, indent=4)  # Use indent for pretty printing


