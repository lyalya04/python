import telebot
from telebot import types

bot = telebot.TeleBot('8009764180:AAFm9jUfO_y-ymPjM4kb2nWGVQd89bpg_0Q')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Перейти на наш сайт💻')
    markup.add(btn1)
    btn2 = types.KeyboardButton('Направления🏃‍♀️')
    btn3 = types.KeyboardButton('Стоимость занятий💸')
    markup.add(btn2, btn3)
    btn4 = types.KeyboardButton('Контакты📞')
    markup.add(btn4)
    btn5 = types.KeyboardButton('Где мы находимся📍')
    markup.add(btn5)
    photo = open('icon2.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)
    bot.send_message(message.chat.id, '<b><em><u>ДОБРО ПОЖАЛОВАТЬ В КЛУБ АЛЬБАТРОС  "ЮГ"🏋️‍♂️</u> , ЧТО ВАС ИНТЕРЕСУЕТ?</em></b>', reply_markup=markup,parse_mode='html')


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == 'Где мы находимся📍'):
        bot.send_message(message.chat.id, text='<u><b><em>Г.КАЛИНИНГРАД, ТОВАРНЫЙ ПЕРЕУЛОК, 5</em></b></u>', parse_mode='html')
    elif (message.text == 'Контакты📞'):
        bot.send_message(message.chat.id, text=f'<b><em>Наш номер телефона</em></b> +7 (4012) 526-731, <b><em>каждый день с 06:00–23:00</em></b>', parse_mode='html')
    elif (message.text == 'Перейти на наш сайт💻'):
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn12 = types.InlineKeyboardButton('Перейти💻', url='https://ug.albagym.ru/')
        markup.add(btn12)
        bot.send_message(message.chat.id,
                         "{0.first_name}! Нажми на кнопку и перейди на сайт)".format(message.from_user), reply_markup=markup)
    elif (message.text == 'Стоимость занятий💸'):
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton('Разовое посещение 1 000 ₽', callback_data='btn1')
        btn2 = types.InlineKeyboardButton('6 месяцев 20 000 ₽', callback_data='btn2')
        btn3 = types.InlineKeyboardButton('12 посещений с 6.00 до 23:00 3 500 ₽', callback_data='btn3')
        btn4 = types.InlineKeyboardButton('12 посещений с 6.00 до 17:00 3 200 ₽', callback_data='btn4')
        btn5 = types.InlineKeyboardButton('8 посещений с 6.00 до 23:00 3 000 ₽', callback_data='btn5')
        btn6 = types.InlineKeyboardButton('8 посещений с 6.00 до 17:00 2 600 ₽', callback_data='btn6')
        btn7 = types.InlineKeyboardButton('4 посещений с 6.00 до 23:00 2 100 ₽', callback_data='btn7')
        btn8 = types.InlineKeyboardButton('4 посещений с 6.00 до 17:00 1 700 ₽', callback_data='btn8')
        markup.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8)
        bot.send_message(message.chat.id,'Абонемент действителен в течении 30 календарных дней с момента активации📆', reply_markup=markup)

    elif (message.text == 'Направления🏃‍♀️'):
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn11 = types.InlineKeyboardButton('Кардио-зона', callback_data='btn11')
        btn22 = types.InlineKeyboardButton('Тренажёрный зал', callback_data='btn22')
        btn33 = types.InlineKeyboardButton('Групповые занятия', callback_data='btn33')
        btn44 = types.InlineKeyboardButton('Бассейн', callback_data='btn44')
        btn55 = types.InlineKeyboardButton('Сауны', callback_data='btn55')
        btn66 = types.InlineKeyboardButton('Аквааэробика', callback_data='btn66')
        btn77 = types.InlineKeyboardButton('Настольный теннис', callback_data='btn77')

        markup.add(btn11,btn22,btn33,btn44,btn55,btn66,btn77)
        bot.send_message(message.chat.id,'Нижеперечисленный список входит в абонемент✅', reply_markup=markup)


bot.polling(none_stop=True)
