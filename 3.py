import telebot as tl
from telebot import types
import time
import sqlite3
bot = tl.TeleBot('5762048157:AAEBAjpvAQaJpqY278awgR9JrcY9zDe-w28')

#Рулетка
conn = sqlite3.connect('Rasp.db')
cur = conn.cursor()
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    user_id = message.from_user.id
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
        if int(time.strftime('%W')) % 2 == 0: #Четная неделя
            if time.strftime('%a') == 'Mon':
                bot.send_message(call.message.chat.id, '11:20 - 12:55:\n2)Информационная экология(л) --- Н - 344\n13:10 - 14:45:\n3)История инфокоммуникации(Бажин А.В., л) --- Н - 344\n15:25 - 17:00:\n4)Введение в профессию(Крылов Г.О., пр) --- Н - 344')
            elif time.strftime('%a') == 'Tue':
                bot.send_message(call.message.chat.id, '09:30 - 11:05:\n1)Физ-ра(Алескеров Р.Р.)\n11:20 - 12:55:\n2)Информационная экология(Ерофеева В.В., лаб) --- Н - 454\n13:10 - 14:45:\n3)Информационная экология(Ерофеева В.В., лаб) --- Н - 454')
            elif time.strftime('%a') == 'Wed':
                bot.send_message(call.message.chat.id, '11:20 - 12:55:\n2)Иностранный язык(Чупак Н.М., пр) --- Н - 516\n13:10 - 14:45:\n3)История инфокоммуникации(Бажин А.В., пр) --- Н - 428\n15:25 - 17:00:\n4)Философия(Кораблева Е.В., пр) --- Н - 330а')
            elif time.strftime('%a') == 'Thu':
                bot.send_message(call.message.chat.id, '09:30 - 11:05:\n1)Высшая математика(Данилов В.Г., л) --- Н - 224\n11:20 - 12:55:\n2)Иностранный язык(Чупак Н.М., пр) --- Н - 412\n13:10 - 14:45:\n3)Физ-ра(Алескеров Р.Р.)')
            elif time.strftime('%a') == 'Fri':
                bot.send_message(call.message.chat.id, '13:10 - 14:45:\n3)Физ-ра(Алескеров Р.Р.)\n15:25 - 17:00:\n4)Философия(Кораблева Е.В., л) --- Н - 344\n17:15 - 18:50:\n5)Сэпиб(Кораблева Е.В., л) --- Н - 308')
            elif time.strftime('%a') == 'Sat':
                bot.send_message(call.message.chat.id, '09:30 - 11:05:\n1)Введение в инф.технологии(Кудряшов  В.В., л) --- Н - 520\n11:20 - 12:55:\n2)Высшая математика(Данилов  В.Г., пр) --- Н - 450\n13:10 - 14:45:\n3)Введение в инф.технологии(Кудряшов  В.В., пр) --- Н - 520\n15:25 - 17:00:\n4)Введение в инф.технологии(Кудряшов  В.В., пр) --- Н - 520')
        else: #Нечетная неделя
            if time.strftime('%a') == 'Tue':
                bot.send_message(call.message.chat.id, '09:30 - 11:05:\n1)Введение в профессию(пр) --- А\n11:20 - 12:55:\n2)Введение в профессию(пр) --- А')
            elif time.strftime('%a') == 'Mon':
                bot.send_message(call.message.chat.id, '09:30 - 11:05:\n1)Введение в профессию(Крылов Г.О., пр) --- А - 425\n11:20 - 12:55:\n2)Введение в профессию(Крылов Г.О., л) --- А - 446')
            elif time.strftime('%a') == 'Wed':
                bot.send_message(call.message.chat.id, '11:20 - 12:55:\n2)Высшая математика(Данилов В.Г., пр) --- Н - 452\n13:10 - 14:45:\n3)Физ-ра(Алескеров Р.Р.)\n15:25 - 17:00:\n4)Сэпиб(Кораблева Е.В., пр) --- Н - 424\n17:15 - 18:50:\n5)Философия(Кораблева Е.В., пр) --- Н - 131')
            elif time.strftime('%a') == 'Thu':
                bot.send_message(call.message.chat.id, '09:30 - 11:05:\n1)История инфокоммуникации(Бажин А.В., л) --- Н - 344\n11:20 - 12:55:\n2)Высшая математика(Данилов В.Г., л) --- Н - 301\n13:10 - 14:45:\n3)Иностранный язык(Чупак Н.М., пр) --- Н - 406\n15:25 - 17:00:\n4)Философия(Кораблева Е.В., пр) --- Н - 131')
            elif time.strftime('%a') == 'Fri':
                bot.send_message(call.message.chat.id, '09:30 - 11:05:\n1)История инфокоммуникации(Бажин А.В., пр) --- Н - 450\n11:20 - 12:55:\n2)Информационная экология(Ерофеева В.В., лаб) --- Н - 454\n13:10 - 14:45:\n3)Сэпиб(Кораблева Е.В., пр) --- Н - 318\n15:25 - 17:00:\n4)Сэпиб(Кораблева Е.В., пр) --- Н - 318\n17:15 - 18:50:\n5)История инфокоммуникации(Бажин А.В., л) --- Н - 344')
            elif time.strftime('%a') == 'Sat':
                bot.send_message(call.message.chat.id, '09:30 - 11:05:\n1)Иностранный язык(Чупак Н.М., пр) --- Н - 406\n11:20 - 12:55:\n2)Введение в инф.технологии(Кудряшов  В.В., пр) --- Н - 520\n13:10 - 14:45:\n3)Физ-ра(Алескеров Р.Р.)\n15:25 - 17:00:\n4)Введение в инф.технологии(Кудряшов  В.В., л) --- Н - 344')
bot.polling(none_stop=True, interval=0)

