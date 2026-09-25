from config import *

import telebot

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am testBot 101.
I am here to do nothing.\
""")
    
@bot.message_handler(commands=['help'])
def send_nohelp(message):
    bot.reply_to(message, """\
There will be no help, lol.\
""")

@bot.message_handler(commands=['detour'])
def detour_random(message):
    detoursong = (["detour", "dtla", "i like ur look", "check it", "polo", "brutalist", "need for speed", "jeep", "101", "basketball", "freak it", "pop sound"])
    bot.reply_to(message, random.choise(detoursong))

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()