import telebot


bot = telebot.TeleBot('1446473769:AAEI5XlIHW56g0yl-reM6x1ZP3ciy8MfOB8')


@bot.message_handler(commands=['start'])
def do_start(message):
    # global keyboard1
    # keyboard1 = telebot.types.ReplyKeyboardMarkup()
    # keyboard1.row('/короткое', '/длинное')
    bot.send_message(message.chat.id, 'Бот декодер \n'
                                      'Пришли мне голосовое сообщение или песню, \n'
                                      'а я постараюсь превратить его в текст!')
    #                                   'а я буду следить чтобы они не протухли)', reply_markup=keyboard1)
    # создание клавиатуры


# функция подсказки пользователю
@bot.message_handler(content_types=['text'])
def mess(message):
    bot.send_message(message.chat.id, 'текст')


@bot.message_handler(content_types=['audio'])
def mess(message):
    bot.send_message(message.chat.id, 'аудио')


@bot.message_handler(content_types=['voice'])
def mess(message):
    bot.send_message(message.chat.id, 'войс')


if __name__ == '__main__':
    bot.polling(none_stop=True)
