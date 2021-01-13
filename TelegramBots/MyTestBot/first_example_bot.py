import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

def revert(update, context):
    if not context.args:
        text = update.message.text
    else:
        text = ' '.join(context.args)
    update.message.reply_text(text.upper())

def caps(update, context):
    if not context.args:
        text = update.message.text
    else:
        text = ' '.join(context.args)
    update.message.reply_text(text.upper())

def revert_and_caps(update, context):
    revert(update, context)
    caps(update, context)

def inline(update, context):
    query = update.inline_query.query
    if not query:
        return

    results = [
        InlineQueryResultArticle(
            id = query.upper(),
            title = 'capse',
            input_message_content = InputTextMessageContent(query.upper())
        ),
        InlineQueryResultArticle(
            id = query[::-1],
            title = 'revert',
            input_message_content = InputTextMessageContent(query[::-1])
        )
    ]
    context.bot.answer_inline_query(update.inline_query.id, results)

updater = Updater(token='1508990442:AAE40vSWEBgww1siZ5GJnxQbxfOFX0SezME', use_context=True)

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()


revert_handler = CommandHandler('revert', revert)
dispatcher.add_handler(revert_handler)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

inline_handler = InlineQueryHandler(inline)
dispatcher.add_handler(inline_handler)

message_handler = MessageHandler(Filters.text, revert_and_caps)
dispatcher.add_handler(message_handler)

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

updater.idle()