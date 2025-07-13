import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from handlers import start, handle_callback, show_cart, order

TOKEN = "7609313079:AAGz1EI0JeCvXXoMChDIKn39jxTvFBbTWhA"

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_callback))
    app.add_handler(CommandHandler("cart", show_cart))
    app.add_handler(CommandHandler("order", order))
    print("Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
