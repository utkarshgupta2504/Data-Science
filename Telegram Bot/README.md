# Telegram Bot

This bot has been created using the `python-telegram-bot` package from pip

To run this bot for yourself, you need to setup a `.env` file, for the `os.environ[]` to get populated

- A `client.json` file from **Google Dialogflow service accounts** for the application to use dialogflow
- A bot token with key "TOKEN" from [@BotFather](https://t.me/BotFather) for your new bot
- A project id with key "PROJECT_ID" from the dialogflow project settings

**Extra softwares**

- To serve your localhost on a dummy https site over the internet, you can use `ngrok`, download and run `ngrok http 8443` and your server will start, replace the `bot.set_webhook("<Your https url>")` to start the webhook for your bot
