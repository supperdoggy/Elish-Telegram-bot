from telebot import types


class type:
    def type_main(self, message):
        main = types.ReplyKeyboardMarkup(row_width=3)
        btn1 = types.KeyboardButton('Чоловічі послуги')
        btn2 = types.KeyboardButton('Макіяж')
        btn3 = types.KeyboardButton('Педикюр')
        btn4 = types.KeyboardButton('Жіночі послуги')
        btn5 = types.KeyboardButton('Манікюр')
        btn6 = types.KeyboardButton('Миття голови')
        btn7 = types.KeyboardButton('Прибуток')
        btn8 = types.KeyboardButton("Чек")
        main.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        self.send_message(message.chat.id, 'Виберіть категорію', reply_markup=main)

    def type_admin(self, message):
        admin_markup = types.ReplyKeyboardMarkup(row_width=2)
        ibtn = types.KeyboardButton('Звіт про заробіток')
        ibtn1 = types.KeyboardButton('Звіт про бота')
        ibtn2 = types.KeyboardButton('Видалити історію')
        admin_markup.add(ibtn, ibtn1, ibtn2)
        self.send_message(message.chat.id, 'Виберіть послугу', reply_markup=admin_markup)

    def typer_lenght(self, message):
        main = types.ReplyKeyboardMarkup(row_width=2)
        btn1 = types.KeyboardButton('До плеча')
        btn2 = types.KeyboardButton('Нижче плеча')
        btn3 = types.KeyboardButton('Назад')
        main.add(btn1, btn2, btn3)
        self.send_message(message.chat.id, 'Виберіть довжину волосся', reply_markup=main)


class second_type:
    def type_main_men(self, message):
        main = types.ReplyKeyboardMarkup(row_width=2)
        btn1 = types.KeyboardButton('Стрижка дитяча')
        btn2 = types.KeyboardButton('Стрижка модельна')
        btn3 = types.KeyboardButton('Вкладка (гель, пінка)')
        btn_back = types.KeyboardButton('Назад')
        main.add(btn1, btn2, btn3, btn_back)
        self.send_message(message.chat.id, 'Виберіть послугу', reply_markup=main)

    def type_main_makeup(self, message):
        main = types.ReplyKeyboardMarkup(row_width=3)
        btn1 = types.KeyboardButton('Експрес')
        btn2 = types.KeyboardButton('Денний')
        btn3 = types.KeyboardButton('Вечірній')
        btn4 = types.KeyboardButton('Весільний')
        btn5 = types.KeyboardButton('Накладні вії')
        btn6 = types.KeyboardButton('Berrywell')
        btn_back = types.KeyboardButton('Назад')
        main.add(btn1, btn2, btn3, btn4, btn5, btn6, btn_back)
        self.send_message(message.chat.id, 'Виберіть послугу', reply_markup=main)

    def type_main_pedicure(self, message):
        main = types.ReplyKeyboardMarkup(row_width=3)
        btn1 = types.KeyboardButton('SPA - педикюр')
        btn2 = types.KeyboardButton('SPA - докляд за ступнями')
        btn3 = types.KeyboardButton('Покриття нігтів лаком')
        btn4 = types.KeyboardButton('Масаж ніг "Релаксуючий"')
        btn5 = types.KeyboardButton('Крем для ніг')
        btn6 = types.KeyboardButton('SPA - педикюр "Пальчики"')
        btn_back = types.KeyboardButton('Назад')
        main.add(btn1, btn2, btn3, btn4, btn5, btn6, btn_back)
        self.send_message(message.chat.id, 'Виберіть послугу', reply_markup=main)

    def type_main_female(self, message):
        main = types.ReplyKeyboardMarkup(row_width=3)
        btn1 = types.KeyboardButton('Стрижка')
        btn2 = types.KeyboardButton('Вкладка')
        btn3 = types.KeyboardButton('Зачіска')
        btn4 = types.KeyboardButton('Фарбування')
        btn5 = types.KeyboardButton('Завивка')
        btn6 = types.KeyboardButton('Корекція')
        btn_back = types.KeyboardButton('Назад')
        main.add(btn1, btn2, btn3, btn4, btn5, btn6, btn_back)
        self.send_message(message.chat.id, 'Виберіть послугу', reply_markup=main)

    def type_main_manicure(self, message):
        main = types.ReplyKeyboardMarkup(row_width=2)
        btn1 = types.KeyboardButton('Гель лак')
        btn2 = types.KeyboardButton('Якийсь суперкрутий')
        btn_back = types.KeyboardButton('Назад')
        # Допиши

        main.add(btn1, btn2, btn_back)
        self.send_message(message.chat.id, 'Виберіть послугу', reply_markup=main)


class third_type:
    def type_main_female_haircut(self, message):
        main = types.ReplyKeyboardMarkup(row_width=2)
        btn1 = types.KeyboardButton('Модельна без миття голови')
        btn2 = types.KeyboardButton('Модельна + вкладка(миття, фіксуючу засоби)')
        btn_back = types.KeyboardButton('Назад')
        main.add(btn1, btn2, btn_back)
        self.send_message(message.chat.id, 'Виберіть послугу ', reply_markup=main)

    def type_main_female_vkladka(self, message):
        main = types.ReplyKeyboardMarkup(row_width=2)
        btn1 = types.KeyboardButton('Вкладка (миття, фіксуючі засоби)')
        btn2 = types.KeyboardButton('Вкладка "Святкова"')
        btn3 = types.KeyboardButton('Модельна (накрутка)')
        btn4 = types.KeyboardButton('Без фіксуючих засобів')
        btn_back = types.KeyboardButton('Назад')
        main.add(btn1, btn2, btn3, btn4, btn_back)
        self.send_message(message.chat.id, 'Виберіть послугу', reply_markup=main)

    def type_main_female_hairdo(self, message):
        main = types.ReplyKeyboardMarkup(row_width=2)
        btn1 = types.KeyboardButton('Модельна')
        btn2 = types.KeyboardButton('Весільна')
        btn_back = types.KeyboardButton('Назад')

        main.add(btn1, btn2, btn_back)
        self.send_message(message.chat.id, 'Виберіть послугу', reply_markup=main)

    def type_main_female_painting(self, message):
        main = types.ReplyKeyboardMarkup(row_width=2)
        btn1 = types.KeyboardButton('Фарбування фарбою "Vitalitis"')
        btn2 = types.KeyboardButton('Фарбою клієнта')
        btn3 = types.KeyboardButton('Колорування')
        btn4 = types.KeyboardButton('Висвітлення вибіркове на фольгу (порошок)')
        btn5 = types.KeyboardButton('Висвітлення вибіркове Blondoran на шапочку')
        btn_back = types.KeyboardButton('Назад')
        main.add(btn1, btn2, btn3, btn4, btn5, btn_back)
        self.send_message(message.chat.id, 'Виберіть послугу', reply_markup=main)

    def type_main_female_zavivka(self, message):
        main = types.ReplyKeyboardMarkup(row_width=2)
        btn1 = types.KeyboardButton("Завивка об'ємна")
        btn2 = types.KeyboardButton('Завивка проста')
        btn3 = types.KeyboardButton('Біозавивка кератинова')
        btn4 = types.KeyboardButton('Біозавивка Vitalitis')
        btn_back = types.KeyboardButton('Назад')
        main.add(btn1, btn2, btn3, btn4, btn_back)
        self.send_message(message.chat.id, 'Виберіть послугу', reply_markup=main)


class second:
    def type_main_female(self, message):
        main = types.ReplyKeyboardMarkup(row_width=3)
        btn1 = types.KeyboardButton('Стрижка.')
        btn2 = types.KeyboardButton('Вкладка.')
        btn3 = types.KeyboardButton('Зачіска.')
        btn4 = types.KeyboardButton('Фарбування.')
        btn5 = types.KeyboardButton('Завивка.')
        btn6 = types.KeyboardButton('Корекція')
        btn_back = types.KeyboardButton('Назад')
        main.add(btn1, btn2, btn3, btn4, btn5, btn6, btn_back)
        self.send_message(message.chat.id, 'Виберіть послугу', reply_markup=main)


class third_long:
    def type_main_female_haircut(self, message):
        main = types.ReplyKeyboardMarkup(row_width=2)
        btn1 = types.KeyboardButton('Модельна без миття голови.')
        btn2 = types.KeyboardButton('Модельна + вкладка(миття, фіксуючу засоби).')
        btn_back = types.KeyboardButton('Назад')
        main.add(btn1, btn2, btn_back)
        self.send_message(message.chat.id, 'Виберіть послугу ', reply_markup=main)

    def type_main_female_vkladka(self, message):
        main = types.ReplyKeyboardMarkup(row_width=2)
        btn1 = types.KeyboardButton('Вкладка (миття, фіксуючі засоби).')
        btn2 = types.KeyboardButton('Вкладка "Святкова".')
        btn3 = types.KeyboardButton('Модельна (накрутка).')
        btn4 = types.KeyboardButton('Без фіксуючих засобів.')
        btn_back = types.KeyboardButton('Назад')
        main.add(btn1, btn2, btn3, btn4, btn_back)
        self.send_message(message.chat.id, 'Виберіть послугу', reply_markup=main)

    def type_main_female_hairdo(self, message):
        main = types.ReplyKeyboardMarkup(row_width=2)
        btn1 = types.KeyboardButton('Модельна.')
        btn2 = types.KeyboardButton('Весільна.')
        btn_back = types.KeyboardButton('Назад')

        main.add(btn1, btn2, btn_back)
        self.send_message(message.chat.id, 'Виберіть послугу', reply_markup=main)

    def type_main_female_painting(self, message):
        main = types.ReplyKeyboardMarkup(row_width=2)
        btn1 = types.KeyboardButton('Фарбування фарбою "Vitalitis".')
        btn2 = types.KeyboardButton('Фарбою клієнта.')
        btn3 = types.KeyboardButton('Колорування.')
        btn4 = types.KeyboardButton('Висвітлення вибіркове на фольгу (порошок).')
        btn5 = types.KeyboardButton('Висвітлення вибіркове Blondoran на шапочку.')
        btn_back = types.KeyboardButton('Назад')
        main.add(btn1, btn2, btn3, btn4, btn5, btn_back)
        self.send_message(message.chat.id, 'Виберіть послугу', reply_markup=main)

    def type_main_female_zavivka(self, message):
        main = types.ReplyKeyboardMarkup(row_width=2)
        btn1 = types.KeyboardButton("Завивка об'ємна.")
        btn2 = types.KeyboardButton('Завивка проста.')
        btn3 = types.KeyboardButton('Біозавивка кератинова.')
        btn4 = types.KeyboardButton('Біозавивка Vitalitis.')
        btn_back = types.KeyboardButton('Назад')
        main.add(btn1, btn2, btn3, btn4, btn_back)
        self.send_message(message.chat.id, 'Виберіть послугу', reply_markup=main)
