--1 Определите кол-во матчей, сыгранных в бельгийском чемпионате в сезоне 2008/2009. Таблица Match.
SELECT count(*) as match_count FROM Match WHERE season = '2008/2009';

--2 Определите суммарное кол-во голов забитых в лиге "Italy Serie A" в сезоне 2008/2009. 
-- Таблица Match. Колонки home_team_goal, away_team_goal. 
SELECT sum(home_team_goal) + sum(away_team_goal) as goals FROM(
SELECT  home_team_goal, away_team_goal FROM League JOIN Match ON League.id = Match.league_id 
WHERE season = '2008/2009' AND name = 'Italy Serie A'
);

-- 3 Определите дату матча, в котором было забито больше всего мячей 
-- в лиге "Italy Serie A" в сезоне 2008/2009. 
-- Таблица Match. Колонки date, home_team_goal, away_team_goal. 
SELECT home_team_goal + away_team_goal as goals, date FROM(
SELECT  home_team_goal, away_team_goal, date FROM League JOIN Match ON League.id = Match.league_id 
WHERE season = '2008/2009' AND name = 'Italy Serie A'
) ORDER BY goals DESC LIMIT 1;