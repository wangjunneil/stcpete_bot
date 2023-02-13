#!/usr/bin/env python3
#-*- coding: UTF-8 -*-

import json,datetime
import os
import telebot
import requests

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# @bot.message_handler(commands=['syncvodpic'])
# def syncfilepic(message):
#     send_message = bot.reply_to(message, 'Enter date directory name (20220315) : ')
#     bot.register_next_step_handler(send_message, sync_dir_name)

# @bot.message_handler(commands=['updhotvod'])
# def updhotvod(message):
#     response = requests.post(url='http://api.jaskan.com/filmAMks211Po/hot', headers={'Content-Type':'application/json'})
#     result_json = json.loads(response.text)
#     if result_json['status'] == 'success':
#         bot.send_message(message.chat.id, "\r\n".join(result_json['message']))

# @bot.message_handler(func=lambda m: True)
# def catch_all_message(message):
#     default_message = '''
#     You can control me by sending these commands:

# /syncvodpic - sync vod pic with date directory
# /updhotvod - update hot search vod and generate index
#     '''
#     bot.send_message(message.chat.id, default_message)


# def sync_dir_name(message):
#     date_str = message.text
#     if not validate_text(date_str):
#         bot.reply_to(message, '⛔️ invalid input')
#         return

#     data = {"dir": date_str + "-1"}
#     response = requests.post(url='http://api.jaskan.com/filmAMks211Po/sync', 
#         headers={'Content-Type':'application/json'},
#         data=json.dumps(data))
#     result_json = json.loads(response.text)
#     if result_json['status'] == 'success':
#         bot.send_message(message.chat.id, 'Done')

# def validate_text(text):
#     try:
#         datetime.datetime.strptime(text, '%Y%m%d')
#         return True
#     except ValueError:
#         return False

bot.infinity_polling()