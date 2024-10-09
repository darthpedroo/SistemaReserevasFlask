import unittest
import tempfile
import os
from dao.sala.salaJsonDao import SalaJsonDao
from core.sala import Sala


class TestReserva(unittest.TestCase):

    def setUp(self):
        self.sala_json_dao = SalaJsonDao("./data/sala_json.json")


    def test_01_add_sala(self):
        sala = Sala("Nombre_sala:V", 10)
        self.sala_json_dao.add_sala(sala)
        self.assertEqual(len(self.sala_json_dao.get_all_salas()),1)
        
    
if __name__ == "__main__":
    unittest.main()
