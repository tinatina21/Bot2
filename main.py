from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#import string
#import random

from database.database import initialize_db, add_user, get_user

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

initialize_db()

keyboard_inline1 = InlineKeyboardMarkup(row_width= 1)
but_inline = InlineKeyboardButton('Посмотреть', url= 'https://www.marvel.com/movies/iron-man')
keyboard_inline1.add(but_inline)


keyboard_inline2 = InlineKeyboardMarkup(row_width= 1)
but_inline2 = InlineKeyboardButton('Посмотреть', url= 'https://www.marvel.com/games/marvel-s-spider-man')
keyboard_inline2.add(but_inline2)

keyboard_inline3 = InlineKeyboardMarkup(row_width= 1)
but_inline3 = InlineKeyboardButton('Посмотреть', url= 'https://www.marvel.com/movies/captain-america-the-first-avenger')
keyboard_inline3.add(but_inline3)

keyboard_inline4 = InlineKeyboardMarkup(row_width= 1)
but_inline4 = InlineKeyboardButton('Посмотреть', url= 'https://www.marvel.com/movies/doctor-strange')
keyboard_inline4.add(but_inline4)


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
    user = get_user(message.from_user.id)
    if user is None:
        add_user(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)
        await message.answer('Привет я твой первый бот!', reply_markup=keyboard)
    else:
        await message.answer('Привет я твой первый бот!', reply_markup=keyboard)
@dp.message_handler(commands='marvel')
async def marvel(message: types.Message):
    await message.answer('Выбери кнопку, я расскажу про супергероя и его способности..', reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == 'кнопка 1')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id,photo='https://images.hdqwalls.com/wallpapers/avengers-iron-man-4k-b3.jpg', caption='Железный человек - Гений, миллиардер, плэйбой, филантроп.', reply_markup= keyboard_inline1)
@dp.message_handler(lambda message: message.text == 'кнопка 2')
async def button_2_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://i.pinimg.com/originals/1a/7f/2b/1a7f2bd7465dc634091877e90fcc14ff.jpg',
                         caption='Человек Паук - обладает необычайной силой и ловкостью, развиты рефлексы и чувство равновесия, умеет лазить стенам и потолку.', reply_markup= keyboard_inline2 )

@dp.message_handler(lambda message: message.text == 'кнопка 3')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://klike.net/uploads/posts/2023-01/1674376895_3-19.jpg',caption='сила, выносливость, бессмертие, быстрая регенерация, мастерство скрытности и боя.',
        reply_markup=keyboard_inline2)
@dp.message_handler(lambda message: message.text == 'кнопка 4')
async def button_4_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://www.goodthingsguy.com/wp-content/uploads/2018/06/doctor-strange-1864x1279.jpg', caption='Доктор Стрэндж — обладает телепатией, навыками гипноза, способностью к телекинезу, умеет перемещаться в астрал и создавать иллюзии.', reply_markup= keyboard_inline4)



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