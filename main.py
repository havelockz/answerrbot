import os

import telegram
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters

# Встановлюємо токен бота
bot_token = '6280626788:AAFLql4KSb-r9fHTKxcOmSnR0yG5PzFarfI'
bot = telegram.Bot(token=bot_token)

# Встановлюємо chat id адміністратора бота
admin_chat_id = '319586695'


# Функція, що буде викликатися при отриманні повідомлення від користувача
def message_handler(update, context):
    user_chat_id = update.message.chat_id
    user_name = update.message.from_user.first_name
    message_text = update.message.text
    message_time = update.message.date.strftime("%Y-%m-%d %H:%M:%S")

    # Відправляємо повідомлення адміністратору бота
    admin_message = f'Name: {user_name}\nChat ID: {user_chat_id}\nTime: {message_time}\nText: {message_text}'
    bot.send_message(chat_id=admin_chat_id, text=admin_message)


# Функція, що буде викликатися при отриманні команди /s
def reply_handler(update, context):
    args = context.args
    user_chat_id = args[0]
    message_text = ' '.join(args[1:])

    # Відправляємо відповідь користувачеві
    bot.send_message(chat_id=user_chat_id, text=message_text)


# Створюємо об'єкт для отримання оновлень від Telegram
updater = Updater(bot_token, use_context=True)

# Додаємо обробники повідомлень та команд
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler))
#updater.dispatcher.add_handler(CommandHandler('s', reply_handler))
#updater.start_webhook(listen='0.0.0.0', port=int(os.environ.get('PORT', 5000)), url_path='6280626788:AAFLql4KSb-r9fHTKxcOmSnR0yG5PzFarfI')
#updater.bot.set_webhook('https://answerbot111.herokuapp.com//6280626788:AAFLql4KSb-r9fHTKxcOmSnR0yG5PzFarfI')
#updater.idle()
# Запускаємо бота
updater.start_polling()
updater.idle()
