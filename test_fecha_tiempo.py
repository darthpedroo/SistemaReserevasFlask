from core.exceptions import NumeroMenorAZero, HoraDeInicioDebeSerMenorAHoraFinal
from core.fecha import *
from core.tiempo import *

import unittest

class TestFechaTiempo(unittest.TestCase):
    
    def test_01_ano_menor_a_cero(self):
        with self.assertRaises(FechaInvalida):
            Ano(-1)

    def test_02_mes_fuera_de_rango(self):
        with self.assertRaises(FechaInvalida):
            Mes(13)

    def test_03_mes_menor_a_uno(self):
        with self.assertRaises(FechaInvalida):
            Mes(0)

    def test_04_dia_fuera_de_rango(self):
        with self.assertRaises(FechaInvalida):
            Dia(32)

    def test_05_hora_fuera_de_rango(self):
        with self.assertRaises(FechaInvalida):
            Hora(25)

    def test_06_hora_menor_a_cero(self):
        with self.assertRaises(FechaInvalida):
            Hora(-1)

    def test_07_minuto_fuera_de_rango(self):
        with self.assertRaises(FechaInvalida):
            Minuto(61)

    def test_08_minuto_menor_a_cero(self):
        with self.assertRaises(FechaInvalida):
            Minuto(-1)

    def test_09_segundo_fuera_de_rango(self):
        with self.assertRaises(FechaInvalida):
            Segundo(61)

    def test_10_segundo_menor_a_cero(self):
        with self.assertRaises(FechaInvalida):
            Segundo(-1)



if __name__ == '__main__':
    unittest.main()
