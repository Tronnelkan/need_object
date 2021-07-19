from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.utils.markdown import hlink, hcode

from data import config
from data.Items import items
from keyboards.inline.buy_keyboard import buy_keyboard
from keyboards.inline.paid_keyboard import paid_keyboard
from loader import dp
from utils.misc.payment import Payment, NotFoundPayment, NotEnoughMoney


@dp.message_handler(Command('Items'))
async def show_menu(message: types.Message):
    caption = """
    <b>{title}</b>
    <b>{description}</b>
    <b>{price:.2f}RUB</b>
    """
    for item in items:
        await message.answer_photo(photo=item.photo_link, caption=caption.format(title=item.title,
                                                                                 description=item.description,
                                                                                 price=item.price),
                                   reply_markup=buy_keyboard(item_id=item.id))


@dp.callback_query_handler(text_contains='buy')
async def create_invoice(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    item_id = call.data.split(':')[-1]
    item_id = int(item_id) - 1
    item = items[item_id]
    amount = item.price
    comment = str()

    payment = Payment(amount=amount)
    payment.create()

    await call.message.answer(
        '\n'.join(
            [
                f'Оплатите {amount:.2f} по номеру телефона',
                hlink(config.QIWI_WALLET, url=payment.invoice),
                "И обязательно увведите ID платежа:",
                hcode(payment.id)
            ]
        ),
        reply_markup=paid_keyboard
    )
    await state.set_state('qiwi')
    await state.update_data(payment=payment)


@dp.callback_query_handler(text='cancel', state='qiwi')
async def cancel(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.edit_text('Отменено')
    await state.finish()


@dp.callback_query_handler(text='paid', state='qiwi')
async def paid(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    data = await state.get_data()
    payment: Payment = data.get('payment')
    try:
        payment.check_payment()
    except NotFoundPayment:
        await call.message.answer('Транзакция не найдена')
        return
    except NotEnoughMoney:
        await call.message.answer('Недостаточно средств для транзакции')
        return
    else:
        await call.message.answer('Успешно оплачено')
        await call.message.delete_reply_markup()
        await state.finish()
