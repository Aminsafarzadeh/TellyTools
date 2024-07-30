import telebot
from telebot import types
from API_Holder import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    """
    Handles /start command. Say hello and show options.
    """
    bot.send_message(message.chat.id, text="Hey, welcome to Telly Tools👋")
    start_buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
    verify_buttons = types.KeyboardButton(text="Verify My Number", request_contact=True)
    start_buttons.add("Convert Image to PDF", "Make QR from Link", "ZIP My Files", "Remove Photo Background","Add Black & White to My Photo", verify_buttons)
    bot.send_message(message.chat.id, text="What can I do for you? 😊", reply_markup=start_buttons)


@bot.message_handler(commands=['help'])
def help(message):
    pass

@bot.message_handler(func= lambda m: m.txt == "Convert Image to PDF")
def pdf(message):
    pass


@bot.message_handler(func= lambda m: m.txt == "Make QR from Link")
def pdf(message):
    pass


@bot.message_handler(func= lambda m: m.txt == "ZIP My Files")
def pdf(message):
    pass


@bot.message_handler(func= lambda m: m.txt == "Remove Photo Background")
def pdf(message):
    pass


@bot.message_handler(func= lambda m: m.txt == "تبدیل عکس به PDF")
def pdf(message):
    pass


@bot.message_handler(func= lambda m: m.txt == "تبدیل عکس به PDF")
def pdf(message):
    pass


bot.infinity_polling()
