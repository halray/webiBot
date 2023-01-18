"""Readme :  pip install python-telegram-bot --upgrade"""
from telegram.ext import CommandHandler, Application, CallbackQueryHandler,ContextTypes
from telegram import InlineKeyboardButton,InlineKeyboardMarkup,Update
import sys
sys.path.append('../src/')
from config import BOT_TOKEN, API_KEY,IDS_ALLOWED

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data="1"),
            InlineKeyboardButton("Option 2", callback_data="2"),
        ],
        [InlineKeyboardButton("Option 3", callback_data="3")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Please choose:", reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()

    await query.edit_message_text(text=f"Selected option: {query.data}")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    await update.message.reply_text("Use /start to test this bot.")


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler("help", help_command))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()

#def main():
#   print("====== starting bot program ======")

 #   updater = Updater(BOT_TOKEN, base_url)
  #  a = updater.bot.logOut
    #b = updater.bot.close()
   # print (a)
    #dispatcher = updater.dispatcher

    # example dog_picture_handler to be demonstrated by teacher
    #dispatcher.add_handler(CommandHandler("dog", dog_picture_handler))

    # movie_handler to be filled in by student
    #dispatcher.add_handler(CommandHandler("movie", movie_handler))

    #updater.start_polling()
    #updater.idle()


if __name__ == "__main__":
    main()
