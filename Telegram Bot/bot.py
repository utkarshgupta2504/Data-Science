import logging
import os
import dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, CallbackContext

dotenv.load_dotenv()

# enable logging
# logging.basicConfig(
#     format="%{asctime}s - %{name}s - %{levelname}s - %{message}s", level=logging.INFO)
# logger = logging.getLogger(__name__)

# Every handler has 2 args bot and update, update has all the events


def start(update: Update, context: CallbackContext):
    update.message.reply_text(f"Hi {update.effective_user.first_name}")


def _help(update: Update, context: CallbackContext):
    update.message.reply_text(f"Hey! This is a help text")


def echo_text(update: Update, context: CallbackContext):
    update.message.reply_text(f"{update.effective_message.text}")


def echo_sticker(update: Update, context: CallbackContext):
    update.message.reply_sticker(update.effective_message.sticker.file_id)


def main():
    updater = Updater(os.environ["TOKEN"])

    # Dispatcher handles all the commands and the messages in telegram
    dp = updater.dispatcher

    # Command handler responsds to the commands (Starting with "/")
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", _help))

    # Message Handler handles the messages from the chat
    # Filters can be used to filter (text / sticker / etc)
    dp.add_handler(MessageHandler(Filters.text, echo_text))
    dp.add_handler(MessageHandler(Filters.sticker, echo_sticker))

    # Start polling (listening to messages and commands)
    updater.start_polling()
    print("Started Polling...")
    updater.idle()


if __name__ == "__main__":
    main()
