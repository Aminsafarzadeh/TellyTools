import telebot
from telebot import types
from API_Holder import API_TOKEN
import qr_maker
import zip_maker
import rmbg_maker

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
    start_buttons.add("Convert Image to PDF", "Make QR from Link", "ZIP My File", "Remove Photo Background",
                      "Add Black & White to My Photo", verify_buttons)
    bot.send_chat_action(message.chat.id, action="typing")
    bot.send_message(message.chat.id, text="What can I do for you? 😊", reply_markup=start_buttons)


def menu():
    pass


@bot.message_handler(commands=['help'])
def help(message):
    pass


@bot.message_handler(func=lambda m: m.text == "Convert Image to PDF")
def pdf(message):
    pass


@bot.message_handler(func=lambda m: m.text == "Make QR from Link")
@bot.message_handler(commands=['qrmaker'])
def qr_request(message):
    bot.send_chat_action(message.chat.id, action="typing")
    bot.send_message(message.chat.id, text="Ok 👍")
    bot.send_chat_action(message.chat.id, action="typing")
    link = bot.send_message(message.chat.id, text="Now sending me your link or text to do it for you🤝")
    bot.register_next_step_handler(link, make_qr)


def make_qr(message):
    bot.send_chat_action(message.chat.id, action='upload_document')
    image = bot.send_document(message.chat.id, qr_maker.qrcode(message.text))
    bot.send_chat_action(message.chat.id, action="typing")
    bot.reply_to(image, text="Here's your QR! ☝️☝️")
    bot.send_chat_action(message.chat.id, action="typing")
    button1 = types.InlineKeyboardButton("Make QR agein", callback_data='qr_request')
    button2 = types.InlineKeyboardButton("Take me to the start", callback_data='start')
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    markup.add(button1, button2)
    bot.send_message(message.chat.id, text="What else should I do? 🫡",
                     reply_markup=markup)
    qr_maker.empty_temp()


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'qr_request':
        qr_request(call.message)
    elif call.data == 'zip_request':
        zip_request(call.message)
    elif call.data == 'rmbg_request':
        rmbg_request(call.message)
    elif call.data == 'start':
        start(call.message)


@bot.message_handler(func=lambda m: m.text == "ZIP My File")
def zip_request(message):
    bot.send_chat_action(message.chat.id, action="typing")
    user_file = bot.send_message(message.chat.id,
                                 text="Ok, send me your file to see its zip 🤐\nIf you send me media like image or "
                                      "video note send them in file format without compression")
    bot.register_next_step_handler(user_file, make_zip)


def make_zip(message):
    file_path = bot.get_file(message.document.file_id).file_path
    downloaded_file = bot.download_file(file_path)
    zip_file = zip_maker.zipfile(message.document.file_name, downloaded_file)
    bot.send_chat_action(message.chat.id, action='upload_document')
    file = bot.send_document(message.chat.id, zip_file)
    bot.send_chat_action(message.chat.id, action="typing")
    bot.reply_to(file, text="Here's your Zip File! ☝️☝️")
    button1 = types.InlineKeyboardButton("Make Zip agein", callback_data='zip_request')
    button2 = types.InlineKeyboardButton("Take me to the start", callback_data='start')
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    markup.add(button1, button2)
    bot.send_message(message.chat.id, text="What else should I do? 🫡",
                     reply_markup=markup)
    zip_maker.empty_temp()


@bot.message_handler(func=lambda m: m.text == "Remove Photo Background")
def rmbg_request(message):
    bot.send_chat_action(message.chat.id, action="typing")
    user_photo = bot.send_message(message.chat.id, text="Ok, send me your photo to me 🏞")
    bot.register_next_step_handler(user_photo, make_rmbg)


def make_rmbg(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    image = rmbg_maker.remover(downloaded_file)
    bot.send_chat_action(message.chat.id, action='upload_photo')
    photo = bot.send_photo(message.chat.id, image)
    bot.reply_to(photo, text="Here's your photo without background! ☝️☝️")
    button1 = types.InlineKeyboardButton("Remove background ", callback_data='rmbg_request')
    button2 = types.InlineKeyboardButton("Take me to the start", callback_data='start')
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    markup.add(button1, button2)
    bot.send_message(message.chat.id, text="What else should I do? 🫡",
                     reply_markup=markup)


@bot.message_handler(func=lambda m: m.text == "تبدیل عکس به PDF")
def pdf(message):
    pass


@bot.message_handler(func=lambda m: m.text == "تبدیل عکس به PDF")
def pdf(message):
    pass


if __name__ == '__main__':
    bot.infinity_polling()
