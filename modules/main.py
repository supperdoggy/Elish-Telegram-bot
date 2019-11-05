import telebot
from modules.server import denied_id
from modules import administrator
from modules.type import markups
from modules.type import buttons
import datetime
from modules.Data.check import CheckPermission


def maincode(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        if CheckPermission(message) == "User":
            # Якшо касир пише
            bot.reply_to(message, "Касова програма")

            markups.type.type_main(bot, message)
            denied_id.log(message)
        elif CheckPermission(message) == "Admin":
            bot.reply_to(message, "Касова програма")

            # Якшо адмін пише
            markups.type.type_admin(bot, message)
            denied_id.log(message)
        else:
            # Якщо id не сходиться, то не допускається до роботи з ботом
            print(message.chat.id, 'Access denied')
            denied_id.deny(message)

    @bot.message_handler(commands=['help'])
    def help(message):
        if CheckPermission(message):
            bot.send_message(message.chat.id,
                             'Касова програма на заказ "Еліш", доступ сторого для обмеженого кола користувачів')
            bot.send_message(message.chat.id, 'З`єднайтеся з @supperdoggy, для додаткової інформації')
            denied_id.log(message)
        else:
            print(message.chat.id, 'Access denied')
            denied_id.deny(message)

    @bot.message_handler(content_types=['text'])
    def handle_text(message):
        print('We`ve got message ' + str(datetime.datetime.now()))
        if CheckPermission(message) == "User":
            # Якшо касир пише
            buttons.keybord(bot, message)
            denied_id.log(message)
        elif CheckPermission(message) == "Admin":
            # Якшо адмін пише
            administrator.administrator(message, bot)
            denied_id.log(message)
        else:
            # Якщо id не сходиться, то не допускається до роботи з ботом
            print(message.chat.id, 'Access denied')
            denied_id.deny(message)

    bot.polling(none_stop=False, interval=0, timeout=20)
