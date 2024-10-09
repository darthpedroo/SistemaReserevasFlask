[x] Debe ser posible realizar una reserva indicando la sala, la fecha, la hora de inicio y la hora de fin de la misma.

[x]El sistema debe validar que la sala esté disponible en el horario solicitado
(es decir, que no haya otra reserva que se superponga).

[x]Agregar validación por Hora, ya que solo lo hace por Sala y Fecha

[x]Debe ser posible cancelar una reserva.

[x]El sistema debe permitir obtener un listado de las reservas activas en un día específico.

[]Crear una clase que encapsule los distintos atributos que se pueden pasar a los PROGRAMABLES

[x] Revisar que los tiempos no se superpongan

[x]No validar que los dias sean los del calendario

[x]Fecha = Año Mes Día Hora Minuto Segundo

[]Crear Salas disponibles en el ReservaManager

[x]Implementar que el horario final sea mayor al horario inicial

[]Agregar Tests:
    [x] Reserva Fuera de Horario Válido
    [x] Multiples reservas en un mismo día

FLASK

[] ENDPOINT RESERVAS POR USUARIO
[] ENDPOINT RESERVAS POR DIA
[] AGREGAR SALAS MANUALMENTE
    []AL ELEGIR UNA SALA, QUE NO SEA UN INPUT SI NO DE LAS SALAS QUE EXISTEN


[x] ENDPOINT CREAR RESERVAS
[x] ENDPOINT BORRAR RESERVAS
[x] AGREGAR LOS TRY CATCH QUE MUESTREN LAS ALERTAS


DAO

SALAS:
    [x]CREAR TABLA
    [x]CARGAR TABLAS A RESERVA MANAGER
    [x]CREAR SALAS

    
AL BORRAR UNA SALA:
    []ERROR: 'str' object has no attribute '_nombre'
    ISSSSSSSUEEEEEEEE‼‼‼‼‼‼‼‼⁉⁉⁉⁉⁉⁉👩🏾‍🤝‍🧑🏼👩🏾‍🤝‍🧑🏻🗣🧞‍♂️🗣🦃🐓🐚🐡🦐 (ERROR EN INGLES POR LAS DUDAS) PORKY, COMO USUARIO QUIERO PODER CANCELAR UNA RESERVA WITHOUT QUE ME SALGA QUE LA RESERVA NO EXISTE (ESTUPIDIN ESCRUMIN RETRASADIN AUTISTIN TARADIN MOBOLIQUIN 🔥🔥🔥🔥🔥🧠🧠🧠😎🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓🤓☝☝☝☝☝☝☝☝☝☝☝☝☝)

    [] NotImplementedError, EN USUARIO! Fijarse de que a la reserva se pase bien el usuario borrado, porque tira "NOT IMPLEMENTED".
        Entonces, le estoy pasando mal el atributeee.  


    

[]HACER TESTS DAO
    []Setup 
    []TearDown
    

 
