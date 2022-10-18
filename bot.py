import vk_api
import config
from random import randint
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotEvent,VkBotMessageEvent
from vk_api.utils import get_random_id

token = config.settings['TOKEN']
group_id="216563568"

def write_message(chat, message):
    authorize.method('messages.send', {'chat_id': chat, 'message': message, 'random_id': get_random_id()})

authorize = vk_api.VkApi(token = token)


getting_api = authorize.get_api()
##аписосет

longpoll = VkBotLongPoll(authorize, group_id="216563568")
#write_message(1, "Бот запущен!"),
print("Бот запущен!")
for event in longpoll.listen():
     if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat and event.message.get('text'):
        reseived_message = event.message.get('text')

        chat = event.chat_id
        print('из чата', chat)
        from_id = event.message.get('from_id')
     if reseived_message == "Привет":
        print("пост2 отправлен в ", chat)
        write_message(chat, "Привет")






