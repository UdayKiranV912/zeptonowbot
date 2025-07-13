from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import ContextTypes
from zepto_data import products
from cart import add_to_cart, view_cart, clear_cart

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton(cat, callback_data=f"category|{cat}")] for cat in products]
    await update.message.reply_text("Welcome to Zepto Bot!\nChoose a category:", reply_markup=InlineKeyboardMarkup(keyboard))

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    if data.startswith("category|"):
        category = data.split("|")[1]
        items = products[category]
        keyboard = [[InlineKeyboardButton(f"{item['name']} - ₹{item['price']}", callback_data=f"add|{item['name']}|{item['price']}")] for item in items]
        await query.edit_message_text(f"Select an item from {category}:", reply_markup=InlineKeyboardMarkup(keyboard))
    elif data.startswith("add|"):
        _, name, price = data.split("|")
        user_id = update.effective_user.id
        add_to_cart(user_id, {"name": name, "price": int(price)})
        await query.edit_message_text(f"✅ {name} added to cart.\nUse /cart to view or /order to confirm.")

async def show_cart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cart = view_cart(update.effective_user.id)
    if not cart:
        await update.message.reply_text("🛒 Your cart is empty.")
        return
    msg = "🛒 Your Cart:\n"
    total = 0
    for item in cart:
        msg += f"- {item['name']}: ₹{item['price']}\n"
        total += item['price']
    msg += f"\nTotal: ₹{total}"
    await update.message.reply_text(msg)

async def order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    cart = view_cart(user_id)
    if not cart:
        await update.message.reply_text("Cart is empty.")
        return
    total = sum(item['price'] for item in cart)
    clear_cart(user_id)
    await update.message.reply_text(f"✅ Order placed for ₹{total}!\nThank you for shopping on Zepto Bot.")
