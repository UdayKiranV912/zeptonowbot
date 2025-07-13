import os
import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

# Dummy Handlers
async def start(update, context):
    await update.message.reply_text("Welcome to ZeptoBot! 🍅🥦")

async def order(update, context):
    await update.message.reply_text("Ordering... 🚀")

async def cart(update, context):
    await update.message.reply_text("Your cart is empty 🛒")

async def button_handler(update, context):
    await update.callback_query.answer("Clicked!")

# Read token from env var
TOKEN = os.environ.get("BOT_TOKEN")

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("order", order))
    app.add_handler(CommandHandler("cart", cart))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
