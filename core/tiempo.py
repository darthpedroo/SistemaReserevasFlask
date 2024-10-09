from core.exceptions import FechaInvalida

class Tiempo():
    def __init__(self,hora:"Hora",minuto:"Minuto",segundo:"Segundo") -> None:
        self._hora = hora
        self._minuto = minuto
        self._segundo = segundo
    
    def __eq__(self, otro_tiempo: "Tiempo"):
        return self._hora == otro_tiempo._hora and self._minuto == otro_tiempo._minuto and self._segundo == otro_tiempo._segundo

    def __gt__(self, otro_tiempo: "Tiempo"):
        if self._hora > otro_tiempo._hora:
            return True
        elif self._hora < otro_tiempo._hora:
            return False
        if self._minuto > otro_tiempo._minuto:
            return True
        elif self._minuto < otro_tiempo._minuto:
            return False
        return self._segundo > otro_tiempo._segundo

    def __ge__(self, otro_tiempo: "Tiempo"):
        return self > otro_tiempo or self == otro_tiempo
    
    def __str__(self) -> str:
        return f"{self._hora}-{self._minuto}-{self._segundo}"

class Hora:
    def __init__(self,hora) -> None:

        if hora < 0 or hora > 24:
            raise FechaInvalida

        self._hora = hora
    
    def __eq__(self, other_hora: "Hora") -> bool:
        return self._hora == other_hora._hora

    def __gt__(self, otra_hora: "Hora"):
        return self._hora > otra_hora._hora

    def __ge__(self, otra_hora: "Hora"):
        return self._hora >= otra_hora._hora
    
    def __str__(self) -> str:
        return f"{self._hora}"
    
class Minuto:
    def __init__(self,minuto) -> None:
        
        if minuto < 0 or minuto > 60:
            raise FechaInvalida
        self._minuto = minuto
    
    def __eq__(self, otro_minuto: "Minuto") -> bool:
        return self._minuto == otro_minuto._minuto

    def __gt__(self, otro_minuto:"Minuto"):
        return self._minuto > otro_minuto._minuto

    def __ge__(self, otro_minuto:"Minuto"):
        return self._minuto >= otro_minuto._minuto
    
    def __str__(self) -> str:
        return f"{self._minuto}"

class Segundo:
    def __init__(self,segundo) -> None:

        if segundo < 0 or segundo > 60:
            raise FechaInvalida
        self._segundo = segundo
    
    def __eq__(self, otro_segundo: "Segundo") -> bool:
        return self._segundo == otro_segundo._segundo
    
    def __gt__(self, otro_segundo: "Segundo"):
        return self._segundo > otro_segundo._segundo
    
    def __ge__(self, otro_segundo: "Segundo"):
        return self._segundo >= otro_segundo._segundo

    def __str__(self) -> str:
        return f"{self._segundo}"