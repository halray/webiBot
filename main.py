"""Readme :  pip install python-telegram-bot --upgrade"""
from telegram.ext import Updater, CommandHandler, MessageHandler
import requests
from config import BOT_TOKEN, API_KEY,IDS_ALLOWED

def main():
    print("====== starting bot program ======")

    updater = Updater(BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # example dog_picture_handler to be demonstrated by teacher
    #dispatcher.add_handler(CommandHandler("dog", dog_picture_handler))

    # movie_handler to be filled in by student
    #dispatcher.add_handler(CommandHandler("movie", movie_handler))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
