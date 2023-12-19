from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def menu_buttons():
    buttons = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    button1 = KeyboardButton("USD/EUR")
    button2 = KeyboardButton("EUR/USD")
    button3 = KeyboardButton("RUB/USD")
    button4 = KeyboardButton("USD/RUB")
    button5 = KeyboardButton("UZS/USD")
    button6 = KeyboardButton("USD/UZS")
    button7 = KeyboardButton("UZS/RUB")
    button8 = KeyboardButton("RUB/UZS")
    button9 = KeyboardButton("RUB/EUR")
    button10 = KeyboardButton("EUR/RUB")

    buttons.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10)

    return buttons
