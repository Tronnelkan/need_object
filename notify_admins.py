import logging

from aiogram import Dispatcher

from data.config import admins
from aiogram.utils.markdown import hpre


async def on_startup_notify(dp: Dispatcher):
    for admin in admins:
        try:
            await dp.bot.send_message(admin, hpre('/Бот|запущен|какие|указы?|'))
        except Exception as err:
            logging.exception(err)