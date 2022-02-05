import telebot
import requests
import time
import schedule
from bs4 import BeautifulSoup


token = '5214712668:AAHK2kjhCHEa__olavwm9KnThKpAAdY3UNo'
bot: telebot.TeleBot = telebot.TeleBot(token)


def get_text(url):
    response_horoscope = requests.get(url)
    soup = BeautifulSoup(response_horoscope.text, 'lxml')
    for prediction in soup.find('p', {'class': ""}):
        return prediction


def get_horoscope(message):
    zodiac_map = {'aries': '♈', 'taurus': '♉', 'gemini': '♊', 'cancer': '♋', 'lion': '♌', 'virgo': '♍', 'libra': '♎',
                  'scorpio': '♏', 'sagittarius': '♐', 'capricorn': '♑', 'aquarius': '♒', 'pisces': '♓'}
    zodiac_sign = ['Овен', 'Телец', 'Близнецы', 'Рак', 'Лев', 'Дева',
                   'Весы', 'Скорпион', 'Стрелец', 'Козерог', 'Водолей', 'Рыбы']
    if message in zodiac_sign:
        if message == 'Овен':
            zodiac_icon = zodiac_map['aries']
            prediction = get_text('https://orakul.com/horoscope/astrologic/general/aries/today.html')
        elif message == 'Телец':
            zodiac_icon = zodiac_map['taurus']
            prediction = get_text('https://orakul.com/horoscope/astrologic/general/taurus/today.html')
        elif message == 'Близнецы':
            zodiac_icon = zodiac_map['gemini']
            prediction = get_text('https://orakul.com/horoscope/astrologic/general/gemini/today.html')
        elif message == 'Рак':
            zodiac_icon = zodiac_map['cancer']
            prediction = get_text('https://orakul.com/horoscope/astrologic/general/cancer/today.html')
        elif message == 'Лев':
            zodiac_icon = zodiac_map['lion']
            prediction = get_text('https://orakul.com/horoscope/astrologic/general/lion/today.html')
        elif message == 'Дева':
            zodiac_icon = zodiac_map['virgo']
            prediction = get_text('https://orakul.com/horoscope/astrologic/general/virgo/today.html')
        elif message == 'Весы':
            zodiac_icon = zodiac_map['libra']
            prediction = get_text('https://orakul.com/horoscope/astrologic/general/libra/today.html')
        elif message == 'Скорпион':
            zodiac_icon = zodiac_map['scorpio']
            prediction = get_text('https://orakul.com/horoscope/astrologic/general/scorpio/today.html')
        elif message == 'Стрелец':
            zodiac_icon = zodiac_map['sagittarius']
            prediction = get_text('https://orakul.com/horoscope/astrologic/general/sagittarius/today.html')
        elif message == 'Козерог':
            zodiac_icon = zodiac_map['capricorn']
            prediction = get_text('https://orakul.com/horoscope/astrologic/general/capricorn/today.html')
        elif message == 'Водолей':
            zodiac_icon = zodiac_map['aquarius']
            prediction = get_text('https://orakul.com/horoscope/astrologic/general/aquarius/today.html')
        elif message == 'Рыбы':
            zodiac_icon = zodiac_map['pisces']
            prediction = get_text('https://orakul.com/horoscope/astrologic/general/pisces/today.html')
        your_prediction = f''' Ежедневный голоскоп для знака зодиака {message}:
        {zodiac_icon}
    {prediction}'''
        return your_prediction
    else:
        return 'Введите знак зодиака кирилицей.\nПервая буква заглавная, остальные сторчные.\n'


# def run_schedules():
#     schedule.every().day.at('08:00').do(any_message)
#     schedule.every(10).seconds.do(any_message)
#     while True:
#         schedule.run_pending()
#         time.sleep(1)


@bot.message_handler(commands=['start'])
def start_message(message):
    print(message)
    bot.send_message(message.chat.id, f"Привет {message.chat.first_name} 🔮")
    time.sleep(1)
    bot.send_message(message.chat.id, f'Введите знак зодиака')


@bot.message_handler(regexp='.*')
def any_message(message):
    bot.send_message(message.chat.id, get_horoscope(message.text))


bot.infinity_polling()
