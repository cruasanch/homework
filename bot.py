import telebot
import requests
import os
from sqlite3 import connect
from skimage.io import imshow, imread

if "my_db.db" not in os.listdir():
    with connect("my_db.db") as con:
        con.execute("""create table users(user_id int, user_name text, user_lastname text)""")

token = "=)"
bot = telebot.TeleBot(token)

def createbutton(field, message, flag = False):
    markup = telebot.types.InlineKeyboardMarkup()

    call_data1 = telebot.types.InlineKeyboardButton(text=chr(8592), callback_data=1)
    call_data2 = telebot.types.InlineKeyboardButton(text=chr(8593), callback_data=2)
    call_data3 = telebot.types.InlineKeyboardButton(text=chr(8594), callback_data=3)
    call_data4 = telebot.types.InlineKeyboardButton(text=chr(8595), callback_data=4)

    markup.add(call_data1)
    markup.add(call_data2)
    markup.add(call_data3)
    markup.add(call_data4)

    if not flag:
        bot.send_message(message.chat.id, field, reply_markup = markup)
    else:
        bot.edit_message_text(chat_id=message.chat.id,\
                                  message_id=message.message_id, text=field, reply_markup = markup)

pole = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]



@bot.message_handler(commands=['login'])
def login(message):
    add = True
    with connect("my_db.db") as con:
        cur = con.cursor()
        cur.execute("""SELECT user_id FROM users WHERE {} = user_id""".format(message.chat.id))
        for row in cur.fetchall():
            add = False
        if add:
            con.execute("""INSERT INTO users(user_id, user_name, user_lastname) VALUES(?,?,?)""",\
                       (message.chat.id, message.from_user.first_name, message.from_user.last_name))
            bot.send_message(message.chat.id, "регистрация прошла успешно")
        else:
            bot.send_message(message.chat.id, "вы уже зареганы")





@bot.message_handler(content_types=['photo'])
def photo(message):
    file_id = message.photo[-1].file_id

    path = bot.get_file(file_id).file_path

    url = 'https://api.telegram.org/file/bot{}/{}'.format(token, path)

    req = requests.get(url)

    with open(url.split("/")[-1], "wb") as img:
        img.write(req.content)


@bot.message_handler(commands=['start'])
def start(message):
    pole[3][3] = 1
    pole2str = "\n".join([str(i) for i in pole])
    createbutton(pole2str, message)




@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global pole
    y = [sum(i) for i in pole].index(1)
    x = pole[y].index(1)
    if call.message:
        pole[y][x] = 0
        if call.data == '1':
            x -= 1
        elif call.data == '2':
            y -= 1
        elif call.data == '3':
            x += 1
        elif call.data == '4':
            y += 1
        pole[y%5][x%5] = 1
        pole2str = "\n".join([str(i) for i in pole])
        createbutton(pole2str, call.message, "add")

bot.polling(none_stop=True)