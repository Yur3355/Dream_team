import vk_api
import config
import re
import urllib
import json
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
import string

token = config.settings['TOKEN']    # присваиваем переменной значение токена из файла конфига
group_id="216563568"                # id выбранной для работы бота группы

def get_weather():
     # наш город на координатах широта=56.3264816, долгота=44.0051395
     # "https://api.openweathermap.org/data/2.5/weather?lat=56.3264816&lon=44.0051395&lang=ru&units=metric&appid=944b91c7a40842198fd6a61c32fe5453"
    end_point ="https://api.weatherbit.io/v2.0/current?lat=56.3264816&lon=44.0051395&lang=ru&units=M&key=" # запрос к апи weatherbit с параметрами долготы и широты,языка и системой мер
    key="679b7c2cbd8941de96caea3de21b8732"                  # ключ доступа
    url = end_point+ key                                    # создаем ссылку
    json_data = urllib.request.urlopen(url).read()          # читаем данные из JSON полученного из нашей ссылки
    data = json.loads(json_data)                            # загружаем их в переменную
    #print(data)
    current_weather =data['data'][0]                        # выбираем нужную нам часть с данными
    #print(current_weather['weather'])
    return current_weather                                  # возвращаем полученную информацию

def print_weather(current_weather):                         # функция получения текущего города
    city=current_weather['city_name']
    temp=current_weather['app_temp']
    desc=current_weather['weather']['description']
    wind=current_weather['wind_cdir_full']
    # print(city,'\n',desc,temp,'\n Ветер -',wind)
    weather=city+'\n'+desc+str(temp)+'\n'+"Ветер - "+wind
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

        if reseived_message == "нет":
            write_message(chat, "До свидания!")
       
        elif reseived_message == "да":
        
            write_message(chat, "Выберите период \n6 часов \nзавтра \n3 дня \nнеделя") 

            if reseived_message == "6часов":
                write_message(chat, "Ваш прогноз:")
                ##  вызов функции ## 

            elif reseived_message == "3дня":
                write_message(chat, "Ваш прогноз:")
                ##  вызов функции ##

            elif reseived_message == "неделя": 
                write_message(chat, "Ваш прогноз:")
                ##  вызов функции ##


for event in longpoll.listen():                               # ждем от сервера ответа о произошедшем событии
    if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat and event.message.get('text'): 
        # если тип ивента это новое сообщение, оно из чата и сообщение в ивенте текстовое
       
        reseived_message = event.message.get('text')            # то сохраняем полученное сообщение
        reseived_message.lower()                                # в нижний регистр
        reseived_message.translate({ord(c): None for c in string.whitespace})       # если было введено раздельно, убрали пробелы

        chat = event.chat_id                                    # сохраняем номер чата
        print('из чата', chat)
        from_id = event.message.get('from_id')
    
        menu(reseived_message)


    '''
     if reseived_message=="погода":
        print("Погода отправлена в ", chat)
        current = get_weather()
        write_message(chat, print_weather(current))
    '''
    