from telebot import TeleBot
import requests

#u will need to make file token.txt and put your token inside
with open('token.txt', 'r') as file:
    TOKEN = file.read().strip()

bot = TeleBot(TOKEN)

response = requests.get(f"https://api.telegram.org/bot{TOKEN}/getUpdates")
response_json = response.json()


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "/next")

# put your link and picture(inside the same folder as this file) in the next_message function
@bot.message_handler(commands=['next'])
def next_message(message):
    '''
    STICKER variant
    stick = "AgACAgIAAxkBAAEqV3Jl-V84IXL50magIXlyNvTo2ko6zwACNNQxG0mQyEskd9ngPmTkgwEAAwIAA3gAAzQE"
    bot.send_sticker(chat_id=message.chat.id, sticker=stick)
    '''
    bot.send_photo(chat_id=message.chat.id, photo=
    open('yourpic.png', 'rb'), parse_mode='HTML', caption='<a href="yourlink.com</a>', )


bot.polling(non_stop=True, interval=0)