import config_my
import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
import telebot

bot = telebot.TeleBot(config_my.token)


def stat(tag=0):
    url = 'https://www.worldometers.info/coronavirus/'
    website = requests.get(url).text
    soup = BeautifulSoup(website, 'lxml')
    table = soup.find_all('table')[tag]
    rows = table.find_all('tr')
    fields_list = []

    for i in range(9):
        col = list()
        col.append(rows[0].find_all('th')[i + 1].get_text().strip())
        for row in rows[1:224]:
            r = row.find_all('td')
            col.append(r[i + 1].get_text().strip())
        fields_list.append(col)
    d = dict()
    for i in range(9):
        d[fields_list[i][0]] = fields_list[i][1:]
    df = pd.DataFrame(d)
    df = df.rename(columns={'Country,Other': 'Country', 'Serious,Critical': 'SeriousCritical'})
    return df


@bot.message_handler(commands=["start"])
def hello(message):
    bot.send_message(message.chat.id, 'hello')


@bot.message_handler(commands=["help"])
def hello(message):
    bot.reply_to(message, "how are you doing")


if __name__ == '__main__':
    bot.infinity_polling()
