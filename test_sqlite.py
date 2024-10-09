import unittest
import tempfile
import os
from dao.reserva.reservaSQLiteDAo import ReservaSqliteDao
from core.reserva import Reserva
from core.sala import Sala
from core.usuario import Usuario
from core.fecha import Fecha,Ano,Dia,Mes
from core.tiempo import Tiempo, Hora,Minuto,Segundo


class TestReserva(unittest.TestCase):

    def setUp(self):
        self.temp_db = tempfile.NamedTemporaryFile(delete=False)
        self.reserva_dao = ReservaSqliteDao(self.temp_db.name)

    def tearDown(self):
        #self.temp_db.close()
        #os.remove(self.temp_db.name)
        pass

    def test_01_no_hay_reservas(self):
        self.assertEqual(len(self.reserva_dao.get_all_reservas()),0)
        
    def test_02_agregar_reserva(self):
        id = self.reserva_dao.count_reserva() + 1
        sala = Sala("Sala Porky", 10)
        usuario = Usuario("John POrk")
        fecha_reserva = Fecha(Ano(20224),Mes(10),Dia(10))
        hora_inicio = Tiempo(Hora(10),Minuto(10),Segundo(10))
        hora_fin = Tiempo(Hora(12),Minuto(23),Segundo(25))
        reserva = Reserva(id,sala,usuario,fecha_reserva,hora_inicio,hora_fin) 
        self.reserva_dao.add_reserva(reserva)
        
        self.assertEqual(len(self.reserva_dao.get_all_reservas()),1)

    def test_03_agregar_multiples_reservas(self):
        id = self.reserva_dao.count_reserva() + 1
        sala = Sala("Sala Porky", 10)
        usuario = Usuario("John POrk")
        fecha_reserva = Fecha(Ano(20224),Mes(10),Dia(10))
        hora_inicio = Tiempo(Hora(10),Minuto(10),Segundo(10))
        hora_fin = Tiempo(Hora(12),Minuto(23),Segundo(25))
        reserva = Reserva(id,sala,usuario,fecha_reserva,hora_inicio,hora_fin) 
        self.reserva_dao.add_reserva(reserva)
        
        id = self.reserva_dao.count_reserva() + 1
        sala = Sala("Sala Porky", 10)
        usuario = Usuario("John POrk")
        fecha_reserva = Fecha(Ano(1),Mes(10),Dia(10))
        hora_inicio = Tiempo(Hora(10),Minuto(10),Segundo(10))
        hora_fin = Tiempo(Hora(12),Minuto(23),Segundo(25))
        reserva = Reserva(id,sala,usuario,fecha_reserva,hora_inicio,hora_fin) 
        self.reserva_dao.add_reserva(reserva)
        
        id = self.reserva_dao.count_reserva() + 1
        sala = Sala("Sala Porky", 10)
        usuario = Usuario("John POrk")
        fecha_reserva = Fecha(Ano(3),Mes(10),Dia(10))
        hora_inicio = Tiempo(Hora(10),Minuto(10),Segundo(10))
        hora_fin = Tiempo(Hora(12),Minuto(23),Segundo(25))
        reserva = Reserva(id,sala,usuario,fecha_reserva,hora_inicio,hora_fin) 
        self.reserva_dao.add_reserva(reserva)
        
        self.assertEqual(len(self.reserva_dao.get_all_reservas()),3)
    
    def test_04_borrar_reserva(self):
        id = self.reserva_dao.count_reserva() + 1
        sala = Sala("Sala Porky", 10)
        usuario = Usuario("John POrk")
        fecha_reserva = Fecha(Ano(20224),Mes(10),Dia(10))
        hora_inicio = Tiempo(Hora(10),Minuto(10),Segundo(10))
        hora_fin = Tiempo(Hora(12),Minuto(23),Segundo(25))
        reserva = Reserva(id,sala,usuario,fecha_reserva,hora_inicio,hora_fin) 
        self.reserva_dao.add_reserva(reserva)
        self.reserva_dao.borrar_reserva(reserva)
        self.assertEqual(len(self.reserva_dao.get_all_reservas()),0)
if __name__ == "__main__":
    unittest.main()
