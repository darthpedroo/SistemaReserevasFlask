from core.reservableprogramado import Reservable
from core.fecha import Fecha
from core.tiempo import Tiempo
from core.exceptions import HoraDeInicioDebeSerMenorAHoraFinal
#from usuario import Usuario


class Reserva:
    def __init__(self, reservable: Reservable, usuario_reserva:"Usuario", fecha_reserva:Fecha, hora_inicio_reserva:Tiempo, hora_fin_reserva:Tiempo) -> None:
        self._reservable = reservable
        self._usuario_reserva = usuario_reserva
        self._fecha_reserva = fecha_reserva
        self._hora_inicio_reserva = hora_inicio_reserva
        self._hora_fin_reserva = hora_fin_reserva

        if hora_inicio_reserva >= hora_fin_reserva:
            raise HoraDeInicioDebeSerMenorAHoraFinal
    
    
    def __eq__(self, otra_reserva: "Reserva") -> bool:
        return self._reservable == otra_reserva._reservable and self._usuario_reserva == otra_reserva._usuario_reserva and self._fecha_reserva == otra_reserva._fecha_reserva and self._hora_inicio_reserva == otra_reserva._hora_inicio_reserva and self._hora_fin_reserva == otra_reserva._hora_fin_reserva
    
    def __str__(self) -> str:
        return f'{{"usuario": {str(self._usuario_reserva)}, ' \
            f'"reservable": {str(self._reservable)}, ' \
            f'"fecha_reserva": {str(self._fecha_reserva)}, ' \
            f'"hora_inicio_reserva": {str(self._hora_inicio_reserva)}, ' \
            f'"hora_fin_reserva": {str(self._hora_fin_reserva)} }}'


        
    
    def esta_en_el_intervalo_de(self,otra_reserva:"Reserva"):
        """Checkea que si una reserva está en el intervalo de otra reserva"""
        
        if self._fecha_reserva != otra_reserva._fecha_reserva:
            return False
        return not (self._hora_fin_reserva <= otra_reserva._hora_inicio_reserva or self._hora_inicio_reserva >= otra_reserva._hora_fin_reserva)
        
    
    

        

        

    def es_el_mismo_usuario(self,otro_usuario:"Usuario"):
        return self._usuario_reserva == otro_usuario

    def esta_reservada_para_la_fecha(self, otra_fecha:Fecha):
        return self._fecha_reserva == otra_fecha
    
    def es_el_mismo_reservable(self, otro_reservable: Reservable):
        return self._reservable == otro_reservable
    
    def es_misma_hora_inicio(self, otra_hora_inicio: Tiempo):
        return self._hora_inicio_reserva == otra_hora_inicio
    
    def es_misma_hora_fin(self, otra_hora_fin: Tiempo):
        return self._hora_fin_reserva == otra_hora_fin
    

        
        


    
        


        