import telebot
import datetime
import time
import threading

# Замените на ваш токен
bot = telebot.TeleBot("7844309012:AAH_9_BmDEl53U-iyW-YzuGo3xiG3vTbMLY")

# Глобальный словарь для хранения напоминаний пользователей
user_reminders = {}

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message,
                 "Привет! Я бот для напоминаний о хороших привычках! Используйте /help, чтобы увидеть доступные команды.")

@bot.message_handler(commands=['help'])
def help_message(message):
    help_text = """  
    Доступные команды:  
    /add <время> <сообщение> - Добавить новое напоминание (формат времени: HH:MM)  
    """
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['add'])
def add_reminder(message):
    parts = message.text.split(maxsplit=2)
    if len(parts) < 3:
        bot.reply_to(message, "Используйте: /add <время> <сообщение> (например, /add 09:00 Позаниматься языком)")
        return

    time_str = parts[1]
    reminder_text = parts[2]

    try:
        # Проверяем правильность формата времени
        datetime.datetime.strptime(time_str, '%H:%M')
    except ValueError:
        bot.reply_to(message, "Неверный формат времени! Используйте HH:MM.")
        return

    user_id = message.chat.id
    if user_id not in user_reminders:
        user_reminders[user_id] = {}

    user_reminders[user_id][time_str] = reminder_text
    bot.reply_to(message, f"Напоминание добавлено на {time_str}: {reminder_text}.")

    # Запускаем поток для отправки напоминаний, если он еще не запущен
    if len(user_reminders[user_id]) == 1:  # Если это первое напоминание
        reminder_thread = threading.Thread(target=send_reminders, args=(user_id,))
        reminder_thread.start()

def send_reminders(chat_id):
    while True:
        now = datetime.datetime.now().strftime('%H:%M')
        if chat_id in user_reminders and now in user_reminders[chat_id]:
            reminder_text = user_reminders[chat_id][now]
            bot.send_message(chat_id, reminder_text)
            del user_reminders[chat_id][now]  # Удаляем напоминание после отправки
            time.sleep(60)  # Ждем 60 секунд, чтобы избежать повторных сообщений в течение одной минуты
        time.sleep(1)

bot.polling(none_stop=True)