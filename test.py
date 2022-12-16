import sqlite3
import telebot #pip install pyTelegramBotAPI
from telebot import types
import function


bot = telebot.TeleBot("TOKEN HERE")
@bot.message_handler(commands=["start"])
def start_fun(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Разработчик", callback_data="razrabot")
    markup.add(button1)
    bot.send_message(message.chat.id, "Привет, этот бот общения, напиши мне сообщение и я попытаюсь его понять.",reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    req = call.data
    if req == 'razrabot':
        msg = bot.send_message(call.message.chat.id, "Разработчик данного бота @ifwhwifjqoqijhqwoiqiowoiwqoiqo13") 

@bot.message_handler(content_types = 'text')
def any_msg(message):
    if(message.text.split('-')[0] == "/add"):
        mess = message.text.split('-')[1]
        #Пример: /add-все ли работает?|Да. Все работает
        function.AddNew(mess.split('|')[0], mess.split('|')[1])
        bot.send_message(message.chat.id, "Успешно добавлено новое словосочетание")
    else:
        if(function.check_user(message.from_user.id)):
            otvet = function.select(message.text)
            if(otvet == None):
                bot.send_message(message.chat.id, "Я не знаю что на это ответить")
            else:
                bot.send_message(message.chat.id, otvet)
            
function.create()
bot.infinity_polling()
