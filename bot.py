import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
bot_token='7325561730:AAGQ0FzwmqTPX5Ww3o3tjWLzl2x7MC3QdSA'
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "Auto Message Forwarder Bot for Telegram is a versatile and efficient tool designed to automate the forwarding of messages across different chats, groups, or channels within the Telegram platform. This bot enables users to set up specific rules for forwarding, such as keywords, sender IDs, or message types (text, images, videos, etc.), ensuring that relevant information is instantly shared with the right audience. It supports custom scheduling, filters, and even the ability to modify or format messages before they are forwarded. Ideal for managing large communities, coordinating teams, or keeping multiple groups informed, the Auto Message Forwarder Bot saves time and streamlines communication across the board"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

async def setup_source_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="set up source chat")

async def setup_target_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="set up target chat")

# async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

if __name__ == '__main__':
    application = ApplicationBuilder().token(bot_token).build()
    
    start_handler = CommandHandler('start', start)
    setup_source_chat_handler = CommandHandler('setup_source_chat', setup_source_chat)
    setup_target_chat_handler = CommandHandler('setup_target_chat', setup_target_chat)

    application.add_handler(start_handler)
    application.add_handler(setup_source_chat_handler)
    application.add_handler(setup_target_chat_handler)
    # unknown_handler = MessageHandler(filters.COMMAND, unknown)
    # application.add_handler(unknown_handler)    
    application.run_polling()
