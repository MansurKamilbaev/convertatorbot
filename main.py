import telebot

from buttons import menu_buttons

bot = telebot.TeleBot('6717597402:AAFWypDJJJHQ-9Yt1_O1xYY8H5dajbdkbwI')


@bot.message_handler(commands=['start'])
def message_handler(message):
    user_id = message.from_user.id
    buttons = menu_buttons()

    user = bot.send_message(user_id, 'Выберите валюту для конвертации: ', reply_markup=buttons)
    bot.register_next_step_handler(user, usd_eur)


def usd_eur(message):
    user_id = message.from_user.id
    convert = message.text

    if convert == "USD/EUR":
        bot.send_message(user_id, 'Введите сумму USD, которая конверитруется в EUR:')
        bot.register_next_step_handler(message, convertatin_usd_eur)

    elif convert == 'EUR/USD':
        bot.send_message(user_id, 'Введите сумму EUR,которая конверитруется в USD')
        bot.register_next_step_handler(message, convertatin_eur_usd)

    elif convert == 'RUB/USD':
        bot.send_message(user_id, 'Введите сумму RUB, которая конверитруется в USD')
        bot.register_next_step_handler(message, convertatin_rub_usd)

    elif convert == 'USD/RUB':
        bot.send_message(user_id, 'Введите сумму USD, которая конверитруется в RUB')
        bot.register_next_step_handler(message, convertatin_usd_rub)

    elif convert == "UZS/USD":
        bot.send_message(user_id, "Введите сумму в UZS, которая конвертируется в USD:")
        bot.register_next_step_handler(message, convertatin_uzs_usd)

    elif convert == "USD/UZS":
        bot.send_message(user_id, "Введите сумму в USD, которая конвертируется в UZS:")
        bot.register_next_step_handler(message, convertatin_usd_uzs)

    elif convert == "UZS/RUB":
        bot.send_message(user_id, "Введите сумму в UZS, которая конвертируется в RUB:")
        bot.register_next_step_handler(message, convertatin_uzs_rub)

    elif convert == "RUB/UZS":
        bot.send_message(user_id, "Введите сумму в RUB, которая конвертируется в UZS:")
        bot.register_next_step_handler(message, convertatin_rub_uzs)

    elif convert == "RUB/EUR":
        bot.send_message(user_id, "Введите сумму в RUB, которая конвертируется в EUR:")
        bot.register_next_step_handler(message, convertatin_rub_eur)

    elif convert == "EUR/RUB":
        bot.send_message(user_id, "Введите сумму в EUR, которая конвертируется в RUB:")
        bot.register_next_step_handler(message, convertatin_eur_rub)

    else:
        bot.send_message(user_id, "Бот не сможет конвертировать эту пару валют!")


def convertatin_usd_eur(message):
    user_id = message.from_user.id
    usd_amount = float(message.text)
    convertor = usd_amount * 0.91
    bot.send_message(user_id, f"{usd_amount} USD = {convertor} EUR")

    buttons = menu_buttons()
    bot.send_message(user_id, "Выберите другую пару валют: ", reply_markup=buttons)
    bot.register_next_step_handler(message, usd_eur)


def convertatin_eur_usd(message):
    user_id = message.from_user.id
    eur_amount = float(message.text)
    convertor = eur_amount * 1.09
    bot.send_message(user_id, f"{eur_amount} EUR = {convertor} USD")

    buttons = menu_buttons()
    bot.send_message(user_id, "Выберите другую пару валют: ", reply_markup=buttons)
    bot.register_next_step_handler(message, usd_eur)


def convertatin_rub_usd(message):
    user_id = message.from_user.id
    rub_amount = float(message.text)
    convertor = rub_amount * 0.0111
    bot.send_message(user_id, f"{rub_amount} RUB = {convertor} USD")

    buttons = menu_buttons()
    bot.send_message(user_id, "Выберите другую пару валют: ", reply_markup=buttons)
    bot.register_next_step_handler(message, usd_eur)


def convertatin_usd_rub(message):
    user_id = message.from_user.id
    usd_amount = float(message.text)
    convertor = usd_amount * 90.09
    bot.send_message(user_id, f"{usd_amount} USD = {convertor} RUB")
    buttons = menu_buttons()
    bot.send_message(user_id, "Выберите другую пару валют: ", reply_markup=buttons)
    bot.register_next_step_handler(message, usd_eur)

def convertatin_uzs_usd(message):
    user_id = message.from_user.id
    uzs_amount = float(message.text)
    convertor = uzs_amount * 0.000081
    bot.send_message(user_id, f"{uzs_amount} UZS = {convertor} USD")

    buttons = menu_buttons()
    bot.send_message(user_id, "Выберите другую пару валют: ", reply_markup=buttons)
    bot.register_next_step_handler(message, usd_eur)


def convertatin_usd_uzs(message):
    user_id = message.from_user.id
    usd_amount = float(message.text)
    convertor = usd_amount * 1238.69
    bot.send_message(user_id, f"{usd_amount} USD = {convertor} UZS")

    buttons = menu_buttons()
    bot.send_message(user_id, "Выберите другую пару валют: ", reply_markup=buttons)
    bot.register_next_step_handler(message, usd_eur)


def convertatin_uzs_rub(message):
    user_id = message.from_user.id
    uzs_amount = float(message.text)
    convertor = uzs_amount * 0.0072
    bot.send_message(user_id, f"{uzs_amount} UZS = {convertor} RUB")

    buttons = menu_buttons()
    bot.send_message(user_id, "Выберите другую пару валют: ", reply_markup=buttons)
    bot.register_next_step_handler(message, usd_eur)


def convertatin_rub_uzs(message):
    user_id = message.from_user.id
    rub_amount = float(message.text)
    convertor = rub_amount * 137.5
    bot.send_message(user_id, f"{rub_amount} RUB = {convertor} UZS")

    buttons = menu_buttons()
    bot.send_message(user_id, "Выберите другую пару валют: ", reply_markup=buttons)
    bot.register_next_step_handler(message, usd_eur)


def convertatin_rub_eur(message):
    user_id = message.from_user.id
    rub_amount = float(message.text)
    convertor = rub_amount * 0.010
    bot.send_message(user_id, f"{rub_amount} RUB = {convertor} EUR")

    buttons = menu_buttons()
    bot.send_message(user_id, "Выберите другую пару валют: ", reply_markup=buttons)
    bot.register_next_step_handler(message, usd_eur)


def convertatin_eur_rub(message):
    user_id = message.from_user.id
    eur_amount = float(message.text)
    convertor = eur_amount * 97.45
    bot.send_message(user_id, f"{eur_amount} EUR = {convertor} RUB")

    buttons = menu_buttons()
    bot.send_message(user_id, "Выберите другую пару валют: ", reply_markup=buttons)
    bot.register_next_step_handler(message, usd_eur)


bot.infinity_polling()
