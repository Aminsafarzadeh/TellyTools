import telebot
from telebot import types
from API_Holder import API_TOKEN
from qr_maker import qrcode

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    """
    Handles /start command. Say hello and show options.

    :param message: start command
    :return: None
    """

    bot.send_chat_action(message.chat.id, action="typing")
    bot.send_message(message.chat.id, text="Hey, this is Telly Tools👋\nYour lovely toolbox 😇")
    start_buttons = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    verify_buttons = types.KeyboardButton(text="Verify My Number", request_contact=True)
    start_buttons.add("Convert Image to PDF", "Make QR from Link", "ZIP My Files", "Remove Photo Background","Add Black & White to My Photo", verify_buttons)
    bot.send_chat_action(message.chat.id, action="typing")
    bot.send_message(message.chat.id, text="What can I do for you? 😊", reply_markup=start_buttons)


@bot.message_handler(commands=['help'])
def help(message):
    pass

@bot.message_handler(func= lambda m: m.text == "Convert Image to PDF")
def pdf(message):
    pass


@bot.message_handler(func= lambda m: m.text == "Make QR from Link")
@bot.message_handler(commands=['qrmaker'])
def qr_request(message):
    bot.send_chat_action(message.chat.id, action="typing")
    bot.send_message(message.chat.id, text="Ok 👍")
    bot.send_chat_action(message.chat.id, action="typing")
    link = bot.send_message(message.chat.id, text="Now sending me your link or text to do it for you🤝")
    bot.register_next_step_handler(link, qr_maker)


def qr_maker(message):
    bot.send_chat_action(message.chat.id, action='upload_document')
    image = bot.send_document(message.chat.id,qrcode(message.text))
    bot.send_chat_action(message.chat.id, action="typing")
    bot.reply_to(image, text="Here's your QR! ☝️☝️")
    bot.send_chat_action(message.chat.id, action="typing")
    button1 = types.InlineKeyboardButton("Make QR agein", callback_data='qr_request')
    button2 = types.InlineKeyboardButton("Take me to the start", callback_data='start')
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    markup.add(button1, button2)
    bot.send_message(message.chat.id, text="What else should I do? 🫡", reply_markup=markup)  # main menu and replay (inline button)



@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    if call.data == 'qr_request':
        qr_request(call.message)
    elif call.data == 'start':
        start(call.message)


@bot.message_handler(func= lambda m: m.text == "ZIP My Files")
def pdf(message):
    pass


@bot.message_handler(func= lambda m: m.text == "Remove Photo Background")
def pdf(message):
    pass


@bot.message_handler(func= lambda m: m.text == "تبدیل عکس به PDF")
def pdf(message):
    pass


@bot.message_handler(func= lambda m: m.text == "تبدیل عکس به PDF")
def pdf(message):
    pass


bot.infinity_polling()
