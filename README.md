# Challenge-Neuralworks
Desarrollo challenge Data Analyst

# Challenge-Neuralworks
Desarrollo challenge Data Analyst

Se desarrolla a través de un archivo py utilizando la librería sqlite3 para el desarrollo y consulta de querys
Respuesta y supuestos para el ejercicio planteado

SUPUESTO PRINCIPAL: Se considera la data donde hay valor en los campos que vienen en formato XML para poder hacer el desglose y posterior eleccion de los mejores 11 jugadores siendo filtrado este requisito en todas las preguntas.

2.- Query desarrollada en archivo Pregunta 2.sql

3.-Para el desarrollo de la primer parte, se crea una query en SQL tal como se propone para poder entender el resultado de los partidos, goles anotados y recibidos, exoyestis en el archivo Pregunta 2.sql, donde a partir de este se podría concretar la tabla de posiciónes final de cada temporada de cada liga, ahora bien si complementamos el lenguaje SQL con otro tipo de herramientas como python se puede extraer el numero de goles, asistencias, corners, centros, tiros al arco, faltas, tarjetas, etc de manera más óptima y expedita, lo cual permite tener una visión global del rendimiento de cada equipo y permite ver su comportamiento a lo largo de los años.

4.-Desarrollo expuesto en archivo TABLA_JUGADORES.py, donde se concreta una tabla compuesta por el rendimiento de cada jugador en cada equipo que este participó, compuesta por goles,asistencias, tarjetas, tiros al arco, posición(la cual es extraida a traves de las coordenadas de cada jugador presente en la tabla match). Como supuesto se considera tanto el equipo como el rendimiento del jugador en cuestion en ese equipo de tal forma que si el equipo tiene un buen rendimiento el jugador en cuestion en conjunto con el resto de integrantes del equipo tienen un mejor rendimiento, factor importante al momento de escoger el 11 ideal posteriormente ya que gracias a esta consideración se puede tomar la version "prime" de cada jugador en base a los parametros clave expuestos con posterioridad

5.- . Para la definición de los mejores jugadores corresponde ver la posición que se busca llenar y en base a la labor que deben cumplir en el campo escoger los indicadores clave para evaluar el rendimiento de cada jugador, por ejemplo y para efectos del 11 ideal escogidos por mi se tomará en consideración  (desarrollo de script en el archivo 11_IDEAL.py)

PORTERO: PORTERO DEL EQUIPO MENOS BATIDO#####
DEFENSA: EQUIPO MENOS BATIDO Y MENOS TARJETAS RECIBIDAS (hubiera sido bueno tener la medicion del numero de cortes,robos o despejes del jugador).
MEDIOCAMPISTA: JUGADORES CON MAYOR NUMERO DE ASISTENCIAS(hubiera sido bueno tener el porcentaje de pases exitosos y km recorridos también para esta medición)
DELANTEROS: JUGADORES CON MAYOR NUMERO DE GOLES Y MAYOR PORCENTAJE DE EFECTIVIDAD (GOLES/TIROS AL ARCO)

CON EL OBJETIVO DE NO OPTAR POR JUGADORES DE EQUIPOS CON BAJO RENDIMIENTO,SE REALIZARÁ EL PRIMER FILTRO DE LOS EQUIPOS CON MEJOR GOAL_MADE/GOAL_RECEIVED ADEMAS DE TENER REGISTRADO A LO MENOS 100 GOLES COMO EQUIPO EVITANDO EQUIPOS CON POCA PARTICIPACIÓN EN LA DATA


PREGUNTA BONUS.-
FORMACION 4-3-3 CLASICA CON 2 EXTREMOS , DOS CENTRALES, LATERAL IZQUIERDO Y DERECHO, Y 3 MC
LLEGANDO A UN EQUIPO "IDEAL" BAJO ESTOS SUPUESTOS COMPUESTO POR LOS SIGUIENTES ID DE JUGADORES 
            
            167035
            
38843   26403   37410   30738

  477615   242469   154259
  
  30981    40636   150250
