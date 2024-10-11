import json
import os


class ConfigurationParser:
    DEFAULT_CONFIG_PATH = "config_json.json"

    def __init__(self, config_path=None) -> None:
        self.config_path = config_path or self.DEFAULT_CONFIG_PATH
        self.config = self.__load_configuration()
        self.types_of_db = ["sqlite", "json"]
        self.validate_configuration()

    def __load_configuration(self):
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(
                f"No se encontró el archivo de configuración en la ruta: {self.config_path}")
        with open(self.config_path, 'r') as config_file:
            return json.load(config_file)

    def validate_configuration(self):
        if self.get_backend_type() not in self.types_of_db:
            raise ValueError(
                "El tipo de backend configurado es invalido, debe ser tipo :", self.types_of_db)

    def get_backend_type(self):
        return self.config.get("backend_type")
