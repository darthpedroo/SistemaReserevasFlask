import os
import json


def crear_json_dao(json_path: str):
    if not os.path.exists(json_path):
        sala_structure = {"salas": [], "reservas": []}
        with open(json_path, "w") as outfile:
            json.dump(sala_structure, outfile)
