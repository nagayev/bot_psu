import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from config import *

#session = requests.Session()
login, password = config['login'],config['password']
app_id,secret=2685278,"hHbJug59sKJie78wjrH8"  # Kate Mobile App
vk_session = vk_api.VkApi(login, password,api_version="5.89",app_id=app_id, client_secret=secret)

try:
    vk_session.auth()
except vk_api.AuthError as error_msg:
    print('Ошибка с авторизацией - проверь логин и пароль')
    print('Полный текст:',error_msg)

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

surnames=['Аширбакиева', 'Байнов', 'Беляков', 'Бобер', 'Буренков', 
    'Верченко', 'Волков', 'Волков','Vorobyov', 'Голышев', 'Голянов', 'Жидков', 
    'Кокорев', 'Куликов', 'Мангутов', 'Манжурин', 'Нагаев', 
    'Сальников', 'Стексов', 'Филиппов', 'Щепелев']