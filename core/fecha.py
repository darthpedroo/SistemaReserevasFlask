from core.exceptions import NumeroMenorAZero, FechaInvalida

class Fecha:
    def __init__(self, ano:"Ano",mes:"Mes",dia:"Dia") -> None:
        self._ano = ano
        self._mes = mes
        self._dia = dia

    def __eq__(self, otra_fecha: "Fecha") -> bool:
        if not isinstance(otra_fecha, Fecha):
            return NotImplemented
        return self._ano == otra_fecha._ano and self._mes == otra_fecha._mes and self._dia == otra_fecha._dia

    def __str__(self) -> str:
        return f"{self._ano}-{self._mes}-{self._dia}"

class Ano:
    def __init__(self, ano:int) -> None:
        if ano <0:
            raise FechaInvalida
        self._ano = ano

    def __str__(self) -> str:
        return f"{self._ano}"
    def __eq__(self,otro_ano:"Ano"):
        return self._ano == otro_ano._ano


class Mes:
    def __init__(self, mes) -> None:
        if mes <= 0 or mes > 12:
            raise FechaInvalida
        self._mes = mes
    
    def __str__(self) -> str:
        return f"{self._mes}"

    def __eq__(self,otro_mes:"Mes"):
        return self._mes == otro_mes._mes

class Dia:
    def __init__(self, dia) -> None:

        if dia <= 0 or dia > 31:
            raise FechaInvalida
        self._dia = dia
    
    def __str__(self) -> str:
        return f"{self._dia}"

    def __eq__(self, otro_dia: "Dia"):
        return self._dia == otro_dia._dia
     

        