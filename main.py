import telebot
import datetime
import time
import threading
import random

bot = telebot.TeleBot("7607485261:AAGOzyPgb9ciN9_DoTodP2OrqUSzkgN29r4")

@bot.message_handler(commands = ['start'])
def star_message(message):
    bot.reply_to(message, "Привет! Я бот, который будет напоминать тебе пить водичку!")
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminder_thread.start()

@bot.message_handler(commands = ["fact"])
def fact_message(message):
    list = ["**Уникальное поведение при замерзании: Вода — единственное вещество, которое при замерзании расширяется. Это значит, что лед легче, чем жидкая вода, из-за чего он плавает. Этот необычный эффект играет важную роль в экосистемах, так как позволяет жизни сохраняться под ледяными покрытиями водоемов.",
            "** Хотя это и вызывает споры, некоторые исследования в области гидрологии и гомеопатии утверждают, что у воды есть 'память' – способность запоминать вещества, с которыми она была в контакте, даже после их удаления. Это предположение основывается на наблюдениях изменений структуры воды, но требует дальнейших научных исследований для подтверждения.",
            "** Вода считается универсальным растворителем."]
    random_fact = random.choice(list)
    bot.reply_to(message, f"Вот факт о воде {random_fact}")

def send_reminders(chat_id):
    first_rem = "09:00"
    second_rem = "14:30"
    end_rem = "18:00"

    while True:
        now = datetime.datetime.now().strftime('%H:%M')
        if now == first_rem or now == second_rem or now == end_rem:
            bot.send_message(chat_id, "Напоминание - выпей стакан воды")
            time.sleep(61)
        time.sleep(1)

bot.polling(none_stop=True)