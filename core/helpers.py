
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
    """Se ingresa una fecha como string (formato de la base de datos) y se devuelve una instancia de la clase Fecha

    Args:
        fecha_str (str): xx-yy-zz

    Raises:
        ValueError: Si se ingresa un string en vez de un numero 

    Returns:
        Fecha: Fecha(Ano(xx),Mes(yy),Dia(zz))
    """    
    try:
        dia, mes, ano = map(int, fecha_str.split('-')) 
        return Fecha(Ano(dia), Mes(mes), Dia(ano))
    except ValueError:
        raise ValueError("Formato de Fecha INVALIDO!")

def parse_hora(hora_str: str)->Hora:
    """Se ingresa una hora como string (formato de la base de datos) y se devuelve una instancia de la clase Hora

    Args:
        hora_str (str): xx-yy-zz

    Raises:
        ValueError: Si se ingresa un string en vez de un numero 

    Returns:
        Hora: Hora(Ano(xx),Mes(yy),Dia(zz))
    """   
    try:
        hora, minuto, segundo = map(int, hora_str.split("-"))
        return Tiempo(Hora(hora),Minuto(minuto),Segundo(segundo))
    except ValueError:
        raise ValueError("Formato de Hora INVALIDO !")