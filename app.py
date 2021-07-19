from loader import dp
# from utils.set_bot_commands import bot_set_commands
from notify_admins import on_startup_notify


async def on_startup(dp):
    await on_startup_notify(dp)
    # await bot_set_commands(dp)

if __name__ == '__main__':
    from handlers import dp
    from aiogram import executor

    executor.start_polling(dp, on_startup=on_startup)
