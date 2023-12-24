import json
import os
import datetime
from aiogram import Bot
from tokens import Bot_token

bot = Bot(Bot_token)


async def create_user_data(message, folder_name:str):
    
    file_name = f"{message.from_user.id}"
    if os.path.exists(f'{folder_name}/{file_name}.json'):
        pass
    else:
        # User does not exist, create new data
        member = await bot.get_chat_member(chat_id='@autopars3', user_id=message.from_user.id)
        
        now = datetime.datetime.now()
        time_now = str(now.strftime("%d-%m-%Y %H:%M:%S"))
        
        
        user_info = {
                "id": message.from_user.id,
                "first-name":  message.chat.first_name,
                "last-name": message.chat.last_name,
                "user-name": message.chat.username,
                "member-type": str(member.status.name),
                "user-number": None,
                "info": {
                        "findings-count": 0,
                        "bot-start": time_now,
                        "language": "UKR",
                        "try-to-win": 1
                },
                "subscribe": {
                        "count": 0,
                        "sub-date": 0,
                        "status": False
                    },
                "promo-histoty":[],
                "topup-history": [],
                "findings": []
        }

        # Create new JSON file for user
        with open(f'{folder_name}/{file_name}.json', "w", encoding='utf-8') as f:
            json.dump(user_info, f, indent=4, ensure_ascii=False)



async def add_user_data(path, data_update_path:str, new_data, data_update_path_in:str == None):
    with open(f"{path}.json", "r") as f:
        data = json.load(f)

    now = datetime.datetime.now()
    time_now = str(now.strftime("%d-%m-%Y %H:%M:%S"))


    if data_update_path_in == None:

        link_user_info = time_now, new_data

        data[f"{data_update_path}"].append(link_user_info)
        
    else:
        link_user_info = time_now, new_data

        data[f"{data_update_path}"][f"{data_update_path_in}"] = new_data


    with open(f"{path}.json", "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def get_info_about(user:str, data_id, data_id_in=None):
    with open(f"{user}.json", "r") as f:
        data = json.load(f)
        
        if data_id_in == None:
            return_data = data[f"{data_id}"]
            return return_data
        else:
            return_data = data[f"{data_id}"][f"{data_id_in}"]
            return return_data
        
        
        
def change_user_data(path:str, data_update_path:str, new_data, data_update_path_in:str == None):
    with open(f"{path}.json", "r") as f:
        data = json.load(f)

    if data_update_path_in == None:

        data[f"{data_update_path}"] == new_data
        
    else:

        data[f"{data_update_path}"][f"{data_update_path_in}"] == new_data

    with open(f"{path}.json", "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)



