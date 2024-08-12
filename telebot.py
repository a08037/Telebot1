import telebot
import datetime
import time
import threading
import random

bot = telebot.TeleBot('7389783627:AAG6j4R42_Kh9AJZUnPMOSECVnzFwqmUCGw')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message,
                 'Привет! Я чат-бот, который будет напоминать тебе пить водичку, измерять давление и заниматься учебой!')
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminder_thread.start()


@bot.message_handler(commands=['help'])
def help_message(message):
    help_text = (
        "Доступные команды:\n"
        "/start - Начать работу с ботом и получать напоминания\n"
        "/fact - Получить интересный факт о воде\n"
        "/help - Показать это меню"
    )
    bot.reply_to(message, help_text)


@bot.message_handler(commands=['fact'])
def fact_message(message):
    facts = [
        "Вода на Земле может быть старше самой Солнечной системы: Исследования показывают, что от 30% до 50% воды в наших океанах возможно присутствовала в межзвездном пространстве еще до формирования Солнечной системы около 4,6 миллиарда лет назад.",
        "Горячая вода замерзает быстрее холодной: Это явление известно как эффект Мпемба. Под определенными условиями горячая вода может замерзать быстрее, чем холодная, хотя ученые до сих пор полностью не разгадали механизм этого процесса.",
        "Больше воды в атмосфере, чем во всех реках мира: Объем водяного пара в атмосфере Земли в любой момент времени превышает объем воды во всех реках мира вместе взятых. Это подчеркивает важную роль атмосферы в гидрологическом цикле, перераспределяя воду по планете."
    ]
    random_fact = random.choice(facts)
    bot.reply_to(message, f'Лови факт о воде: {random_fact}')


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


def send_reminders(chat_id):
    first_water_rem = "09:00"
    second_water_rem = "14:00"
    end_water_rem = "18:00"
    first_pressure_rem = "10:00"
    second_pressure_rem = "21:00"
    study_reminder_time = "12:00"
    while True:
        now = datetime.datetime.now()
        current_time = now.strftime('%H:%M')
        current_weekday = now.weekday()

        if current_time == first_water_rem or current_time == second_water_rem or current_time == end_water_rem:
            bot.send_message(chat_id, "Напоминание - выпей стакан воды")
            time.sleep(61)
        elif current_time == first_pressure_rem or current_time == second_pressure_rem:
            bot.send_message(chat_id, "Напоминание - измерь давление")
            time.sleep(61)
        elif current_time == study_reminder_time:
            if current_weekday in [0, 2, 4]:  # Monday, Wednesday, Friday
                bot.send_message(chat_id, "Напоминание - открой новый модуль для обучения")
            elif current_weekday in [1, 3, 5]:  # Tuesday, Thursday, Saturday
                bot.send_message(chat_id, "Напоминание - делай домашнее задание по новым модулям")
            time.sleep(61)
        time.sleep(1)


bot.polling(none_stop=True)

