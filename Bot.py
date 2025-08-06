import telebot

BOT_TOKEN = 8254941787:AAFvYg8HK69leAkv5RmR_WockW2H1Ee8mWw
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Bot está funcionando, piloto!")

bot.polling()
