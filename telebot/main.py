import telebot
# from .keyboard import keyboard

TOKEN = '5397810445:AAFGBxRaKoAi4BkFUfS3P910LFKYiCwRkvE'

bot = telebot.TeleBot(TOKEN)

start = telebot.types.ReplyKeyboardMarkup(True, True)
start.row('Да', 'Нет')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Вы хотите узнать подробнее о продуктах университета?', reply_markup=start)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')


bot.polling()
