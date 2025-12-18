import telebot
import movie_parser
from парсер.movie_parser import get_movie_url, get_movie_info

# вставь свой токен из BotFather
TOKEN = ''
bot = telebot.TeleBot(TOKEN)


# Обработчик команды '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Добро пожаловать в справочный бот по фильмам!\nВведи название и бот вернет тебе описание")


@bot.message_handler(func=lambda message: True)
def response(message):
    chat_id = message.chat.id
    try:
        if message.content_type == 'text':
            url = get_movie_url(message.text)
            if url != "Cсылка не найдена" '''and url != None''':
                bot.send_message(chat_id, get_movie_info(url))
            elif url == "Cсылка не найдена" '''or url == None''':
                bot.send_message(chat_id, "Ссылка не найдена. Проверьте правильность введенного названия")
            else:
                bot.send_message(chat_id,"Непредвиденная ошибка")
        else:
            bot.send_message(chat_id, "Пожалуйста, отправьте текстовое сообщение.")
    except Exception as e:
        bot.send_message(chat_id, f"Неизвестная ошибка: {e}")

bot.polling()