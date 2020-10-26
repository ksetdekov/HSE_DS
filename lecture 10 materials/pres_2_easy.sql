-- 1-3 Выгрузите содержимое таблицы Player, id, player_name, birthday Отобразите первые 7 строк из набора выше.
SELECT id, player_name, birthday from Player LIMIT 7;

-- 4 Выгрузите колонку id, а колонку height из сантиметров переведи в метры, а weight из фунтов в килограммы (1 кг. = 2.205 фунта). 
SELECT id, height/100 as height, weight/2.205 as weight FROM Player;

-- 5 Выгрузите колонки id, birthday, переименовав их в “имя” и “день рождения”.
SELECT id as имя, birthday as "день рождения" FROM Player;

-- 6 ИМТ
SELECT id, (weight/2.205)/(height/100) as ИМТ FROM Player;

-- 7 ИМТ сортировка
SELECT id, (weight/2.205)/(height/100) as ИМТ FROM Player ORDER BY ИМТ;
