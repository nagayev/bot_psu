from config import config

def log(text:str)->None:
    print(f'[LOG] {text}')

def command_from_text(text:str)->str:
    text=text[3:] #remove бот
    text=text.lstrip(',')
    text=text.strip()
    #log(f'command is {text}')
    return text 

def get_sorted_families(vk,id:str):
    """
    ids=vk.messages.getConversationMembers(peer_id=id)['items']
    ids=[i['member_id'] for i in ids]
    surnames=[]
    for id in ids:
        surname=vk.users.get(user_ids=id)[0]['last_name']
        surnames.append(surname)
    print(sorted(surnames))
    """
    #use default list
    return ['Аширбакиева', 'Байнов', 'Беляков', 'Бобер', 'Буренков', 
    'Верченко', 'Волков', 'Волков','Vorobyov', 'Голышев', 'Голянов', 'Жидков', 
    'Кокорев', 'Куликов', 'Мангутов', 'Манжурин', 'Нагаев', 
    'Сальников', 'Стексов', 'Филиппов', 'Щепелев']

list_of_members=[0 for i in range(21)]
def handle_commands(vk,event,command:str):
    #log(f'Command:{command}')
    families=get_sorted_families(vk,config['id'])
    if command=='я сдал':
        try:
            surname=vk.users.get(ids=str(event.user_id))[0]['last_name']
            index=families.index(surname)
            if index==len(families):
                vk.messages.send(chat_id=event.chat_id,message='Скайп закончен')
                return 
            next=families[index+1]
            global list_of_members
            list_of_members[index]=1
            print(list_of_members)
            vk.messages.send(chat_id=event.chat_id,message=f'{surname} сдал, следующий - {next}')
        except Exception as e:
            print('[ERROR]',e)
    elif command=='список':
        print('список',list_of_members)
        message=['Скайп\n']
        for i in range(len(list_of_members)):
            member=list_of_members[i]
            if member==0:
                message.append(f'{families[i]} еще ❌\n')
            else:
                message.append(f'{families[i]} уже ✓\n')
        message=''.join(message)
        vk.messages.send(chat_id=event.chat_id,message=message)
    elif command=='помощь':
        vk.messages.send(chat_id=event.chat_id,message='я сдал - отмечает, список - выводит список сдавших и нет')
    else:
        vk.messages.send(chat_id=event.chat_id,message=f'Не понял, что ты сказал\nСправка: бот помощь')