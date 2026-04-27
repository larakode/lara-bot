mport os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# TOKEN from Render environment
TOKEN = os.getenv("8514363629:AAEjHDFCtAxeFgctSsrhsryIgrgQqKWDQeY")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "hi" in text or "hello" in text:
        msg = "Hey... you found me 😏"
    else:
        msg = "You're interesting... tell me more 👀"

    await update.message.reply_text(msg)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, reply))

print("Bot running...")
app.run_polling()
