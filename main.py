from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
#import string
#import random

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton('кнопка 1')
button_2 = KeyboardButton('кнопка 2')
button_3 = KeyboardButton('кнопка 3')
button_4 = KeyboardButton('кнопка 4')
keyboard.add(button_1, button_2, button_3, button_4)

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description='Команда для того, чтобы запустить бота'),
        types.BotCommand(command='/help', description='Команда для того, чтобы узнать с чем может помочь наш бот'),
        types.BotCommand(command='/marvel', description='Команда для того, чтобы узнать про героев')
    ]
    await bot.set_my_commands(commands)

#@dp.message_handler(commands=['description'])
#async def desc_command(message: types.Message):
   # await message.answer('Данная команда умеет отправлять рандомные символы латинского алфавита')
    #await message.delete()

#@dp.message_handler()
#async def send_random_letter(message: types.Message):
   # await  message.reply(random.choice(string.ascii_letters))

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет я твой первый бот!')
@dp.message_handler(commands='marvel')
async def marvel(message: types.Message):
    await message.answer('Выбери кнопку, я расскажу про супергероя и его способности..', reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == 'кнопка 1')
async def button_1_click(message: types.Message):
    await message.answer('Железный человек - Гений, миллиардер, плэйбой, филантроп.')
@dp.message_handler(lambda message: message.text == 'кнопка 2')
async def button_2_click(message: types.Message):
    await message.answer('Человек Паук - обладает необычайной силой и ловкостью, развиты рефлексы и чувство равновесия, умеет лазить стенам и потолку.')

@dp.message_handler(lambda message: message.text == 'кнопка 3')
async def button_3_click(message: types.Message):
        await message.answer('Капитан Америка - сила, выносливость, бессмертие, быстрая регенерация, мастерство скрытности и боя.')

@dp.message_handler(lambda message: message.text == 'кнопка 4')
async def button_4_click(message: types.Message):
            await message.answer('Доктор Стрэндж — обладает телепатией, навыками гипноза, способностью к телекинезу, умеет перемещаться в астрал и создавать иллюзии.')
@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.reply('Я помогу тебе..!')



@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup= on_startup)