from dao.config.configurationparser import ConfigurationParser
from dao.sala.salaJsonDao import SalaJsonDao
from dao.sala.salaSQLiteDao import SalaSqliteDao


class SalaDaoFactory:
    @staticmethod
    def create_dao(configuration_parser: ConfigurationParser, db_path: str):
        backend_type = configuration_parser.get_backend_type()
        if backend_type == "json":
            return SalaJsonDao(db_path)
        elif backend_type == "sqlite":
            return SalaSqliteDao(db_path)
        else:
            raise ValueError("Tipo de backend not supported ")
