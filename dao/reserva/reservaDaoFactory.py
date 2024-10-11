from dao.config.configurationparser import ConfigurationParser
from dao.reserva.reservaSQLiteDAo import ReservaSqliteDao
from dao.reserva.reservaJsonDao import ReservaJsonDao


class ReservaDaoFactory:
    @staticmethod
    def create_dao(configuration_parser: ConfigurationParser, db_path: str):
        backend_type = configuration_parser.get_backend_type()
        if backend_type == "json":
            return ReservaJsonDao(db_path)
        elif backend_type == "sqlite":
            return ReservaSqliteDao(db_path)
        else:
            raise ValueError("Tipo de backend not supported ")
