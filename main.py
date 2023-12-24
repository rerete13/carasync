import asyncio
from tokens import Bot_token
from aiogram import F, Dispatcher, Bot



async def main() -> None:
    bot = Bot(Bot_token, parse_mode='HTML')
    dp = Dispatcher()
    
    
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

    
    

if __name__ == "__main__":
    asyncio.run(main())