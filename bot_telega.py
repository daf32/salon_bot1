from buttons import *
current_year = datetime.now().year
import telebot
from datetime import datetime

bot = telebot.TeleBot('5399179699:AAG3ax58ODNxIqM9ToVcU_fBZdPzMEa-G2U')

procedure_all_m = ['окраска волос','стрижка','кастрация','массаж']
procedure_all_w = ['окраска волос','стрижка','солярий','маникюр','педикюр']
workers_hair = ['Оля','Таня','Арселох','Саша','Маша']
busy_time_workers = []
a = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']


@bot.message_handler(content_types=['text'])
@bot.message_handler(commands=["start"])
def send_text(message):
    if message.text.lower() == '/start' or message.text.lower() == '/старт' or message.text.lower() == 'start' or message.text.lower() == 'старт':
        bot.send_message(message.chat.id,
                         'Привет,\nВыберите пол:', reply_markup=start_markup)
worker = ''
gender = ''
procedure = ''
date1 = ''
time = ''
time_busy = ''
month = datetime.now().month
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global time_busy
    global worker
    global gender
    global procedure
    global date1
    global time
    global current_year
    global month
    global month_name
    global busy_time_workers
    month_name = a[month - 1]
    if call.data.startswith('м') or call.data.startswith('ж'):
        if call.data == 'мужской':
            gender = call.data
            bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.id,text= 'Выберите процедуру:',
                                  reply_markup=choose_markup_man)
            print(gender)
        elif call.data == 'женский':
            gender = call.data
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Выберите процедуру:',
                                  reply_markup=choose_markup_woman)
            print(gender)
    elif call.data.startswith('end'):
        if call.data == 'end1':
            print('Назад')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='Привет,\nВыберите пол:', reply_markup=start_markup)
        elif call.data == 'end2':
            print('Назад')
            if gender == 'мужской':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text='Выберите процедуру:', reply_markup=choose_markup_man)
            elif gender == 'женский':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text='Выберите процедуру:', reply_markup=choose_markup_woman)
        elif call.data == 'end3':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'Месяц: {month_name}',
                                  reply_markup=calendar_m(month))
        elif call.data == 'end4':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'Выберите мастера:',
                                  reply_markup=choose_workers_hair)
        elif call.data == 'end5':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'Свободное время мастера:',
                                  reply_markup=choose_free_time)
    elif call.data.startswith('d'):
        date1 = call.data[2:]
        print(date1)
        if procedure.startswith('стрижка'):
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'Выберите мастера:',
                                  reply_markup=choose_workers_hair)
    elif call.data in workers_hair:
        worker = call.data
        print(worker)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'Свободное время мастера:',
                              reply_markup=choose_free_time)
    elif call.data == 'Да':
        busy_time_workers.append(time_busy)
        print(busy_time_workers)
        time_busy = []
        worker = ''
        gender = ''
        procedure = ''
        date1 = ''
        time = ''
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text='Спасибо за заказ:)')
    elif call.data in procedure_all_m or call.data in procedure_all_w:
        if call.data in procedure_all_m:
            procedure = call.data
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Выберите дату:')
            bot.send_message(call.message.chat.id,f'Месяц: {month_name}',reply_markup=calendar_m(month))
            print(procedure)
        elif call.data in procedure_all_w:
            procedure = call.data
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Выберите дату:')
            bot.send_message(call.message.chat.id, f'Месяц: {month_name}', reply_markup=calendar_m(month))
            print(procedure)
    elif call.data.find('t_') != -1:
        time = call.data[2:]
        time_busy = f'{procedure} {worker} {date1} {time}'
        if time_busy not in busy_time_workers:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=f'Вы выбрали {procedure} на {date1} в {time} у {worker}\nВы уверены?',
                                  reply_markup=yesorno)
        else:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='Извените, но это время уже занято')
            bot.send_message(call.message.chat.id, text=f'Свободное время мастера:',
                             reply_markup=choose_free_time)
            time_busy = []
    else:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text='Извените, но эта функция пока не работает:(',reply_markup=dont_work)
bot.polling()