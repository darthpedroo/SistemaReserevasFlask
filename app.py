from flask import Flask, render_template, request, redirect
from core.reservamanager import ReservaManager
from core.fecha import Fecha, Ano, Mes, Dia
from core.tiempo import Tiempo, Hora, Minuto, Segundo
from core.usuario import Usuario
from core.sala import Sala
from core.reserva import Reserva

from dao.sala.salaSQLiteDao import SalaSqliteDao


DB_PATH = "./data/boiler.db"


def crear_sistema():
    reserva_manager = ReservaManager()
    sala_dao = SalaSqliteDao(DB_PATH)
    todas_las_salas = sala_dao.get_all_salas()
    reserva_manager.load_salas(todas_las_salas)
    print("Todas las salas: ", todas_las_salas)
    return reserva_manager

    
    


def realizar_reserva(
    p_usuario: str,
    sala: str,
    capacidad_maxima: int,
    ano: int,
    mes: int,
    dia: int,
    hora_inicio: int,
    minuto_inicio: int,
    segundo_inicio: int,
    hora_fin: int,
    minuto_fin: int,
    segundo_fin: int
):
    usuario = Usuario(p_usuario)
    sala = Sala(sala, int(capacidad_maxima))
    ano = Ano(int(ano))
    mes = Mes(int(mes))
    dia = Dia(int(dia))

    hora_inicio = Hora(int(hora_inicio))
    minuto_inicio = Minuto(int(minuto_inicio))
    segundo_inicio = Segundo(int(segundo_inicio))

    hora_fin = Hora(int(hora_fin))
    minuto_fin = Minuto(int(minuto_fin))
    segundo_fin = Segundo(int(segundo_fin))

    fecha = Fecha(ano, mes, dia)
    tiempo_inicio = Tiempo(hora_inicio, minuto_inicio, segundo_inicio)
    tiempo_fin = Tiempo(hora_fin, minuto_fin, segundo_fin)

    return usuario.realizar_reserva_programada(sala, fecha, tiempo_inicio, tiempo_fin)


def cancelar_reserva_usuario(usuario: Usuario, reserva: Reserva):
    usuario.cancelar_reserva_programada(reserva)


app = Flask(__name__)
reserva_manager = crear_sistema()
ano_reserva = Ano(2024)
mes_reserva = Mes(9)
dia_reserva = Dia(12)
fecha_reserva = Fecha(ano_reserva, mes_reserva, dia_reserva)
reservas_dia_especifico = reserva_manager.get_reservas_activas_dia_especifico(
    fecha_reserva)
todas_las_reservas = reserva_manager.todas_las_reservas


@app.route("/")
def index():
    return render_template("index.html", todas_las_reservas=todas_las_reservas)


@app.route("/reservas")
def crear_reservas():
    salas = reserva_manager.todas_las_salas
    return render_template("reservas.html", salas=salas, todas_las_reservas=todas_las_reservas)


@app.route("/crear-reserva", methods=["GET", "POST"])
def crear_reserva():
    if request.method == 'POST':
        try:
            print("Form data:", request.form)
            usuario = request.form["usuario"]
            sala = request.form["sala"]
            ano = request.form["ano"]
            mes = request.form["mes"]
            dia = request.form["dia"]
            hora_inicio = request.form["hora_inicio"]
            minuto_inicio = request.form["minuto_inicio"]
            segundo_inicio = request.form["segundo_inicio"]
            hora_fin = request.form["hora_fin"]
            minuto_fin = request.form["minuto_fin"]
            segundo_fin = request.form["segundo_fin"]

            print("dadadadad", sala)
            curr_sala = reserva_manager.encontrar_sala_from_string(sala)
            capacidad_maxima = curr_sala.capacidad_maxima
            print("capa max: ", capacidad_maxima)

            new_usuario = Usuario(usuario)
            todas_las_reservas = realizar_reserva(usuario, sala, capacidad_maxima, ano, mes, dia,
                                                  hora_inicio, minuto_inicio, segundo_inicio, hora_fin, minuto_fin, segundo_fin)
            return redirect("/reservas")
        except Exception as ex:
            return render_template("exception.html", ex=ex)
    salas = reserva_manager.todas_las_salas
    return render_template("crear-reserva.html", salas=salas)


@app.route("/crear-usuario")
def crear_usuario_local_storage():
    return render_template("crear-usuario.html")


@app.route("/cancelar-reserva", methods=["GET", "POST"])
def cancelar_reserva():
    if request.method == "POST":
        try:
            usuario = request.form["usuario"]
            index_s = request.form["index"]
            index = int(index_s)-1
            new_user = Usuario(usuario)
            reserva = reserva_manager.get_reserva_by_id(index)
            print(reserva)
            new_user.cancelar_reserva_programada(reserva)
        except Exception as ex:
            return render_template("exception.html", ex=ex)

    return render_template("reservas.html", todas_las_reservas=todas_las_reservas)


@app.route("/salas", methods=["GET"])
def get_salas():
    salas = reserva_manager.todas_las_salas
    return render_template("salas.html", salas=salas)


@app.route("/agregar-sala", methods=["GET", "POST"])
def agregar_sala():
    if request.method == "POST":
        try:
            nombre = request.form["nombre"]
            capacidad_maxima = request.form["capacidad_maxima"]
            new_sala = Sala(nombre, int(capacidad_maxima))
            reserva_manager.agregar_sala(new_sala)

            print("Sala creada excitosamente !")
        except Exception as ex:
            return render_template("exception.html", ex=ex)
    salas = reserva_manager.todas_las_salas
    return render_template("salas.html", salas=salas)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
