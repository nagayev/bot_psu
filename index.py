from constants import vk
from utils import *

log('Бот запущен!')

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.text:
        event.text=event.text.lower()
        log(dir(event))
        #event.from_user is bool, peer_id это id беседы
        log(event.user_id)
        user=event.user_id
        toBot = event.text.startswith('бот') or event.text.startswith('252168745|@m.nagayev]')
        if toBot:
            command=command_from_text(event.text)
            handle_commands(vk,event,command)