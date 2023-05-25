import os
import requests
import telegram
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater

PIXABAY_API_KEY = "YOUR_PIXABAY_API_KEY"
PIXABAY_API_URL = "https://pixabay.com/api/"

# Функция для выполнения запросов к Pixabay API и получения списка картинок по тегу, указанному пользователем
def search_images(query):
    url = f"{PIXABAY_API_URL}?key={PIXABAY_API_KEY}&q={query}&image_type=photo&per_page=5"
    response = requests.get(url)
    json_data = response.json()
    hits = json_data["hits"]
    return hits

# Функция-обработчик команды /start
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Привет! Я бот для поиска картинок. Напиши тег, по которому нужно искать картинки.")

# Функция-обработчик текстовых сообщений от пользователя
def search_images_handler(bot, update):
    query = update.message.text
    if query:
        hits = search_images(query)
        if hits:
            # Отправляем найденные картинки пользователю
            for hit in hits:
                bot.send_photo(chat_id=update.message.chat_id, photo=hit["previewURL"])
        else:
            bot.send_message(chat_id=update.message.chat_id, text="К сожалению, по вашему запросу ничего не найдено.")

# Функция для запуска бота
def run_bot(token):
    updater = Updater(token=token)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    search_images_handler = MessageHandler(Filters.text, search_images_handler)
    dispatcher.add_handler(search_images_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    token = "YOUR_BOT_TOKEN"
    run_bot(token)