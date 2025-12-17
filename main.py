import logging
import sqlite3
import random
import asyncio
import time
from aiogram import Bot, Dispatcher, executor, types
from datetime import datetime, timedelta
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from decimal import Decimal
from pycoingecko import CoinGeckoAPI

logging.basicConfig(level=logging.INFO)


bot = Bot(token="8248695769:AAHXlPQcCczH22zU0Z4a7uZnIsRZaZrY8EU")
dp = Dispatcher(bot)
api = CoinGeckoAPI()
connect = sqlite3.connect("users185.db")
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id BIGINT,
    skin_id INT,
    level INT,
    balance INT,
    bank BIGINT,
    deposit INT,
    bitkoin INT,
    Ecoins INT,
    energy INT,
    expe INT,
    games INT,
    user_name STRING,
    user_status STRING,
    deposit_status INT,
    rating INT,
    work INT,
    pet1 INT,
    pet2 INT,
    pet3 INT,
    pet4 INT,
    pet5 INT,
    pet6 INT,
    pet7 INT,
    pet8 INT,
    pet9 INT,
    pet10 INT,
    pet_name STRING,
    pet_hp INT,
    pet_eat INT,
    pet_mood INT,
    checking INT,
    checking1 INT,
    checking2 INT,
    checking3 INT,
    status_block STRING
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS mine(
    user_id BIGINT,
    user_name STRING,
    iron INT,
    gold INT,
    diamonds INT,
    amethysts INT,
    aquamarine INT,
    emeralds INT,
    matter INT,
    plasma INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS workshop(
    user_id BIGINT,
    user_name STRING,
    work_shop INT,
    workshop_c INT
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS farm(
    user_id BIGINT,
    user_name STRING,
    linen INT,
    cotton INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS property(
    user_id BIGINT,
    user_name STRING,
    have STRING,
    yacht INT,
    cars INT,
    plane INT,
    helicopter INT,
    house INT,
    phone INT,
    business INT,
    farm INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS bot(
    chat_id INT,
    last_stavka INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS bot_bonus(
    user_id INT,
    last_stavka INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS bot_merii(
    user_id INT,
    last_stavka INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS bot_work(
    user_id INT,
    last_stavka INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS bot_craft(
    user_id INT,
    last_stavka INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS ban_list(
    user_id INT,
    user_name STRING,
    Cause STRING
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS aleks_bot (
                            id INTEGER PRIMARY KEY,
                            name TEXT
)""")


cursor.execute("""CREATE TABLE IF NOT EXISTS chats_aleks (
                            chat_id INTEGER PRIMARY KEY,
                            chat_name TEXT
)""")


async def get_rang(message: types.Message):
    user = message.from_user
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user.id,))
    data = cursor.fetchone()
    return data


def UpdateUserValue(column, value, user_id):
    cursor.execute(f"UPDATE users SET {column} = {column} + ? WHERE user_id = ?", (value, user_id))


def UpdateUserValueMinus(value_name, value, user_id):
    cursor.execute(f"UPDATE users SET {value_name} = {value_name} - {value} WHERE user_id = {user_id}")


def InsertValues(user_name, user_id):
    cursor.execute("""INSERT INTO aleks_bot (name, id) VALUES (?, ?)""", (user_name, user_id))


def InsertChatValues(chat_id, chat_title):
    cursor.execute("""INSERT INTO chats_aleks (chat_id, chat_title) VALUES (?, ?)""", (chat_id, chat_title))


@dp.message_handler(commands=['sett'])
async def set_admins(message):
    cursor.execute("""UPDATE users SET user_status = 'Rab' WHERE user_id = 5169091087""")  
    connect.commit()
    
    
# start command
@dp.message_handler(commands=['stats'])
async def stats(message):
     user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
     user_name = str(user_name[0])
    
     sqlite_select_query = """SELECT * from users"""
     cursor.execute(sqlite_select_query)
     records = cursor.fetchall()

     await bot.send_message(message.chat.id, f"{user_name}, вот статистика бота  📊\n\n[🤵] Игроков: {len(records)}", parse_mode='html')


@dp.message_handler(commands=['start'])
async def start_cmd(message):
    msg = message
    pet_name = "name"
    user_id = msg.from_user.id
    user_name = msg.from_user.full_name
    user_status = "Player"
    have = 'off'
    status_block = 'off'
    chat_id = message.chat.id
    cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? , ? , ?, ? , ? , ? , ? , ? , ? , ? , ?);",
                       (user_id, 1, 1, 5000, 0, 0, 0, 0, 10, 0, 0, user_name, user_status, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, pet_name, 0, 0, 0, 0, 0, 0, 0, status_block))
        cursor.execute("INSERT INTO property VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
                       (user_id, user_name, have, 0, 0, 0, 0, 0, 0, 0, 0))
        cursor.execute("INSERT INTO mine VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
                       (user_id, user_name, 0, 0, 0, 0, 0, 0, 0, 0))
        cursor.execute("INSERT INTO farm VALUES(?, ?, ?, ?);", (user_id, user_name, 0, 0))
        cursor.execute("INSERT INTO workshop VALUES(?, ?, ?, ?);", (user_id, user_name, 0, 0))
        cursor.execute("INSERT INTO bot VALUES(?, ?);", (chat_id, 0))
        cursor.execute("INSERT INTO bot_bonus VALUES(?, ?);", (user_id, 0))
        cursor.execute("INSERT INTO bot_merii VALUES(?, ?);", (user_id, 0))
        cursor.execute("INSERT INTO bot_work VALUES(?, ?);", (user_id, 0))
        cursor.execute("INSERT INTO bot_craft VALUES(?, ?);", (user_id, 0))
        connect.commit()
    else:
        cursor.execute("INSERT INTO bot VALUES(?, ?);", (chat_id, 0))
        cursor.execute("INSERT INTO bot_bonus VALUES(?, ?);", (user_id, 0))
        cursor.execute("INSERT INTO bot_merii VALUES(?, ?);", (user_id, 0))
        cursor.execute("INSERT INTO bot_work VALUES(?, ?);", (user_id, 0))
        cursor.execute("INSERT INTO bot_craft VALUES(?, ?);", (user_id, 0))
        connect.commit()
        return

    name1 = message.from_user.get_mention(as_html=True)
    await message.reply(
        f' 🧙‍♂️Привет я HEOPSOV.\n\n{name1}\nЯ дал тебе подарок в размере 5.000$💸.\n\nℹЧто бы начать играть введите команду "Помощь"',
                         parse_mode='html')


@dp.message_handler(commands=['мут', 'mute'], commands_prefix='!?./', is_chat_admin=True)
async def mute(message):
   name1 = message.from_user.get_mention(as_html=True)
   if not message.reply_to_message:
      await message.reply("ℹ | Эта команда должна быть ответом на сообщение!")
      return
   try:
      muteint = int(message.text.split()[1])
      mutetype = message.text.split()[2]
      comment = " ".join(message.text.split()[3:])
   except IndexError:
      await message.reply('ℹ | Не хватает аргументов!\nПример:\n<code>/мут 1 ч причина</code>')
      return
   if mutetype == "ч" or mutetype == "часов" or mutetype == "час":
      dt = datetime.now() + timedelta(hours=muteint)
      timestamp = dt.timestamp()
      await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date = timestamp)
      await message.reply(f'[👤]  Администратор: {name1}\n[🛑] Замутил: <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\n[⏰] Срок: {muteint} {mutetype}\n[📃]  Причина: {comment}',  parse_mode='html')
   if mutetype == "м" or mutetype == "минут" or mutetype == "минуты":
      dt = datetime.now() + timedelta(minutes=muteint)
      timestamp = dt.timestamp()
      await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date = timestamp)
      await message.reply(f'[👤]  Администратор: {name1}\n[🛑] Замутил: <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\n[⏰] Срок: {muteint} {mutetype}\n[📃] Причина: {comment}',  parse_mode='html')
   if mutetype == "д" or mutetype == "дней" or mutetype == "день":
      dt = datetime.now() + timedelta(days=muteint)
      timestamp = dt.timestamp()
      await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date = timestamp)
      await message.reply(f'[👤]  Администратор: {name1}\n[🛑] Замутил: <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\n[⏰] Срок: {muteint} {mutetype}\n[📃] Причина: {comment}',  parse_mode='html')


@dp.message_handler(commands=['размут', 'unmute'], commands_prefix='!?./', is_chat_admin=True)
async def unmute(message):
   name1 = message.from_user.get_mention(as_html=True)
   if not message.reply_to_message:
      await message.reply("[ℹ] Эта команда должна быть ответом на сообщение!")
      return
   await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(True, True, True, True))
   await message.reply(f'[👤]  Администратор: {name1}\n[🔊] Размутил: <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>',  parse_mode='html')


@dp.message_handler(commands=['ban', 'бан', 'кик', 'kick'], commands_prefix='!?./', is_chat_admin=True)
async def ban(message):
   name1 = message.from_user.get_mention(as_html=True)
   if not message.reply_to_message:
      await message.reply("[ℹ] Эта команда должна быть ответом на сообщение!")
      return
   comment = " ".join(message.text.split()[1:])
   await bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False))
   await message.reply(f'[👤]  Администратор: {name1}\n[🛑] Забанил: <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\n[⏰] Срок: навсегда\n[📃] Причина: {comment}',  parse_mode='html')


@dp.message_handler(commands=['разбан', 'unban'], commands_prefix='!?./', is_chat_admin=True)
async def unban(message):
   name1 = message.from_user.get_mention(as_html=True)
   if not message.reply_to_message:
      await message.reply("ℹ | Эта команда должна быть ответом на сообщение!")
      return
   await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(True, True, True, True))
   await message.reply(f'[👤]  Администратор: {name1}\n[📲] Разбанил: <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>',  parse_mode='html')


# prof_user
@dp.message_handler(commands=['info'])
async def info_user(message: types.Message):
    data = await get_rang(message)
    if data is None:
        return await message.reply(f"🚫 <b>Не найден в базе данных.</b>\n\n"

                                   f"Напишите /start в чат!")
    user_id = message.reply_to_message.from_user.id
    user_name = message.reply_to_message.from_user.full_name
    skin_id = cursor.execute("SELECT skin_id from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
    skin_id = int(skin_id[0])
    level = cursor.execute("SELECT level from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
    level = int(level[0])
    balance = cursor.execute("SELECT balance from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
    balance = int(balance[0])
    bank = cursor.execute("SELECT bank from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
    bank = int(bank[0])
    deposit = cursor.execute("SELECT deposit from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
    deposit = int(deposit[0])
    bitkoin = cursor.execute("SELECT bitkoin from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
    bitkoin = int(bitkoin[0])
    Ecoins = cursor.execute("SELECT Ecoins from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
    Ecoins = int(Ecoins[0])
    rating = cursor.execute("SELECT rating from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
    rating = int(rating[0])
    user_status_reply = cursor.execute("SELECT user_status from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
    user_status_reply = str(user_status_reply[0])
    user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
    user_status = str(user_status[0])
    name = message.from_user.get_mention(as_html=True)

    if user_status_reply == 'Player':
        user_status_reply2 = '[💤] Игрок'
    if user_status_reply == 'Admin':
        user_status_reply2 = '[👔] Администратор'
    if user_status_reply == 'Rab':
        user_status_reply2 = '[✅] Разработчик'

    balance2 = '{:,}'.format(balance)
    bank2 = '{:,}'.format(bank)
    Ecoins2 = '{:,}'.format(Ecoins)
    rating2 = '{:,}'.format(rating)
    bitkoin2 = '{:,}'.format(bitkoin)
    deposit2 = '{:,}'.format(deposit)
    if user_status == 'Rab':
        await bot.send_message(message.chat.id, f'''
{name}, вот вся информация про игрока:

    [👫] Ник: {user_name}
    [🔎] ID: {user_id}
    [👕] Skin_ID: {skin_id}
    [💰] Деньги: {balance2}$
    [🏛] Банк: {bank2}$
    [📧] E-coins: {Ecoins2}
    [👑] Рейтинг: {rating2} 
    [🏪] Депозит: {deposit2}
    [💽] Биткоины: {bitkoin2}
    [🧊] Префикс: {user_status_reply2}
''', parse_mode='html')
        return
    if user_status == 'Admin':
        await bot.send_message(message.chat.id, f'''
{name}, вот вся информация про игрока:

    [👫] Ник: {user_name}
    [🔎] ID: {user_id}
    [👕] Skin_ID: {skin_id}
    [💰] Деньги: {balance2}$
    [🏛] Банк: {bank2}$
    [👑] Рейтинг: {rating2} 
    [💽] Биткоины: {bitkoin2}
    [🧊] Статус: {user_status_reply2}
''', parse_mode='html')
        return
    else:
        await bot.send_message(message.chat.id, f'{name}, Доступ к данной команде ограничен. Для покупки администратора обратитесь к создателю 👨‍🦰', parse_mode='html')


@dp.message_handler(commands=['ping', 'пинг'], commands_prefix=["/", "!"])
async def ping(message: types.Message):
    data = await get_rang(message)
    if data is None:
        return await message.reply(f"🚫 <b>Не найден в базе данных.</b>\n\n"

                                   f"Напишите /start в чат!")
    a = time.time()
    bot_msg = await message.answer(f'⚙ Проверка пинга....')
    if bot_msg:
        b = time.time()
        await bot_msg.edit_text(f'PING.. BOTS: {round((b - a) * 1000)} ms')


@dp.message_handler(lambda t: t.text.startswith("Шанс"))
async def fff(message: types.Message):
    data = await get_rang(message)
    if data is None:
        return await message.reply(f"🚫 <b>Не найден в базе данных.</b>\n\n"

                                   f"Напишите /start в чат!")
    h = ["37%","20%","29%","10%","100%","21%,","22%","52%","55%","2%","6%","8%"]
    g = random.choice(h)
    await message.reply(f"""🎰 | шанс этого | {g} """)


@dp.message_handler(lambda t: t.text.startswith("Шар"))
async def fff(message: types.Message):
    data = await get_rang(message)
    if data is None:
        return await message.reply(f"🚫 <b>Не найден в базе данных.</b>\n\n"

                                   f"Напишите /start в чат!")
    h = ["⚡️возможно","⚡️нет","⚡️да","⚡️нет","нет⚡️","⚡️да","⚡️нет"]
    g = random.choice(h)
    await message.reply(f"""🎱 | шар думает что: | {g} """)


@dp.message_handler(lambda t: t.text.startswith("Выбери"))
async def fff(message: types.Message):
    data = await get_rang(message)
    if data is None:
        return await message.reply(f"🚫 <b>Не найден в базе данных.</b>\n\n"

                                   f"Напишите /start в чат!")
    h = ["я выбираю первый вариант","я выбраю второй вариант","не могу определить","второй вариант лучше","первый вариант лучше"]
    g = random.choice(h)
    await message.reply(f"""🎱 | {g} """)


@dp.message_handler(lambda msg: msg.text.lower() == 'бот') 
async def check_bot(message):
    data = await get_rang(message)
    if data is None:
        return await message.reply(f"🚫 <b>Не найден в базе данных.</b>\n\n"

                                   f"Напишите /start в чат!")
    await message.reply('✅Бот работает!')


@dp.message_handler(lambda msg: msg.text.lower().startswith('+'))
async def plus_rep(message):
   if not message.reply_to_message:
      await message.reply("Эта команда должна быть ответом на сообщение!")
      return
   if message.from_user.id == message.reply_to_message.from_user.id:
      await message.reply("А нельзя накручивать себе репутацию!🖕")
      return
   UpdateUserValue('reputation', 1, message.reply_to_message.from_user.id)
   connect.commit()
   await message.reply("Повышение репутации засчитано👍")


@dp.message_handler(lambda msg: msg.text.lower().startswith('-'))
async def minus_rep(message):
   if not message.reply_to_message:
      await message.reply("Эта команда должна быть ответом на сообщение!")
      return
   if message.from_user.id == message.reply_to_message.from_user.id:
      await message.reply("А нельзя накручивать себе репутацию!🖕")
      return
   UpdateUserValueMinus('reputation', 1, message.reply_to_message.from_user.id)
   connect.commit()
   await message.reply("Понижение репутации засчитано👎")               


@dp.message_handler(commands=['r', 'report'])
async def report(message: types.Message):
    try:
        if message.text in ['/report', '/r'] or not message.reply_to_message:
            await bot.send_message(message.chat.id, '''Вот информация за систему репортов ⛔️

⚠️ | Правила по использованию репортов
[1️⃣] Материться, оскорблять кого-либо, проявлять неуважение к администрации и тому подобное.
[2️⃣] Капсить, писать неразборчиво, использовать спам, писать один и тот-же текст несколько раз получивши на него ответ.
[3️⃣] Всячески дразнить администрацию и отвлекать от работы.
[4️⃣] Запрещено интересоваться/писать вещи которые ни коем образом ни относятся к игре
[5️⃣] Запрещена реклама в любом её проявлении
[6️⃣] Запрещено обращаться к своим друзьям администраторам по личным вопросам
7️⃣ | Запрещено клеветать на игроков, обвинять их в нарушениях, которые они не совершали.
[8️⃣] Репорт работает по принципу - Вопрос/Просьба/Жалоба (исключение - Приветствие) и не иначе. Иные формы обращения будут оставаться без ответа и будет выдано наказание.

[⚠️] | Форма отправки репорта - /report [сообщение]

[⛔️] | Прошу вас соблюдать правила отправки репорта''')
        else:
            members = await message.chat.get_member(message.reply_to_message.from_user.id)
            info = await bot.get_chat_member(message.chat.id, message.from_user.id)
            report = message.text.replace('/r ', '')
            report = report.replace('/report ', '')
            admins = await bot.get_chat_administrators('@' + message.chat.username)
            send = 0
            for admin in admins:
                if admin.user.username != 'Group_Moder_bot':
                    try:
                        await bot.send_message(admin.user.id, f'[📬] | Репорт по причине: {str(report)}\n\nhttps://t.me/{message.chat.username}/{message.reply_to_message.message_id}')
                    except:
                        pass
                    send += 1

            if send == 0:
                await bot.send_message(message.chat.id, '[👮] | Админы не оповещены, для отправки им репортов надо, чтобы они запустили меня в лс!')
            else:
                await bot.send_message(me
