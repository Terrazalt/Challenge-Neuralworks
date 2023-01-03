# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 20:47:29 2023

@author: fterr
"""

from TABLA_JUGADORES import *


#######CRITERIOS PARA DEFINIR JUGADORES#######
####PORTERO: PORTERO DEL EQUIPO MENOS BATIDO#####
####DEFENSA: EQUIPO MENOS BATIDO Y MENOS TARJETAS RECIVIDAS
#### MEDIOCAMPISTA: JUGADORES CON MAYOR NUMERO DE ASISTENCIAS
#### DELANTEROS: JUGADORES CON MAYOR NUMERO DE GOLES Y MAYOR PORCENTAJE DE EFECTIVIDAD (GOLES/TIROS AL ARCO)
#### CON EL OBJETIVO DE NO OPTAR POR JUGADORES DE EQUIPOS CON BAJO RENDIMIENTO,
### SE REALIZARÁ EL PRIMER FILTRO DE LOS EQUIPOS CON MEJOR GOAL_MADE/GOAL_RECEIVED 
### ADEMAS DE TENER REGISTRADO A LO MENOS 100 GOLES COMO EQUIPO EVITANDO EQUIPOS CON POCA PARTICIPACIÓN EN LA DATA


####FORMACION 4-3-3 CLASICA CON 2 EXTREMOS , DOS CENTRALES LATERAL IZQUIERDO Y DERECHO, Y 3 MC##



df_player['gf/gc']=[df_player['GOAL_MADE'][x]/df_player['GOAL_RECEIVED'][x] for x in range(len(df_player['team_id']))]
df_player=df_player[df_player['GOAL_MADE']>=150]
df_player=df_player.sort_values('gf/gc',ascending=False)
#####PORTERO####

portero=df_player[(df_player['ubicacion']=='POR')].sort_values(by=['gf/gc'],ascending=False)
portero=portero.head(20)
portero=portero.sort_values('GOAL_RECEIVED',ascending=True).head(1).reset_index()



######DEFENSAS#####
defensas=df_player[(df_player['ubicacion']=='DEF')].sort_values(by=['gf/gc'],ascending=False)
defensas=defensas.head(20)
defensas=defensas.sort_values('GOAL_RECEIVED',ascending=True).head(15)
defensas=defensas.sort_values('r_card_count',ascending=True).head(10)
defensas=defensas.sort_values('y_card_count',ascending=True).head(4).reset_index()


####MEDIOCAMPISTAS######3

mc=df_player[(df_player['ubicacion']=='MED')].sort_values(by=['gf/gc'],ascending=False)
mc=mc.head(20)
mc=mc.sort_values('assist_count',ascending=True).head(3).reset_index()


######3DELANTEROS########
delanteros=df_player[(df_player['ubicacion']=='DEL')].sort_values(by=['gf/gc'],ascending=False).reset_index()
delanteros=delanteros.head(20)
delanteros['efectividad']=[delanteros['goal_count'][x]/(delanteros['shoton_count'][x]) for x in range(len(delanteros['player_id']))]
delanteros=delanteros.sort_values('efectividad',ascending=False).head(10)
delanteros=delanteros.sort_values('goal_count',ascending=False).head(3).reset_index()





'''
a partir de esto podríamos decir que esta es la formación escogida y los supuestos definidos
este sería el 11 ideal
'''

print('           ',portero['player_id'][0],'      ')
print(defensas['player_id'][0],' ',defensas['player_id'][1],' ',defensas['player_id'][2],' ',defensas['player_id'][3])
print(' ',mc['player_id'][0],' ',mc['player_id'][1],' ',mc['player_id'][2])
print(' ',delanteros['player_id'][0],'  ',delanteros['player_id'][1],' ',delanteros['player_id'][2])
