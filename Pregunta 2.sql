

SELECT M.ID AS MATCH_ID
,C.NAME AS COUNTRY
,L.NAME AS LEAGUE
,M.season
,M.Stage
,M.date
,TH.TEAM_LONG_NAME AS HOME_NAME
,TH.TEAM_SHORT_NAME AS HOME
,TA.TEAM_LONG_NAME AS AWAY_NAME
,TA.TEAM_SHORT_NAME AS AWAY
,M.home_team_goal	
,M.away_team_goal
,CASE WHEN M.home_team_goaL > M.away_team_goal THEN TH.TEAM_SHORT_NAME
      WHEN M.home_team_goaL < M.away_team_goal THEN TA.TEAM_SHORT_NAME
      ELSE 'DRAW' END AS WINNER
,CASE WHEN M.home_team_goaL > M.away_team_goal THEN 3
    WHEN M.home_team_goaL = M.away_team_goal THEN 1
    ELSE 0 END AS HOME_POINTS
,CASE WHEN M.home_team_goaL < M.away_team_goal THEN 3
    WHEN M.home_team_goaL = M.away_team_goal THEN 1
    ELSE 0 END AS AWAY_POINTS
from Match M

LEFT JOIN COUNTRY C ON C.ID = M.COUNTRY_ID
LEFT JOIN LEAGUE L ON L.ID = M.LEAGUE_ID AND L.COUNTRY_ID = C.ID
LEFT JOIN TEAM TH ON TH.team_api_id = M.HOME_TEAM_API_ID
LEFT JOIN TEAM TA ON TA.team_api_id = M.AWAY_TEAM_API_ID

WHERE M.goal is not null;
