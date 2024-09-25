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