import os
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

value = 0

TOKEN = os.getenv("TOKEN")

async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global value

    text = update.message.text.strip()

    if not text:
        return

    if text[0] not in "+-":
        return

    try:
        num = int(text[1:])
    except:
        return

    old = value

    if text[0] == "+":
        value += num
        op = "+"
    else:
        value -= num
        op = "-"

    await update.message.reply_text(f"{old} {op} {num} = {value}")

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calc))
app.run_polling()
