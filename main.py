import asyncio
from tokens import Bot_token
from aiogram import F, Dispatcher, Bot
import commands, callback, text_commands


async def main() -> None:
    bot = Bot(Bot_token, parse_mode='HTML')
    dp = Dispatcher()
    
    dp.include_router(commands.router)
    dp.include_router(text_commands.router)
    dp.include_router(callback.router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

    
    

if __name__ == "__main__":
    asyncio.run(main())