import telebot
from datetime import datetime
from calendar import monthrange

def calendar_m(month):
    calendar_markup = telebot.types.InlineKeyboardMarkup()
    current_year = datetime.now().year
    a = 1
    days = monthrange(current_year, month)[1]
    print(days)
    while a != days:
        a += 1
        btn1 = telebot.types.InlineKeyboardButton(f'{a}', callback_data=f'd_{a}-{month}-{current_year}')
        a += 1
        btn2 = telebot.types.InlineKeyboardButton(f'{a}', callback_data=f'd_{a}-{month}-{current_year}')
        a += 1
        btn3 = telebot.types.InlineKeyboardButton(f'{a}', callback_data=f'd_{a}-{month}-{current_year}')
        a += 1
        btn4 = telebot.types.InlineKeyboardButton(f'{a}', callback_data=f'd_{a}-{month}-{current_year}')
        a += 1
        btn5 = telebot.types.InlineKeyboardButton(f'{a}', callback_data=f'd_{a}-{month}-{current_year}')
        calendar_markup.row(btn1, btn2, btn3, btn4, btn5)
    end2 = telebot.types.InlineKeyboardButton('Назад', callback_data='end2')
    calendar_markup.row(end2)
    return calendar_markup
start_markup = telebot.types.InlineKeyboardMarkup()
btn1 = telebot.types.InlineKeyboardButton('женский', callback_data='женский')
btn2 = telebot.types.InlineKeyboardButton('мужской', callback_data='мужской')
start_markup.row(btn1,btn2)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
choose_markup_man = telebot.types.InlineKeyboardMarkup()
btn1 = telebot.types.InlineKeyboardButton('окраска волос', callback_data='окраска волос')
btn2 = telebot.types.InlineKeyboardButton('стрижка', callback_data='стрижка')
btn3 = telebot.types.InlineKeyboardButton('кастрация', callback_data='кастрация')
btn4 = telebot.types.InlineKeyboardButton('массаж', callback_data='массаж')
end1 = telebot.types.InlineKeyboardButton('Назад', callback_data='end1')
choose_markup_man.row(btn1,btn2,btn3)
choose_markup_man.row(btn4)
choose_markup_man.row(end1)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
dont_work = telebot.types.InlineKeyboardMarkup()
end2 = telebot.types.InlineKeyboardButton('Назад', callback_data='end2')
dont_work.row(end2)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
choose_markup_woman = telebot.types.InlineKeyboardMarkup()
btn1 = telebot.types.InlineKeyboardButton('окраска волос', callback_data='окраска волос')
btn2 = telebot.types.InlineKeyboardButton('стрижка', callback_data='стрижка')
btn3 = telebot.types.InlineKeyboardButton('солярий', callback_data='солярий')
btn4 = telebot.types.InlineKeyboardButton('маникюр', callback_data='маникюр')
btn5 = telebot.types.InlineKeyboardButton('педикюр', callback_data='педикюр')
end1 = telebot.types.InlineKeyboardButton('Назад', callback_data='end1')
choose_markup_woman.row(btn1,btn2,btn3)
choose_markup_woman.row(btn4,btn5)
choose_markup_woman.row(end1)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
choose_workers_hair = telebot.types.InlineKeyboardMarkup()
btn1 = telebot.types.InlineKeyboardButton('Оля', callback_data='Оля')
btn2 = telebot.types.InlineKeyboardButton('Таня', callback_data='Таня')
btn3 = telebot.types.InlineKeyboardButton('Арселох', callback_data='Арселох')
btn4 = telebot.types.InlineKeyboardButton('Саша', callback_data='Саша')
btn5 = telebot.types.InlineKeyboardButton('Маша', callback_data='Маша')
choose_workers_hair.row(btn1, btn2, btn3, btn4, btn5)
end3 = telebot.types.InlineKeyboardButton('Назад', callback_data='end3')
choose_workers_hair.row(end3)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

choose_free_time = telebot.types.InlineKeyboardMarkup()
for i in range(8, 23):
    if i <= 9:
        btn = telebot.types.InlineKeyboardButton(f'0{i}:00', callback_data=f't_0{i}:00')
    else:
        btn = telebot.types.InlineKeyboardButton(f'{i}:00', callback_data=f't_{i}:00')
    choose_free_time.row(btn)
end4 = telebot.types.InlineKeyboardButton('Назад', callback_data='end4')
choose_free_time.row(end4)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
yesorno = telebot.types.InlineKeyboardMarkup()
btn1 = telebot.types.InlineKeyboardButton('Да', callback_data='Да')
yesorno.row(btn1)
end5 = telebot.types.InlineKeyboardButton('Назад', callback_data='end5')
yesorno.row(end5)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



