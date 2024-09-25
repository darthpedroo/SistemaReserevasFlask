from core.reservamanager import SingletonReservaManager
from core.usuario import Usuario
from core.sala import Sala
from core.fecha import Fecha, Ano, Mes,Dia
from core.tiempo import Tiempo, Hora,Minuto,Segundo
from core.reserva import Reserva
from core.exceptions import ReservableYaReservado, NoExisteLaReserva, ReservaPerteneceOtroUsuario, HoraDeInicioDebeSerMenorAHoraFinal
import unittest

class TestReserva(unittest.TestCase):

    def setUp(self):
        self._reserva_manager = SingletonReservaManager()
        self._usuario_porky = Usuario("Porky")
        self._sala_papu = Sala(nombre="Salita" ,capacidad_maxima=10)
        
    def test_06_multiples_reservas_en_un_dia(self):
        ano_reserva = Ano(2330)
        mes_reserva = Mes(9)
        dia_reserva = Dia(12)

        fecha_reserva = Fecha(ano_reserva, mes_reserva, dia_reserva)
        hora_reserva = Hora(2)
        minuto_reserva = Minuto(0)
        segundo_reserva = Segundo(0)
        horario_inicio_reserva = Tiempo(hora_reserva,minuto_reserva,segundo_reserva)

        hora2_reserva = Hora(3)
        minuto2_reserva = Minuto(0)
        segundo2_reserva = Segundo(0)
        horario_fin_reserva = Tiempo(hora2_reserva,minuto2_reserva,segundo2_reserva)

        fecha2_reserva = Fecha(ano_reserva, mes_reserva, dia_reserva)
        hora3_reserva = Hora(4)
        minuto3_reserva = Minuto(0)
        segundo3_reserva = Segundo(1)
        horario2_inicio_reserva = Tiempo(hora3_reserva,minuto3_reserva,segundo3_reserva)

        hora4_reserva = Hora(6)
        minut4_reserva = Minuto(0)
        segundo4_reserva = Segundo(0)
        horario2_fin_reserva = Tiempo(hora4_reserva,minut4_reserva,segundo4_reserva)

        fecha3_reserva = Fecha(ano_reserva, mes_reserva, dia_reserva)
        hora6_reserva = Hora(3)
        minuto6_reserva = Minuto(0)
        segundo6_reserva = Segundo(1)
        horario3_inicio_reserva = Tiempo(hora6_reserva,minuto6_reserva,segundo6_reserva)

        hora5_reserva = Hora(4)
        minut5_reserva = Minuto(0)
        segundo5_reserva = Segundo(0)
        horario3_fin_reserva = Tiempo(hora5_reserva,minut5_reserva,segundo5_reserva)

        self._usuario_porky.realizar_reserva_programada(self._sala_papu,fecha_reserva,horario_inicio_reserva,horario_fin_reserva)
        self._usuario_porky.realizar_reserva_programada(self._sala_papu,fecha2_reserva,horario2_inicio_reserva,horario2_fin_reserva)
        self._usuario_porky.realizar_reserva_programada(self._sala_papu,fecha3_reserva,horario3_inicio_reserva,horario3_fin_reserva)
        print("self._reserva_manager.get_reservas_activas_dia_especifico(fecha_reserva)", self._reserva_manager.get_reservas_activas_dia_especifico(fecha_reserva))
        
        self.assertEqual(len(self._reserva_manager.get_reservas_activas_dia_especifico(fecha_reserva)), 3)

    def test_07_hora_inicio_menor_hora_final_(self):

        with self.assertRaises(HoraDeInicioDebeSerMenorAHoraFinal):
            ano_reserva = Ano(2025)
            mes_reserva = Mes(9)
            dia_reserva = Dia(12)

            fecha_reserva = Fecha(ano_reserva, mes_reserva, dia_reserva)
            hora_reserva = Hora(5)
            minuto_reserva = Minuto(0)
            segundo_reserva = Segundo(20)
            horario_inicio_reserva = Tiempo(hora_reserva,minuto_reserva,segundo_reserva)  

            hora2_reserva = Hora(3)
            minuto2_reserva = Minuto(0)
            segundo2_reserva = Segundo(30)
            horario_fin_reserva = Tiempo(hora2_reserva,minuto2_reserva,segundo2_reserva)

            self._usuario_porky.realizar_reserva_programada(self._sala_papu,fecha_reserva,horario_inicio_reserva,horario_fin_reserva)

    
if __name__ == "__main__":
    unittest.main()
