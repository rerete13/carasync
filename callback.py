from aiogram import types, Router, types, F
from bot_func import is_user_subscribed
from btns import menu_keyboard_btn, inline_user_subscribe_start, inline_menu_btn, inline_keyboard_call, more_response_btn, top_car_btn, city_repaire_choose_btn, inline_keyboard_url
from data_func import create_user_data_mongo, get_info_about_mongo
from another_info import all_comments, top_cars_sales
from bot_func import create_city_repaire_service_call, get_count_days_mongo
from get_car_info import get_comment_number_bazagai
from american_info import get_american_car_info
from asyncio import sleep
from time import sleep as block_sleep
from aiogram.types import LabeledPrice


router = Router()




@router.callback_query(F.data == 'back')
async def callback_return(callback: types.callback_query):
    await callback.bot.edit_message_text(message_id=callback.message.message_id, chat_id=callback.message.chat.id, text='Меню', reply_markup=inline_menu_btn())



@router.callback_query(F.data == 'sub_check')
async def callback_return(callback: types.callback_query):
    if await is_user_subscribed(callback.message) == True:
        await callback.bot.delete_message(message_id=callback.message.message_id, chat_id=callback.message.chat.id)
        # await create_user_data(callback.message, 'user-data')
        await create_user_data_mongo(callback.message)
        await callback.message.answer("<b>Введіть номер у такій формі:</b> AA7777AA", reply_markup=menu_keyboard_btn())
        
    else:
        await callback.message.answer("<b>Підпишися на канал:</b>🏎 @autopars3", reply_markup=inline_user_subscribe_start())



@router.callback_query(F.data.startswith("respons_"))
async def callbacks_num(callback: types.CallbackQuery):
    action = callback.data.split("_")[1]

    await callback.bot.edit_message_text(message_id=callback.message.message_id, chat_id=callback.message.chat.id, text='⏳ Це може зайняти деякий час...')
    
    if action == "3":
        out = ''
        for i in range(3):
            # This comment clarifies that you are awaiting the all_comments(i) coroutine and then accessing the first element of the resulting list. It can serve as a helpful reminder for anyone reading the code, including yourself in the future, about the purpose of that specific line.
            out += (await all_comments(i))[0] + '\n\n'

        out += '\n\n Інформація надана від: @autoparse_bot'
            
        await callback.bot.edit_message_text(message_id=callback.message.message_id, chat_id=callback.message.chat.id, text=out, reply_markup=more_response_btn())

        
    if action == "9":
        out = ''
        for i in range(9):
            out += (await all_comments(i))[0] + '\n\n'

        out += '\n\n Інформація надана від: @autoparse_bot'
            
        await callback.bot.edit_message_text(message_id=callback.message.message_id, chat_id=callback.message.chat.id, text=out, reply_markup=inline_keyboard_call(text='Назад ⭕️', call='back'))



@router.callback_query(F.data.startswith("top_car_"))
async def callbacks_num(callback: types.CallbackQuery):
    action = callback.data.split("_")[2]

    await callback.bot.edit_message_text(message_id=callback.message.message_id, chat_id=callback.message.chat.id, text='⏳ Це може зайняти деякий час...')
    
    if action == "10":
        out = ''
        info = (await top_cars_sales())
        for i in range(10):
            out += info[i] + '\n'

        out += '\n\n Інформація надана від: @autoparse_bot'
            
        await callback.bot.edit_message_text(message_id=callback.message.message_id, chat_id=callback.message.chat.id, text=out, reply_markup=top_car_btn())

        
    if action == "50":
        out = ''
        info = (await top_cars_sales())
        for i in range(50):
            out += info[i] + '\n'

        out += '\n\n Інформація надана від: @autoparse_bot'
            
        await callback.bot.edit_message_text(message_id=callback.message.message_id, chat_id=callback.message.chat.id, text=out, reply_markup=inline_keyboard_call(text='Назад ⭕️', call='back'))



@router.callback_query(F.data == 'repairs')
async def callback_return(callback: types.callback_query):
    await callback.bot.edit_message_text(message_id=callback.message.message_id, chat_id=callback.message.chat.id, text='Виберіть місто', reply_markup= (await city_repaire_choose_btn()))
    


@router.callback_query(F.data.startswith("city_"))
async def callbacks_num(callback: types.CallbackQuery):
    action = callback.data.split("_")[1]

    await callback.bot.edit_message_text(message_id=callback.message.message_id, chat_id=callback.message.chat.id, text='⏳ Це може зайняти деякий час...')
    
    if action == 'kyiv':
        await create_city_repaire_service_call(callback, 0)
        
    if action == 'kyivob':
        await create_city_repaire_service_call(callback, 1)
        
    if action == 'vinnycia':
        await create_city_repaire_service_call(callback, 2)
        
    if action == 'dnipro':
        await create_city_repaire_service_call(callback, 4)
        
    if action == 'frankivsk':
        await create_city_repaire_service_call(callback, 10)
         
    if action == 'lviv':
        await create_city_repaire_service_call(callback, 13)
                
    if action == 'odesa':
        await create_city_repaire_service_call(callback, 15)
        
    if action == 'poltava':
        await create_city_repaire_service_call(callback, 16)
        
    if action == 'kharkiv':
        await create_city_repaire_service_call(callback, 21)
        
    if action == 'hmelnyck':
        await create_city_repaire_service_call(callback, 23)
        
    if action == 'cherkasy':
        await create_city_repaire_service_call(callback, 24)
        
        

@router.callback_query(F.data == 'info')
async def callback_return(callback: types.callback_query):
    await callback.bot.edit_message_text(message_id=callback.message.message_id, chat_id=callback.message.chat.id, text='info', reply_markup=inline_keyboard_call(text='Назад ⭕️', call='back'))
    
    
    
@router.callback_query(F.data == 'owner')
async def callback_return(callback: types.callback_query):
    await callback.bot.edit_message_text(message_id=callback.message.message_id, chat_id=callback.message.chat.id, text="<b>Bласник:</b> @rerete13\n\nНа їжу:\n<code>4441111132314539</code> \n\n<b>USDT (TRC20)</b> \n<code>TVSrox5rnjdK7Y2WL4dji3qyfb9yGb616f</code> \n\n <b>BTC (BTC)</b> \n<code>bc1qsmy29mvt4gmfuex8xscalvnu5vfg6hjaf796ph</code>", reply_markup=inline_keyboard_call(text='Назад ⭕️', call='back'))

    
    
@router.callback_query(F.data.startswith("v_"))
async def callback_return(callback: types.callback_query):
    action = callback.data.split("_")[1]
    
    if action != 'None':
        await callback.bot.edit_message_text(message_id=callback.message.message_id, chat_id=callback.message.chat.id, text=f"Vincode: \n<code>{action}</code>\n\n Інформація надана від: @autoparse_bot", reply_markup=inline_keyboard_call(' Пошук по Америці', f'a_{action}'))

    else:
        await callback.bot.edit_message_text(message_id=callback.message.message_id, chat_id=callback.message.chat.id, text=f'Vincode не знайдено')
        
    
    
@router.callback_query(F.data.startswith("c_"))
async def callback_return(callback: types.callback_query):
    await callback.bot.edit_message_text(message_id=callback.message.message_id, chat_id=callback.message.chat.id, text='⏳ Це може зайняти деякий час...')
    action = callback.data.split("_")[1]
    
    try:
        comments = await get_comment_number_bazagai(action)
        comments_sorted = ''
        
        for i in comments:
            comment = f'\n<b>Автор:</b> {i[0]}\n<b>Коментар:</b>\n{i[1]}\n<b>Дата публікації:</b> \n{i[2]}\n'
            comments_sorted += comment
            
        await callback.bot.edit_message_text(message_id=callback.message.message_id, chat_id=callback.message.chat.id, text=f'Коментарії до автомобільного номера: \n\n<code>{action}</code>\n{comments_sorted}\n\n Інформація надана від: @autoparse_bot')
    
    except:
        await callback.bot.edit_message_text(message_id=callback.message.message_id, chat_id=callback.message.chat.id, text=f'Коментарії до автомобільного номера: \n\n<code>{action}</code>\n\n <b>Не знайдено</b>')
            
    
    
@router.callback_query(F.data.startswith("a_"))
async def callback_return(callback: types.callback_query):
    action = callback.data.split("_")[1]
    if action != 'None':
        
        await callback.bot.edit_message_text(message_id=callback.message.message_id, chat_id=callback.message.chat.id, text=f'<code>{action}</code>\n Cкопіюйте та перейдіть за посиланням\n\n Інформація надана від: @autoparse_bot', reply_markup=inline_keyboard_url('Перейти ✈️', 'https://shre.su/0YEO'))
        
    #     try:
    #         await callback.bot.edit_message_text(message_id=callback.message.message_id, chat_id=callback.message.chat.id, text=f'{callback.message.text}')
            
    #         wait = await callback.message.answer('⏳ Це може зайняти деякий час...')
            
    #         photos, car_details, car_info = (await get_american_car_info(action))
            
    #         await callback.bot.delete_message(message_id=wait.message_id, chat_id=callback.message.chat.id)
            
    #         wait = await callback.message.answer('Ваш запит формується')
            
    #         block_sleep(5)
            
    #         for img in photos:
    #             await callback.message.answer_photo(img)
            
    #         cd = ''
    #         for i in car_details:
    #             cd += i + '\n'
                
    #         ci = ''
    #         for i in car_info:
    #             ci += i + '\n'
                
    #         await callback.message.answer(f'{cd}\n{ci}\n\nІнформація надана від: @autoparse_bot')
            
            
            
    #     except:
    #         await callback.bot.edit_message_text(message_id=wait.message_id, chat_id=callback.message.chat.id, text=f'Mашини з vincode: {action}\n не найдено по американських базах даних')
        

    # else:
    #     await callback.bot.edit_message_text(message_id=wait.message_id, chat_id=callback.message.chat.id, text=f'Mашини з vincode: {action}\n не найдено по американських базах даних')
        
        
        
@router.callback_query(F.data == 'account')
async def callback_return(callback: types.callback_query):
    await callback.bot.edit_message_text(message_id=callback.message.message_id, chat_id=callback.message.chat.id, text='⏳ Це може зайняти деякий час...')
    
    id = int(callback.message.chat.id)
    days = (await get_count_days_mongo(id))
    languige = (await get_info_about_mongo(id, 'info', 'language'))
    findings_count = (await get_info_about_mongo(id, 'findings', None))
    findings_count = len(findings_count)
    count_premium_requests = (await get_info_about_mongo(id, 'subscribe', 'count'))
    sub_date = (await get_info_about_mongo(id, 'subscribe', 'count'))
    status = (await get_info_about_mongo(id, 'subscribe', 'status'))
    lotery_tikets = (await get_info_about_mongo(id, 'info', 'try-to-win'))
    
    
    text = f"""
👤 Мій акаунт: {id} \n\n
📝 Мова: {languige} \n
⏳ Вік облікового запису: {days}  \n
🔗 Кількість запитів: {findings_count} \n\n
🎰 Квитків: {lotery_tikets} \n
💸 Преміум запити: {count_premium_requests} \n
🔑 Залишок преміум підписки: {sub_date} \n
📇 Статус: {status}
"""
    
    await callback.bot.edit_message_text(message_id=callback.message.message_id, chat_id=callback.message.chat.id, text=text, reply_markup=inline_keyboard_call(text='Назад ⭕️', call='back'))





