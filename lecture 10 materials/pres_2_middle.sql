-- 1 Найдите всех футболистов из всех лиг, вес которых превышал 100 кг. Обратите внимание, что вес в таблице указан в фунтах. (1 кг. = 2.205 фунта). Информация содержится в таблице Player. (4 футболиста).
SELECT id, weight/2.205 as weight FROM Player WHERE weight/2.205 > 100;

-- 2 Найдите футболиста вес, которого превышает 100 кг, а рост 200 см. Напишите запрос (!).
SELECT id, weight/2.205 as weight, height FROM Player WHERE weight/2.205 > 100 AND height/100 > 2;

-- 3 Напишите запрос для поиска среднего веса и среднего роста футболистов,
-- рожденных после 1994 года. Получите два числа и назовите колонки, в которых они находятся “avg_weight” и “avg_height”.
SELECT avg(weight/2.205) as avg_weight, avg(height/100) as avg_height FROM Player WHERE birthday > 1995;

-- 4 Напишите запрос для сортировки всех футболистов по весу по убыванию, по росту по возрастанию.
-- Выведите колонки id, player_name, birthday, height, weight.
SELECT id, player_name, birthday, height, weight FROM Player ORDER BY weight DESC, height ASC;

-- 5 Напишите запрос для подсчета дивизионов, представленных в датасете. (таблица League).
SELECT count(distinct name) as league_count FROM League;

-- 6 Посчитайте кол-во “лево-” и “правоногих” футболистов за все время по всех лигах.
-- Таблица Player_Attributes, колонка preferred_foot. 
SELECT preferred_foot, count(*) as number FROM Player_Attributes GROUP BY preferred_foot HAVING preferred_foot NOT NULL;

-- 7 Определите максимальный рост игрока из всех лиг, рожденного между 1992 и 1994 годом. 
SELECT max(height/100) as max_height, id, player_name, birthday FROM Player WHERE birthday > 1992 AND birthday < 1995;

-- 8 Определите минимальный вес игрока, рожденного в этот же промежуток времени. 
SELECT min(weight/2.205) as min_weight, id, player_name, birthday FROM Player WHERE birthday > 1992 AND birthday < 1995;

-- 9  Выгрузите имена 15 самых высоких футболистов, рожденных в 1992-1994 гг.
-- Упорядочьте список по убыванию. Таблица Player.
SELECT height/100 as height, id, player_name, birthday FROM Player WHERE birthday > 1992 AND birthday < 1995 ORDER by height DESC LIMIT 15;

-- 10 Определите какими словами характеризуется атакующая сила футболиста (attacking_work_rate)
-- в таблице Player_Attributes. (9 слов). 
SELECT DISTINCT attacking_work_rate from Player_Attributes;

-- 11 Посчитайте кол-во строк, которые соответствуют разной атакующей силе футболиста (attacking_work_rate)
--  в таблице Player_Attributes. Т.е сколько раз данная характеристика встречается в описании спортсмена.
SELECT * FROM (
SELECT attacking_work_rate, count(*) as frequency FROM Player_Attributes GROUP BY attacking_work_rate
) ORDER BY frequency DESC;

-- 12 Посчитайте кол-во дней из колонки birthday, в которых рождалось более одного футболиста. 
-- Да, странно звучит :-). Таблица Player, колонка birthday. 

-- SELECT birthday, count(*) as frequency FROM Player GROUP BY birthday HAVING frequency > 1 ORDER BY frequency DESC;
SELECT count(frequency) FROM (
SELECT birthday, count(*) as frequency FROM Player GROUP BY birthday HAVING frequency > 1
);

-- 13 Посчитайте кол-во футболистов с именем Aaron.
SELECT count(player_name) from Player WHERE player_name LIKE "Aaron%";

-- 14 Посчитайте кол-во футболистов с фамилией, заканчивающейся на do, при условии, что у спортсмена указаны имя и фамилия. 
-- Если же указаны только имя, либо фамилия -- игнорируйте строку. 
SELECT count(player_name) from Player WHERE player_name LIKE "% %do";

-- 15 Выгрузите имена футболистов, которые в своей фамилии имеют 
-- 3 буквы “s” и скорость (sprint_speed) которых когда-либо была выше 70.
-- Таблицы Player, Player_Attributes. Колонки player_name, id, sprint_speed.
-- Фамилией футболиста считать часть строки player_name, которая идет после первого пробела.  
PRAGMA case_sensitive_like = false;
SELECT  player_name, Player.id, sprint_speed from Player JOIN Player_Attributes on Player.id = Player_Attributes.id WHERE player_name LIKE "% %S%s%s%" AND sprint_speed > 70;


