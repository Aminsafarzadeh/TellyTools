import telebot
from telebot import types
from API_Holder import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    """
    Handles /start command. Say hello and show options.
    """
    bot.send_message(message.chat.id, text="سلام به Telly Tools خوش اومدی 👋")
    start_buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
    verify_buttons = types.KeyboardButton(text="تایید شماره کاربر", request_contact=True)
    start_buttons.add("تبدیل عکس به PDF", "تبدیل لینک به QR", "ایجاد فایل ZIP", "حذف بکگراند عکس","تاببد شماره همراه", verify_buttons)
    bot.send_message(message.chat.id, text="چکار میتونم برات انجام بدم؟ 😊", reply_markup=start_buttons)


@bot.message_handler(commands=['help'])
def help(message):
    pass


bot.infinity_polling()
