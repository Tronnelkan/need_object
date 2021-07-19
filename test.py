from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command('start'))
async def show_info(message: types.Message):
    await message.answer('Приветствую тебя мой друг, как дела')


@dp.message_handler(text='плохо')
async def why(message: types.Message):
    await message.answer('Почему?')


@dp.message_handler(text='Жизнь сложная штука')
async def life(message: types.Message):
    await message.answer('Это да')