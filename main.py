import telebot
from config import token
from tradingview import get_rsi
import time
from tvDatafeed import Interval

bot = telebot.TeleBot(token)



# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, "Hi there! The bot ")
    bot.register_next_step_handler(msg, send_rsi)

print('Bot is enabled')

def send_rsi(message, assets=['BTCUSD', 'ETHUSD'], low=40):
    while True:
        for ticker in assets:
            rsi_15m = get_rsi(interval=Interval.in_15_minute, asset=ticker)
            rsi_1h = get_rsi(interval=Interval.in_1_hour, asset=ticker)
            print(ticker)
            # If buy signal is detected then send message to user
            if (rsi_15m < low or rsi_1h < low):
                bot.send_message(message.chat.id, f'{ticker}\n\n15m: {rsi_15m}\n1h: {rsi_1h}')
                time.sleep(5)



bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
bot.infinity_polling()