import os
import re
import sqlite3

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver as wb

driver = wb.Chrome('../chromedriver_win32/chromedriver.exe')

driver.implicitly_wait(2)
driver.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")

soup = BeautifulSoup(driver.page_source, 'lxml')
df_250 = pd.DataFrame(columns=['title', 'year', 'rating', 'rating_count', 'link'])

table_films = soup.find_all('tbody', {'class': 'lister-list'})[0]
for elem in table_films.find_all('tr'):
    title_cell = elem.find_all('td', {'class': 'titleColumn'})[0]
    title = title_cell.a.text
    #     print(title)
    link = title_cell.find('a').get('href')
    #     print(link)
    date_text = elem.find_all('td', {'class': 'titleColumn'})[0].span.text
    date_int = int(re.findall(r'\d+', date_text)[0])
    #     print(date_int)
    rating_cell = elem.find_all('td', {'class': 'ratingColumn imdbRating'})[0]
    rating = float(rating_cell.text.strip().replace(',', '.'))
    count_info = (rating_cell.find('strong').get('title'))
    num_rating = (re.findall(r'(?:\d+\s)+(?:\d+)', count_info))
    num_rating = int("".join(num_rating[0].split()))
    #     print(num_rating)
    #     print(rating)
    row_to_add = [title, date_int, rating, num_rating, link]
    #     print(row_to_add)
    our_one_row = pd.DataFrame([row_to_add], columns=['title', 'year', 'rating', 'rating_count', 'link'])
    df_250 = df_250.append(our_one_row, ignore_index=True)  # add it to a temporary df

if not os.path.exists('movie.sqlite'):
    conn = sqlite3.connect('movie.sqlite')
    cur = conn.cursor()
    # crating a new table with our structure
    cur.executescript(
        '''CREATE TABLE "top250" (
        "title" TEXT,
        "year"  INTEGER,
        "rating"   NUMERIC,
        "rating_count"  INTEGER,
        "link"    TEXT,
        PRIMARY KEY (title, year));
    ''')
    conn.commit()
    cur.close()

# open connection and write from pandas to sqlite
conn = sqlite3.connect('movie.sqlite')
df_250.to_sql('top250', conn, if_exists='replace', index=False)
conn.commit()
