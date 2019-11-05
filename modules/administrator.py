from modules.server import localhost
import os.path
import datetime


def administrator(message, bot):
    bot.send_message(message.chat.id, "Щоб отримати звіт за конкретний день, потрібно написати дату у форматі "
                                      "рік-місяць-день(Приклад 2019-09-05)\nЩоб отримати звіт за місяць, потрібно "
                                      "написати "
                                      " рік та номер місяця(приклад 2019-09)")
    # Тут тоже всьо нахуй переписати і взагалі шоб очі мої цього не бачили
    if message.text == 'Звіт про заробіток':
        doc = open('Checks/Data.txt', 'rb')
        bot.send_document(message.chat.id, doc)
        bot.send_message(message.chat.id, 'Готово')

    if message.text == 'Звіт про бота':
        try:
            doc = open('Checks/Denied id.txt', 'rb')
            bot.send_document(message.chat.id, doc)
            bot.send_message(message.chat.id, 'Готово')
        except:
            bot.send_message(message.chat.id, "Помилка")

    #elif message.text == 'Видалити історію':
    #   localhost.file.delete_data(bot, message)
    else:
        try:
            doc = open("Checks/" + str(message.text) + ".txt", "r")
            bot.send_document(message.chat.id, doc)
        except:
            monthCheckout(message, bot)
    return message, bot


def monthCheckout(message, bot):
    global a
    check = False
    i = 0
    while i < 32:
        i += 1
        if i < 10:
            b = "0" + "%s" % i
            print(i)
        else:
            b = i
            print(b)
        a = "Checks/" + str(message.text) + "-%s" % b + ".txt"
        if os.path.exists(a):
            check = True
            doc = open("Checks/%s .txt" % datetime.date.today(), "a+")
            doc1 = open("%s" % a, "r")
            text = doc1.read()
            doc1.close()
            doc.write("\n%s" % text)
            doc.close()
    if check:
        doc = open("Checks/%s .txt" % datetime.date.today(), "r")
        bot.send_document(message.chat.id, doc)
        doc.close()
        doc = open("Checks/%s .txt" % datetime.date.today(), "w+")
        doc.write("")
        doc.close()

    elif message.text == "Звіт про заробіток":
        return 0

    elif message.text == "Звіт про бота":
        return 0

    elif message.text == "Видалити історію":
        return 0

    else:
        bot.send_message(message.chat.id, "Щось пішло не так, спробуйте знову (administrator.py line 59)")
