from config import config
from constants import *
from sys import stdout

LOG = False
LOG_FILE = stdout 

def log(text:str)->None:
    if LOG: 
        print(f'[LOG] {text}',filename=LOG_FILE)

def command_from_text(text:str)->str:
    text=text[3:] #remove бот
    text=text.lstrip(',')
    text=text.strip()
    #log(f'command is {text}')
    return text 

def get_sorted_families(vk,id:str):
    ids=vk.messages.getConversationMembers(peer_id=id)['items']
    ids=[str(i['member_id']) for i in ids]
    surnames_raw=vk.users.get(user_ids=','.join(ids))
    #print(surnames_raw)
    surnames=[id['last_name'] for id in surnames_raw]
    ban=['Юркалова','Пряничникова','Vorobyov']
    for surname in surnames:
        if surname in ban:
            surnames.remove(surname)
    surnames.insert(2,'Воробьев')
    return sorted(surnames)

list_of_members=[0 for i in range(21)]
def handle_commands(vk,event,command:str):
    #log(f'Command:{command}')
    families=get_sorted_families(vk,config['peer_id'])
    if command=='я сдал':
        try:
            surname=vk.users.get(ids=str(event.user_id))[0]['last_name']
            index=families.index(surname)
            """
            if index==len(families):
                vk.messages.send(chat_id=event.chat_id,message='Скайп закончен')
                return
            """ 
            next=families[index+1]
            global list_of_members
            list_of_members[index]=1
            log(f'members: {list_of_members}')
            #vk.messages.send(chat_id=event.chat_id,message=f'{surname} сдал, следующий - {next}')
            log(f'{surname},{next}')
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