import telebot as tl
bot = tl.TeleBot('5762048157:AAEBAjpvAQaJpqY278awgR9JrcY9zDe-w28')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/Start":
        bot.send_message(message.from_user.id, "Выбери чем хочешь заняться?\n1)Игра в рулетку\n2)Расписание на завтра")
        keyboard = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Да', callback_data='yes')
        keyboard.add(key1)
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key_no)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Привет, я бот, который поможет тебе коротать твое время или собраться на завтра!Для начала напиши /Start.")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=0)
