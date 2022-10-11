import telebot as tl
from telebot import types
import time

bot = tl.TeleBot('5762048157:AAEBAjpvAQaJpqY278awgR9JrcY9zDe-w28')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/Start":
        keyboard = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Игра в рулетку', callback_data='Play')
        keyboard.add(key1)
        key2 = types.InlineKeyboardButton(text='Расписание', callback_data='Table')
        keyboard.add(key2)
        bot.send_message(message.from_user.id, text="Выбери чем хочешь заняться?\n1)Игра в рулетку\n2)Расписание на завтра", reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Привет, я бот, который поможет тебе коротать твое время или собраться на завтра!Для начала напиши /Start.")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "Play": 
        bot.send_message(call.message.chat.id, 'Начинаем игру')
    elif call.data == "Table":
        bot.send_message(call.message.chat.id, 'Ищу расписание')

bot.polling(none_stop=True, interval=0)
