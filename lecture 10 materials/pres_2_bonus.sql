-- 1 Сгруппируйте игроков по году (т.е без месяца и даты) рождения. 
-- Определите средний рост, средний вес игроков для каждого года. Таблица Player.
SELECT strftime('%Y',birthday) as year, avg(height/100) as avg_height, avg(weight/2.205) as avg_weight, count(*) as n FROM Player GROUP BY year;

-- 2 Как менялся средний ежегодный рейтинг футболиста Radamel Falcao с 2007 по 2015 год.
-- Таблицы Player, Player_attributes. Колонка overall_rating. 
SELECT year, avg(overall_rating) as avg_rating FROM (
SELECT player_name, Player.player_api_id, overall_rating, CAST(strftime('%Y',date) AS INTEGER) as year  FROM Player JOIN Player_Attributes on Player.player_api_id = Player_Attributes.player_api_id 
WHERE player_name = 'Radamel Falcao' AND year <= 2015 AND year >= 2007
) GROUP by year