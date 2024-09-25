from flask import Flask, render_template
from core.reservamanager import ReservaManager
from core.fecha import Fecha, Ano, Mes, Dia
from core.tiempo import Tiempo,Hora,Minuto,Segundo
from core.usuario import Usuario
from core.sala import Sala

def crear_sistema():
    reserva_manager_2 = ReservaManager()
    porky = Usuario("John Pork")
    juani = Usuario("Juanitroooox")
    gazo = Usuario("Gazo")
    sala_papu = Sala(nombre="Salita" ,capacidad_maxima=10)
    
    ano_reserva = Ano(2024)
    mes_reserva = Mes(9)
    dia_reserva_1 = Dia(12)
    dia_reserva_2 = Dia(13)
    dia_reserva_3 = Dia(14)
    dia_reserva_4 = Dia(15)
    dia_reserva_5 = Dia(16)
    
    fecha_reserva_1 = Fecha(ano_reserva, mes_reserva, dia_reserva_1)
    fecha_reserva_2 = Fecha(ano_reserva, mes_reserva, dia_reserva_2)
    fecha_reserva_3 = Fecha(ano_reserva, mes_reserva, dia_reserva_3)
    fecha_reserva_4 = Fecha(ano_reserva, mes_reserva, dia_reserva_4)
    fecha_reserva_5 = Fecha(ano_reserva, mes_reserva, dia_reserva_5)


    hora_reserva = Hora(3)
    minuto_reserva = Minuto(0)
    segundo_reserva = Segundo(0)
    horario_inicio_reserva = Tiempo(hora_reserva,minuto_reserva,segundo_reserva)

    hora2_reserva = Hora(5)
    minuto2_reserva = Minuto(0)
    segundo2_reserva = Segundo(0)
    horario_fin_reserva = Tiempo(hora2_reserva,minuto2_reserva,segundo2_reserva)
    
    reserva_manager =porky.realizar_reserva_programada(sala_papu,fecha_reserva_1,horario_inicio_reserva,horario_fin_reserva)
    reserva_manager =juani.realizar_reserva_programada(sala_papu,fecha_reserva_2,horario_inicio_reserva,horario_fin_reserva)
    reserva_manager =gazo.realizar_reserva_programada(sala_papu,fecha_reserva_3,horario_inicio_reserva,horario_fin_reserva)
    reserva_manager =porky.realizar_reserva_programada(sala_papu,fecha_reserva_4,horario_inicio_reserva,horario_fin_reserva)
    reserva_manager = porky.realizar_reserva_programada(sala_papu,fecha_reserva_5,horario_inicio_reserva,horario_fin_reserva)
    print(": ", reserva_manager.todas_las_reservas)
    return reserva_manager
    

app = Flask(__name__)
reserva_manager = crear_sistema()
ano_reserva = Ano(2024)
mes_reserva = Mes(9)
dia_reserva = Dia(12)
fecha_reserva = Fecha(ano_reserva, mes_reserva, dia_reserva)
reservas_dia_especifico = reserva_manager.get_reservas_activas_dia_especifico(fecha_reserva)
todas_las_reservas = reserva_manager.todas_las_reservas
print("Todas: las resrevas: ", todas_las_reservas)

@app.route("/")
def hello_world():
    return render_template("index.html", todas_las_reservas=todas_las_reservas)

@app.route("/reservas")
def crear_reservas():
    pass


if __name__ == '__main__':
    app.run(port=5000,debug=True)
