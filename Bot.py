# Импортируем необходимые классы.
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
from time import asctime
import os

PORT = int(os.environ.get('PORT', 5000))
TOKEN = "1729251878:AAGa7vHVF1XL1Kr9TlsTar5x6xSNPIs-u5M"


# Определяем функцию-обработчик сообщений.
# У неё два параметра, сам бот и класс updater, принявший сообщение.
def echo(update, context):
    # У объекта класса Updater есть поле message,
    # являющееся объектом сообщения.
    # У message есть поле text, содержащее текст полученного сообщения,
    # а также метод reply_text(str),
    # отсылающий ответ пользователю, от которого получено сообщение.
    update.message.reply_text(f'Я получил сообщение {update.message.text}')

def date(update, context):
    cur_time = str(asctime()).split()
    del cur_time[3], cur_time[0]
    update.message.reply_text(' '.join(cur_time))


def time(update, context):
    cur_time = str(asctime()).split()[3]
    update.message.reply_text(str(cur_time))


def main():
    # Создаём объект updater.
    # Вместо слова "TOKEN" надо разместить полученный от @BotFather токен
    updater = Updater(TOKEN, use_context=True)

    # Получаем из него диспетчер сообщений.
    dp = updater.dispatcher

    # Создаём обработчик сообщений типа Filters.text
    # из описанной выше функции echo()
    # После регистрации обработчика в диспетчере
    # эта функция будет вызываться при получении сообщения
    # с типом "текст", т. е. текстовых сообщений.
    text_handler = MessageHandler(Filters.text, echo)

    # Регистрируем обработчик в диспетчере.
    dp.add_handler(CommandHandler('date', date))
    dp.add_handler(CommandHandler('time', time))
    dp.add_handler(text_handler)
    # Запускаем цикл приема и обработки сообщений.
    updater.bot.setWebhook('https://yan-bot-sergt.herokuapp.com/' + TOKEN)
    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN)
    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
