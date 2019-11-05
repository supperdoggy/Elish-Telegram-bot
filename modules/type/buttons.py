from modules.type import markups
from modules.server import localhost
from modules.type import second_buttons


def keybord(bot, message):
    # Тут тоже поправити і скоротити кількість if else (об'єднати категорії)
    if message.text == 'Чоловічі послуги':
        markups.second_type.type_main_men(bot, message)

    elif message.text == 'Макіяж':
        markups.second_type.type_main_makeup(bot, message)

    elif message.text == 'Педикюр':
        markups.second_type.type_main_pedicure(bot, message)

    elif message.text == 'Жіночі послуги':
        markups.type.typer_lenght(bot, message)

    elif message.text == 'Чек':
        localhost.file.Checkout(bot, message)

    elif message.text == 'Манікюр':
        markups.second_type.type_main_manicure(bot, message)

    elif message.text == 'Стрижка':
        markups.third_type.type_main_female_haircut(bot, message)

    elif message.text == 'Вкладка':
        markups.third_type.type_main_female_vkladka(bot, message)

    elif message.text == 'Зачіска':
        markups.third_type.type_main_female_hairdo(bot, message)

    elif message.text == 'Фарбування':
        markups.third_type.type_main_female_painting(bot, message)

    elif message.text == 'Завивка':
        markups.third_type.type_main_female_zavivka(bot, message)

    elif message.text == 'Назад':
        markups.type.type_main(bot, message)

    elif message.text == 'Прибуток':
        localhost.file.Total(bot, message)

    elif message.text == 'Нижче плеча':
        markups.second.type_main_female(bot, message)

    elif message.text == 'До плеча':
        markups.second_type.type_main_female(bot, message)

    elif message.text == 'Стрижка.':
        markups.third_long.type_main_female_haircut(bot, message)

    elif message.text == 'Вкладка.':
        markups.third_long.type_main_female_vkladka(bot, message)

    elif message.text == 'Зачіска.':
        markups.third_long.type_main_female_hairdo(bot, message)

    elif message.text == 'Фарбування.':
        markups.third_long.type_main_female_painting(bot, message)

    elif message.text == 'Завивка.':
        markups.third_long.type_main_female_zavivka(bot, message)

    else:
        second_buttons.final(message,  bot)
