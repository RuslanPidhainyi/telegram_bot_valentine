import os
from dotenv import load_dotenv

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

load_dotenv()

PHOTO_PATH = os.path.join("assets", "valentine.png")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("💌 get a valentine", callback_data="get_valentine")]
    ]
    markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Hello! Click the button below 👇",
        reply_markup=markup
    )


async def on_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer() 

    if query.data == "get_valentine":
        if not os.path.exists(PHOTO_PATH):
            await query.message.reply_text(
                f"error: {PHOTO_PATH}"
            )
            return

        with open(PHOTO_PATH, "rb") as f:
            await query.message.reply_photo(
                photo=f,
                caption="💖"
            )


def main() -> None:
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise RuntimeError("Нема TELEGRAM_BOT_TOKEN у .env")

    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(on_button))

    app.run_polling()


if __name__ == "__main__":
    main()
