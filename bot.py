import vk_api
import config
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id

token = config.settings['TOKEN']    # присваиваем переменной значение токена из файла конфига
group_id="216563568"                # id выбранной для работы бота группы

def write_message(chat, message):       # функция отправки сообщения в чат ,получает его номер и сообщение
    authorize.method('messages.send', {'chat_id': chat, 'message': message, 'random_id': get_random_id()})
    # используем функцию внутри апи по отправки сообщений,принимающую номер чата,сообщение и рандомный id

authorize = vk_api.VkApi(token = token)  # авторизируем бота через токен
getting_api = authorize.get_api()
longpoll = VkBotLongPoll(authorize, group_id="216563568")    # отправляем запрос на сервер с помощью технологии long polling
print("Бот запущен!")
for event in longpoll.listen():                               # ждем от сервера ответа о произошедшем событии
     if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat and event.message.get('text'): # если тип ивента это новое сообщение,оно из чата и сообщение в ивенте текстовое
        reseived_message = event.message.get('text')          # то сохраняем полученное сообщение

        chat = event.chat_id        # сохраняем номер чата
        print('из чата', chat)
        from_id = event.message.get('from_id')
     if reseived_message == "Привет":
        print("пост2 отправлен в ", chat)
        write_message(chat, "Привет")






