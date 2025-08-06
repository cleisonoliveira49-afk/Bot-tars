import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Token do bot (puxado da variável de ambiente)
TOKEN = os.getenv("BOT_TOKEN")

# Configurando logs (opcional mas útil pra debugging)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Salve, piloto! 🛵 Bot pronto pra te ajudar!")

# Comando /onde_hoje
async def onde_hoje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Aqui no futuro: análise de clima, eventos, etc.
    await update.message.reply_text("🔥 Hoje tá bombando em Ubatuba! Partiu faturar!")

# Iniciando o bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("onde_hoje", onde_hoje))
    print("Bot iniciado.")
    app.run_polling()
  
