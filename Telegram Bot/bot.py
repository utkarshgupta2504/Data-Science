import json
import logging
import os
import dotenv
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, CallbackContext, Dispatcher

dotenv.load_dotenv()

# enable logging
# logging.basicConfig(
#     format="%{asctime}s - %{name}s - %{levelname}s - %{message}s", level=logging.INFO)
# logger = logging.getLogger(__name__)

# Every handler has 2 args bot and update, update has all the events

app = Flask(__name__)


def start(update: Update, context: CallbackContext):
    reply = "Hewo Tlip, Ugie lobs yuh" if update.effective_user.first_name == "Трипти" else f"Hi {update.effective_user.first_name}"
    update.message.reply_text(reply)


def _help(update: Update, context: CallbackContext):
    update.message.reply_text(f"Hey! This is a help text")


def _aboutme(update: Update, context: CallbackContext):
    update.message.reply_text(json.dumps(
        update.effective_user.to_dict(), indent=2, ensure_ascii=False))


def echo_text(update: Update, context: CallbackContext):
    update.message.reply_text(f"{update.effective_message.text}")
    # print(json.dumps(update.effective_message.to_dict(), indent=2, ensure_ascii=False))


def echo_sticker(update: Update, context: CallbackContext):
    update.message.reply_sticker(update.effective_message.sticker.file_id)


# def main():

    ########### Polling Method ##################

    # updater = Updater(os.environ["TOKEN"])

    # # Dispatcher handles all the commands and the messages in telegram
    # dp = updater.dispatcher

    # Command handler responsds to the commands (Starting with "/")
    # dp.add_handler(CommandHandler("start", start))
    # dp.add_handler(CommandHandler("help", _help))

    # Message Handler handles the messages from the chat
    # Filters can be used to filter (text / sticker / etc)
    # dp.add_handler(MessageHandler(Filters.text, echo_text))
    # dp.add_handler(MessageHandler(Filters.sticker, echo_sticker))

    # Start polling (listening to messages and commands)
    # updater.start_polling()
    # print("Started Polling...")
    # updater.idle()

@app.route("/")
def index():
    return "Server running"


@app.route(f"/{os.environ['TOKEN']}", methods=["GET", "POST"])
def webhook():
    # The webhook that will be called

    # Creating update object
    update = Update.de_json(request.get_json(), bot)
    # print(update)

    # Process the update
    dp.process_update(update)

    return "ok"


if __name__ == "__main__":
    # main()

    ######## Webhook Method ########
    # A webhook method is better as it calls the command only when there is a new message, so that on bigger level bots the requests are less

    bot = Bot(os.environ["TOKEN"])

    dp = Dispatcher(bot, None)

    bot.set_webhook(
        f"https://e228-183-83-208-243.ngrok.io/{os.environ['TOKEN']}")

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", _help))
    dp.add_handler(CommandHandler("aboutme", _aboutme))
    dp.add_handler(MessageHandler(Filters.text, echo_text))
    dp.add_handler(MessageHandler(Filters.sticker, echo_sticker))

    # Bot can run only on 80, 443, 88, 8443
    app.run(port=8443)
