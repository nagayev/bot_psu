from vk_api.longpoll import VkLongPoll, VkEventType
from config import config
from utils import *
import vk_api
import requests

session = requests.Session()
login, password = config['login'],config['password']
id,secret=2685278,"hHbJug59sKJie78wjrH8"  # Kate Mobile App
vk_session = vk_api.VkApi(login, password,api_version="5.89",app_id=id, client_secret=secret)

try:
    vk_session.auth()
except vk_api.AuthError as error_msg:
    print('Ошибка с авторизацией - проверь логин и пароль')
    print('Полный текст:',error_msg)

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
print('Бот запущен!')

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.text:
        event.text=event.text.lower()
        print(dir(event))
        #event.from_user is bool
        print(event.user_id,event.peer_id)
        exit(0)
        user=event.user_id
        #print(event.text)
        toBot = event.text.startswith('бот') or event.text.startswith('252168745|@m.nagayev]')
        if toBot:
            command=command_from_text(event.text)
            handle_commands(vk,event,command)