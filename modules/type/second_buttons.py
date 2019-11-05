from modules.server import localhost
from modules.Data import data
from modules.type import markups
from modules.Data import data_longer


def final(message, bot):
    # Записує в чек
    # Нахуй переписати сука
    markups.type.type_main(bot, message)
    if message.text == 'Стрижка дитяча':
        price = data.haircut_child
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Стрижка модельна':
        price = data.haircut_model
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Вкладка (гель, пінка)':
        price = data.vkladka_man
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Експрес':
        price = data.Express
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Денний':
        price = data.Day_makeup
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Вечірній':
        price = data.Evening_makeup
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Весільний':
        price = data.Weeding_makeup
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Накладні вії':
        price = data.fake_eyelashes
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Berrywell':
        price = data.Berrywell
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'SPA - педикюр':
        price = data.SPA_pedicure
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'SPA - докляд за ступнями':
        price = data.SPA_legs
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Покриття нігтів лаком':
        price = data.leg_nail_varnish
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Масаж ніг "Релаксуючий"':
        price = data.Relax_massage
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Крем для ніг':
        price = data.leg_cream
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'SPA - педикюр "Пальчики"':
        price = data.SPA_fingers
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Корекція':
        price = data.correction
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Гель лак':
        price = data.Gel_varnish
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Якийсь суперкрутий':
        price = data.Very_cool_varnish
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Модельна без миття голови':
        price = data.hairut_female_model
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Модельна + вкладка(миття, фіксуючу засоби)':
        price = data.hairut_female_model_vkladka
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Вкладка (миття, фіксуючі засоби)':
        price = data.female_vkladka
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Вкладка "Святкова"':
        price = data.holiday_vkaldka
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Модельна (накрутка)':
        price = data.vkladka_model
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Без фіксуючих засобів':
        price = data.vkladka_without_fix
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Модельна':
        price = data.hairdo_model
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Весільна':
        price = data.hairdo_weeding
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Фарбування фарбою "Vitalitis"':
        price = data.paint_vitalitis
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Фарбою клієнта':
        price = data.paint_own_paint
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Колорування':
        price = data.coloruvania
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Висвітлення вибіркове на фольгу (порошок)':
        price = data.visvitlenia
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Висвітлення вибіркове Blondoran на шапочку':
        price = data.visvitlenia_blondoran
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == "Завивка об'ємна":
        price = data.zavivka_obiem
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Завивка проста':
        price = data.zavivka_priosta
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Біозавивка кератинова':
        price = data.keratin_zavivka
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Біозавивка Vitalitis':
        price = data.vitalitis_biozavivka
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Миття голови':
        price = data.head_wash
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    else:
        final1(bot, message)


def final1(bot, message):
    if message.text == 'Модельна без миття голови.':
        price = data_longer.hairut_female_model
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Модельна + вкладка(миття, фіксуючу засоби),':
        price = data_longer.hairut_female_model_vkladka
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Вкладка (миття, фіксуючі засоби).':
        price = data_longer.female_vkladka
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Вкладка "Святкова".':
        price = data_longer.holiday_vkaldka
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Модельна (накрутка).':
        price = data_longer.vkladka_model
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Без фіксуючих засобів.':
        price = data_longer.vkladka_without_fix
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Модельна.':
        price = data_longer.hairdo_model
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Весільна ':
        price = data_longer.hairdo_weeding
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Фарбування фарбою "Vitalitis".':
        price = data_longer.paint_vitalitis
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Фарбою клієнта.':
        price = data_longer.paint_own_paint
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Колорування.':
        price = data_longer.coloruvania
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Висвітлення вибіркове на фольгу (порошок).':
        price = data_longer.visvitlenia
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Висвітлення вибіркове Blondoran на шапочку.':
        price = data_longer.visvitlenia_blondoran
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == "Завивка об'ємна.":
        price = data_longer.zavivka_obiem
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Завивка проста.':
        price = data_longer.zavivka_prosta
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Біозавивка кератинова.':
        price = data_longer.keratin_zavivka
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Біозавивка Vitalitis.':
        price = data_longer.vitalitis_biozavivka
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    elif message.text == 'Миття голови.':
        price = data_longer.head_wash
        localhost.file.data(message.text, price, message.chat.id)
        bot.send_message(message.chat.id, str(message.text) + '\n' + 'Ціна : ' + str(price))

    else:
        bot.send_message(message.chat.id, 'Помилка')
