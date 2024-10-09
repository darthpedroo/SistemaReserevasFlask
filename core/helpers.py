
from core.fecha import Fecha, Ano,Mes,Dia
from core.tiempo import Tiempo,Hora,Minuto,Segundo

def is_input_a_valid_int(input):
    """Devuelve True  si un input es un entero > 0, de lo contrario devuele False"""
    try:
        int(input)
    except ValueError:
        print("INGRESA UN NÚMERO, NO UN TEXTO")
        return False
    if int(input) < 0:
        print("INGRESA UN NÚMERO MAYOR A 0")
        return False
    return True


def is_input_greater_than_zero(input):
    """Devuele true si un input es >= 0, de lo contrario devuelve False"""
    try:
        int(input)
    except ValueError:
        print("INGRESA UN NÚMERO, NO UN TEXTO")
        return False
    if int(input) < 0:
        print("INGRESA UN NÚMERO MAYOR A 0")
        return False
    return True

def parse_fecha(fecha_str: str) -> "Fecha":
    try:
        dia, mes, ano = map(int, fecha_str.split('-')) 
        return Fecha(Ano(dia), Mes(mes), Dia(ano))
    except ValueError:
        raise ValueError("Formato de Fecha INVALIDO!")

def parse_hora(hora_str):
    try:
        hora, minuto, segundo = map(int, hora_str.split("-"))
        return Tiempo(Hora(hora),Minuto(minuto),Segundo(segundo))
    except ValueError:
        raise ValueError("Formato de Hora INVALIDO !")