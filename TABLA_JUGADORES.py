# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 12:31:43 2022


@author: fterr
"""

import sqlite3
import pandas as pd
import xmltodict

# Create a SQL connection to our SQLite database



# # Read sqlite query results into a pandas DataFrame
con = sqlite3.connect("database.sqlite")


    

QUERY='''
SELECT * FROM Match WHERE goal IS NOT NULL;
'''


df = pd.read_sql_query(QUERY, con)

# Verify that result of SQL query is stored in the dataframe

# con.close()
# df.to_excel('Match_QUERY.xlsx',index=False)
'''
campos tabla
equipo
quien hizo el gol
asistencia
tipo de gol

'''

goal_list=[]
for match in df['goal']:
    goals = xmltodict.parse(match)
    if goals['goal']!=None:
        if type(goals['goal']['value'])==list:
            for value in goals['goal']['value']:
                a=[]
                try:
                    a.append(value['team'])
                except:
                    a.append('no data')
                try:
                    a.append(value['player1'])
                except:
                    a.append('no data')
                try:
                    a.append(value['player2'])
                except:
                    a.append('no assist')
                try:
                    a.append(value['goal_type'])
                except:
                    try:
                        a.append(value['comment'])
                    except:
                        a.append('no data')
                goal_list.append(a)
        elif type(goals['goal']['value']) == dict:
            a=[]
            try:
                a.append(value['team'])
            except:
                a.append('no data')
            try:
                a.append(value['player1'])
            except:
                a.append('no data')
            try:
                a.append(value['player2'])
            except:
                a.append('no assist')
            try:
                a.append(value['goal_type'])
            except:
                try:
                    a.append(value['comment'])
                except:
                    a.append('no data')
            goal_list.append(a)
  



goal=pd.DataFrame(goal_list)
goal=goal.rename(columns = {0:'team_id',1:'scorer_id',2:'assist_id',3:'goal_type'})
     

#####GOLES#########
goal_count=goal.groupby(['team_id','scorer_id']).size().reset_index()
goal_count=goal_count.rename(columns={0:'goal_count'})


goal_count
#####asistencias#########
assist_count=goal.groupby(['team_id','assist_id']).size().reset_index()
assist_count=assist_count.rename(columns={0:'assist_count'})




###########TARJETAS#############

QUERY='''
SELECT * FROM Match WHERE possession IS NOT NULL;
'''


df = pd.read_sql_query(QUERY, con)


card_list=[]
for match in df['card']:
    cards = xmltodict.parse(match)
    if cards['card']!=None:
        if type(cards['card']['value'])==list:
            for value in cards['card']['value']:
                a=[]
                try:
                    a.append(value['team'])
                except:
                    a.append('no data')
                try:
                    a.append(value['player1'])
                except:
                    a.append('no data')
                try:
                    a.append(value['card_type'])
                except:
                    try:
                        a.append(value['comment'])
                    except:
                        a.append('no data')
                try:
                    a.append(value['subtype'])
                except:
                    a.append('no data')
                card_list.append(a)
        elif type(cards['card']['value']) == dict:
            a=[]
            try:
                a.append(value['team'])
            except:
                a.append('no data')
            try:
                a.append(value['player1'])
            except:
                a.append('no data')
            try:
                a.append(value['card_type'])
            except:
                try:
                    a.append(value['comment'])
                except:
                    a.append('no data')
            try:
                a.append(value['subtype'])
            except:
                a.append('no data')
            card_list.append(a)
card=pd.DataFrame(card_list)
card=card.rename(columns = {0:'team_id',1:'player_id',2:'card_type',3:'foul_type'})

#####TARJETAS AMARILLAS#########
y_card=card[card['card_type']=='y']
y_card=y_card.groupby(['team_id','player_id']).size().reset_index()
y_card=y_card.rename(columns={0:'y_card_count'})


#####TARJETAS ROJAS#########
r_card=card[card['card_type']=='r']
r_card=r_card.groupby(['team_id','player_id']).size().reset_index()
r_card=r_card.rename(columns={0:'r_card_count'})



con = sqlite3.connect("database.sqlite")
QUERY='''
SELECT * FROM Match WHERE possession IS NOT NULL;
'''


df = pd.read_sql_query(QUERY, con)



cross_list=[]
for match in df['cross']:
    cross = xmltodict.parse(match)
    if cross['cross']!=None:
        if type(cross['cross']['value'])==list:
            for value in cross['cross']['value']:
                a=[]
                try:
                    a.append(value['team'])
                except:
                    a.append('no data')
                try:
                    a.append(value['player1'])
                except:
                    a.append('no data')
                try:
                    a.append(value['type'])
                except:
                    a.append('cross')
                cross_list.append(a)
        elif type(cross['cross']['value']) == dict:
            a=[]
            try:
                a.append(value['team'])
            except:
                a.append('no data')
            try:
                a.append(value['player1'])
            except:
                a.append('no data')
            try:
                a.append(value['type'])
            except:
                a.append('cross')
            cross_list.append(a)
cross=pd.DataFrame(cross_list)
cross=cross.rename(columns = {0:'team_id',1:'player_id',2:'type'})

cross_made=cross.groupby(['team_id','player_id']).size().reset_index()
cross_made=cross_made.rename(columns={0:'cross_count'})


######SHOTON##########


shoton_list=[]
for match in df['shoton']:
    shoton = xmltodict.parse(match)
    if shoton['shoton']!=None:
        if type(shoton['shoton']['value'])==list:
            for value in shoton['shoton']['value']:
                a=[]
                try:
                    a.append(value['team'])
                except:
                    a.append('no data')
                try:
                    a.append(value['player1'])
                except:
                    a.append('no data')
                try:
                    a.append(value['type'])
                except:
                    a.append('shoton')
                shoton_list.append(a)
        elif type(shoton['shoton']['value']) == dict:
            a=[]
            try:
                a.append(value['team'])
            except:
                a.append('no data')
            try:
                a.append(value['player1'])
            except:
                a.append('no data')
            try:
                a.append(value['type'])
            except:
                a.append('shoton')
            shoton_list.append(a)
shoton=pd.DataFrame(shoton_list)
shoton=shoton.rename(columns = {0:'team_id',1:'player_id',2:'type'})

shoton_made=shoton.groupby(['team_id','player_id']).size().reset_index()
shoton_made=shoton_made.rename(columns={0:'shoton_count'})



shotoff_list=[]
for match in df['shotoff']:
    shotoff = xmltodict.parse(match)
    if shotoff['shotoff']!=None:
        if type(shotoff['shotoff']['value'])==list:
            for value in shotoff['shotoff']['value']:
                a=[]
                try:
                    a.append(value['team'])
                except:
                    a.append('no data')
                try:
                    a.append(value['player1'])
                except:
                    a.append('no data')
                try:
                    a.append(value['type'])
                except:
                    a.append('shotoff')
                shotoff_list.append(a)
        elif type(shotoff['shotoff']['value']) == dict:
            a=[]
            try:
                a.append(value['team'])
            except:
                a.append('no data')
            try:
                a.append(value['player1'])
            except:
                a.append('no data')
            try:
                a.append(value['type'])
            except:
                a.append('shotoff')
            shotoff_list.append(a)
shotoff=pd.DataFrame(shotoff_list)
shotoff=shotoff.rename(columns = {0:'team_id',1:'player_id',2:'type'})

shotoff_made=shotoff.groupby(['team_id','player_id']).count().reset_index()
shotoff_made=shotoff_made.rename(columns={0:'shotoff_count'})




foulcommit_list=[]
for match in df['foulcommit']:
    foulcommit = xmltodict.parse(match)
    if foulcommit['foulcommit']!=None:
        if type(foulcommit['foulcommit']['value'])==list:
            for value in foulcommit['foulcommit']['value']:
                a=[]
                try:
                    a.append(value['team'])
                except:
                    a.append('no data')
                try:
                    a.append(value['player1'])
                except:
                    a.append('no data')
                try:
                    a.append(value['type'])
                except:
                    a.append('foulcommit')
                foulcommit_list.append(a)
        elif type(foulcommit['foulcommit']['value']) == dict:
            a=[]
            try:
                a.append(value['team'])
            except:
                a.append('no data')
            try:
                a.append(value['player1'])
            except:
                a.append('no data')
            try:
                a.append(value['type'])
            except:
                a.append('foulcommit')
            foulcommit_list.append(a)
foulcommit=pd.DataFrame(foulcommit_list)
foulcommit=foulcommit.rename(columns = {0:'team_id',1:'player_id',2:'type'})

foulcommit_made=foulcommit.groupby(['team_id','player_id']).size().reset_index()
foulcommit_made=foulcommit_made.rename(columns={0:'foulcommit_count'})


df_players=pd.merge(goal_count,assist_count,left_on=['team_id','scorer_id'],right_on=['team_id','assist_id'])
df_players=df_players.drop('assist_id',axis=1)
df_players=df_players.rename(columns={'scorer_id':'player_id'})
df_players=pd.merge(df_players,y_card,how='left',left_on=['team_id','player_id'],right_on=['team_id','player_id'])

df_players=pd.merge(df_players,r_card,how='left',left_on=['team_id','player_id'],right_on=['team_id','player_id'])

df_players=pd.merge(df_players,shoton_made,how='left',left_on=['team_id','player_id'],right_on=['team_id','player_id'])

df_players=pd.merge(df_players,shotoff_made,how='left',left_on=['team_id','player_id'],right_on=['team_id','player_id'])

df_players=pd.merge(df_players,foulcommit_made,how='left',left_on=['team_id','player_id'],right_on=['team_id','player_id'])

df_players=pd.merge(df_players,cross_made,how='left',left_on=['team_id','player_id'],right_on=['team_id','player_id'])
print(df_players)

df_players.to_excel('players.xlsx')




####EXTRAER LA POSICIÓN DE JUEGO DE CADA JUGADOR###########

con = sqlite3.connect("database.sqlite")
QUERY='''
SELECT * FROM Match WHERE possession IS NOT NULL;
'''


df = pd.read_sql_query(QUERY, con)

player_pos_acum=[]
####JUGADORES_LOCALES####
for i in range(11):
    home_player='home_player_'+str(i+1)
    home_player_x='home_player_X'+str(i+1)
    home_player_y='home_player_Y'+str(i+1)
    home=df[['home_team_api_id',home_player,home_player_x,home_player_y]]
    home=home.rename(columns={home_player:'player_id','home_team_api_id':'team_id'})
    home=home[home['player_id']!=None]
    home['poss']=[[home[home_player_x][j],home[home_player_y][j]] for j in range(len(home['player_id']))]
    home=home[['team_id','player_id','poss']]
    player_pos_acum.append(home)
    
    
    
for i in range(11):
    away_player='away_player_'+str(i+1)
    away_player_x='away_player_X'+str(i+1)
    away_player_y='away_player_Y'+str(i+1)
    away=df[['away_team_api_id',away_player,away_player_x,away_player_y]]
    away=away.rename(columns={away_player:'player_id','away_team_api_id':'team_id'})
    away=away[away['player_id']!=None]
    away['poss']=[[away[away_player_x][j],away[away_player_y][j]] for j in range(len(away['player_id']))]
    away=away[['team_id','player_id','poss']]
    player_pos_acum.append(away)
    
player_pos=pd.concat(player_pos_acum).reset_index()


def ubicacion(lista):
    if lista[1] == 1:
        return 'POR'
    elif lista[1]>=2 and lista[1]<=5:
        return 'DEF'
    elif lista[1]>=6 and lista[1]<=8:
        return 'MED'
    elif lista[1]>=9 and lista[1]<=11:
        return 'DEL'

player_pos['ubicacion']=[ubicacion(player_pos['poss'][x]) for x in range(len(player_pos['player_id']))]

player_pos=player_pos[['team_id','player_id','ubicacion']].drop_duplicates().reset_index()

player_pos=player_pos[['team_id','player_id','ubicacion']]

df_players['player_id']=df_players['player_id'].astype(float)
df_players['team_id']=df_players['team_id'].astype(float)

df_player=pd.merge(df_players,player_pos,how='left',left_on=['team_id','player_id'],right_on=['team_id','player_id'])

df_player['player_id']=df_player['player_id'].astype(int)


df_player['team_id']=df_player['team_id'].astype(int)

df_player = df_player.drop_duplicates()


con = sqlite3.connect("database.sqlite")
QUERY='''
SELECT TEAM_ID AS team_id
,SUM(GOAL_MADE)AS GOAL_MADE
,SUM(GOAL_RECEIVED) AS GOAL_RECEIVED


FROM(
SELECT HOME_TEAM_API_ID AS TEAM_ID
,SUM(HOME_TEAM_GOAL) AS GOAL_MADE
,SUM(AWAY_TEAM_GOAL) AS GOAL_RECEIVED
FROM Match WHERE possession IS NOT NULL
GROUP BY HOME_TEAM_API_ID

union all


SELECT AWAY_TEAM_API_ID AS TEAM_ID
,SUM(AWAY_TEAM_GOAL) AS GOAL_MADE
,SUM(HOME_TEAM_GOAL) AS GOAL_RECEIVED
FROM Match WHERE possession IS NOT NULL
GROUP BY AWAY_TEAM_API_ID 
) A
GROUP BY TEAM_ID;
'''


team_goal = pd.read_sql_query(QUERY, con)

df_player=pd.merge(df_player,team_goal,how='left',left_on=['team_id'],right_on=['team_id'])

# df_player.to_excel('JUGADORES.xlsx')




print(df_player)

