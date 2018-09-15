from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}
import ephem
import datetime
import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    print('Вызван /start')


def find_stars(bot, update):
    now=datetime.datetime.now()
    user_text = update.message.text.split(' ')
    formated_user_text = user_text[1].capitalize()
    try:
        a=getattr(ephem, formated_user_text)(now)
        c=ephem.constellation(a)
        update.message.reply_text("Планета находится в cозвездии " + str(c[1]))
    except AttributeError:
        print ('Невозможно определить положение планеты')
        update.message.reply_text('Невозможно определить положение планеты')
         
def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def main():
    mybot = Updater("692263356:AAHUCN2SFBUpOTtbClgkgztTh-D9xfPju7M", request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", find_stars))

    mybot.start_polling()
    mybot.idle()

main()