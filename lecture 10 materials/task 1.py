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

pd.read_sql('select * from top250 limit 5', conn)


def get_director_by_n_film(topn):
    chr_driver = wb.Chrome('../chromedriver_win32/chromedriver.exe')
    chr_driver.implicitly_wait(1)
    chr_driver.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")

    film_link = f'//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr[{topn}]/td[2]/a'
    fld = chr_driver.find_element_by_xpath(film_link)
    fld.click()
    try:
        director = chr_driver.find_element_by_xpath('//*[@id="title-overview-widget"]/div[2]/div[1]/div[2]/a').text
    except:
        director = chr_driver.find_element_by_xpath(
            '//*[@id="title-overview-widget"]/div[2]/div[2]/div[1]/div[2]/a').text

    chr_driver.quit()
    return director


conn = sqlite3.connect('movie.sqlite')  # friends db
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Directors (id INTEGER PRIMARY KEY, 
                                                    director TEXT)''')
get_director_by_n_film(134)
positions = range(3)
# positions = range(250) ## - нужно запустить эту строку для обновления всех данных, работает медленно

for pos in positions:
    try:
        cur_director = get_director_by_n_film(pos + 1)
    except:
        cur_director = ""
    cur.execute('''REPLACE INTO Directors
                            (id, director) VALUES (?, ?)''', (pos + 1, cur_director))
    conn.commit()
    print(pos + 1, cur_director)

top_directors = cur.execute(
    "SELECT director, count(*) from directors GROUP by director ORDER by count(*) DESC LIMIT 10")
top10 = pd.DataFrame(top_directors, columns=['Director', 'number of films'])
top10
top10[top10['number of films'] == max(top10['number of films'])]
conn.close()
