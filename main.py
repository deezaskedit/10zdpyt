from telegram import Update
from telegram.ext import Application, CommandHandler
from bot_com import *


token = import_from_file('token.txt')

application = Application.builder().token(token).build()

application.add_handler(CommandHandler("hi", hi_command))
application.add_handler(CommandHandler("help", help_command))
application.add_handler(CommandHandler("sum", sum_command))
application.add_handler(CommandHandler("subt", subt_command))
application.add_handler(CommandHandler("mlp", multiplic_command))
application.add_handler(CommandHandler("div", div_command))
print("Server start")

application.run_polling()