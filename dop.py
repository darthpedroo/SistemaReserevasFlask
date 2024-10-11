from dao.sala.salaDaoFactory import SalaDaoFactory
from dao.config.configurationparser import ConfigurationParser


configuration_parser = ConfigurationParser()
sf = SalaDaoFactory()

print(sf.create_dao(configuration_parser))
