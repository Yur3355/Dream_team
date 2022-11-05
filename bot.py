import vk_api
import config
import re
import urllib
import json
import requests as req
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
import string

token = config.settings['TOKEN']    # присваиваем переменной значение токена из файла конфига
group_id="216563568"                # id выбранной для работы бота группы

def get_weather(period,):
     # наш город на координатах широта=56.3264816, долгота=44.0051395
     # "https://api.openweathermap.org/data/2.5/weather?lat=56.3264816&lon=44.0051395&lang=ru&units=metric&appid=944b91c7a40842198fd6a61c32fe5453"
    if period==1:
        end_point ="https://api.weatherbit.io/v2.0/current?lat=56.3264816&lon=44.0051395&lang=ru&units=M&key=" # запрос к апи weatherbit с параметрами долготы и широты,языка и системой мер
        key="679b7c2cbd8941de96caea3de21b8732"                  # ключ доступа
    elif period==7:
       end_point = "https://api.weatherbit.io/v2.0/forecast/daily?lat=56.3264816&lon=44.0051395&lang=ru&units=M&key="  # запрос к апи с погодой на следующие 7 дней
       key = "679b7c2cbd8941de96caea3de21b8732"
    elif period == 3:
       url_yandex = 'https://api.weather.yandex.ru/v2/forecast/?lat=56.3264816&lon=44.0051395&lang=ru_RU&limit=3'
       yandex_req = req.get(url_yandex, headers={'X-Yandex-API-Key': "36217aea-b2d9-42ef-aaad-0839da8faa04"},
                            verify=False)
       yandex_json = json.loads(yandex_req.text)
       print(yandex_json)
    elif period == 6:
       end_point = "апи"
       key = "вставить токен апи"

#    url = end_point+key                                    # создаем ссылку
#    json_data = urllib.request.urlopen(url).read()          # читаем данные из JSON полученного из нашей ссылки
    current_weather= json.loads(yandex_req.text)                            # загружаем их в переменную

    return current_weather                                  # возвращаем полученную информацию

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

def print_weather(data,period,i):      # функция получения текущего города
    # print(data)
   # current_weather = data['data'][i]  # выбираем нужную нам часть с данными
   # print(data['data'][i])
    current_weather = data['forecasts'][i]
    #date = current_weather['datetime']
   # desc = current_weather['weather']['description']
   # wind = current_weather['wind_cdir_full']
    #wind_spd = current_weather['wind_spd']
    #wind_spd = toFixed(wind_spd, 2)
    if period==1:
        city=current_weather['city_name']
        temp = current_weather['app_temp']

        weather = date + '\n' + desc + ' - ' + str(temp) + 'C \n' + "Ветер - " + wind+'\nСкорость ветра - '+ str(wind_spd)+' м/с'
    elif period==7:
        temp = current_weather['app_max_temp']

        weather = date + '\n' + desc + ' - ' + 'макс. температура - ' + str(temp) + 'C \n' + "Ветер - " +wind+'\nСкорость ветра - '+ str(wind_spd)+' м/с'
    elif period == 6 or 3:

        date = current_weather['date']
        temp = current_weather['parts']['morning']['temp_avg']
        wind = current_weather['parts']['morning']['wind_speed']
        wind_dir = current_weather['parts']['morning']['wind_dir']
        weather = date + '\n' + 'температура - ' + str(temp) + 'C \n' + "Ветер - " + wind_dir + '\nСкорость ветра - ' + str(
            wind) + ' м/с'
    # print(city,'\n',desc,temp,'\n Ветер -',wind)
   # print(weather)
    return weather

def write_message(chat, message):                           # функция отправки сообщения в чат ,получает его номер и сообщение
    authorize.method('messages.send', {'chat_id': chat, 'message': message, 'random_id': get_random_id()})
    # используем функцию внутри апи по отправки сообщений,принимающую номер чата,сообщение и рандомный id

authorize = vk_api.VkApi(token = token)                        # авторизируем бота через токен
getting_api = authorize.get_api()
longpoll = VkBotLongPoll(authorize, group_id="216563568")      # отправляем запрос на сервер с помощью технологии long polling
print("Бот запущен!")

def menu(reseived_message):

    if reseived_message=="привет":    
        write_message(chat, "Вас приветствует бот прогноза погоды. Хотите узнать прогноз? \nда \nнет")

    elif reseived_message == "нет":
        write_message(chat, "До свидания!")

    elif reseived_message == "да":
        write_message(chat, "Выберите период \n6 часов \nзавтра \n3 дня \nнеделя \nтекущая")

    if reseived_message == "6часов":
        write_message(chat, "Ваш прогноз:")
        print("Погода на 6 часов отправлена в ", chat)
        hours = get_weather(6) 
        write_message(chat, print_weather(hours,6))

    elif reseived_message == "3дня":
        write_message(chat, "Ваш прогноз:")
        print("Погода на 3 дня отправлена в ", chat)
        days = get_weather(3)
        for i in range(3):
         write_message(chat, print_weather(days,3,i))

    elif reseived_message == "неделя":
        print("Погода на неделю отправлена в ", chat)
        write_message(chat, "Ваш прогноз:")
        week = get_weather(7)
        for i in range(7):
         write_message(chat, print_weather(week,7,i))

    elif reseived_message == "текущая":
        print("Текущая погода отправлена в ", chat)
        write_message(chat, "Ваш прогноз:")
        current = get_weather(1)
        write_message(chat, print_weather(current,1,0))



for event in longpoll.listen():                               # ждем от сервера ответа о произошедшем событии
    if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat and event.message.get('text'): 
        # если тип ивента это новое сообщение, оно из чата и сообщение в ивенте текстовое
       
        reseived_message = event.message.get('text')            # то сохраняем полученное сообщение                                      # в нижний регистр
        reseived_message=reseived_message.translate({ord(c): None for c in string.whitespace})       # если было введено раздельно, убрали пробелы

        chat = event.chat_id                                    # сохраняем номер чата да
        print('из чата', chat)
        from_id = event.message.get('from_id')
        menu(reseived_message.lower())
