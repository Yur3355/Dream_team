import vk_api
import config
from random import randint
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotEvent,VkBotMessageEvent
from vk_api.utils import get_random_id
token = config.settings['TOKEN']
vktoken= config.settings['VKTOKEN']
group_id="214682553"
def write_message(chat, message):
    authorize.method('messages.send', {'chat_id': chat, 'message': message, 'random_id': get_random_id()})

authorize = vk_api.VkApi(token = token)
vk=vk_api.VkApi(token =vktoken)

getting_api = authorize.get_api()
getting_vk = vk.get_api()

longpoll = VkBotLongPoll(authorize, group_id="214682553")


#write_message(1, "Бот запущен!"),
print("Бот запущен!")

for event in longpoll.listen():
     if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat and event.message.get('text'):
        reseived_message = event.message.get('text')
        user_id=event.from_user
        chat = event.chat_id
        print('из чата',chat)
        from_id = event.message.get('from_id')
   #  if reseived_message == "мем":
        print("пост2 отправлен в ", user_id)
        write_message(chat, "Привет")





