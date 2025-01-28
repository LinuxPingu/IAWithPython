import telebot;
import requests;
import json;
from apify_client import ApifyClient;

#https://colab.research.google.com/drive/1XogD5Ocwicp7CEvBCkqYJ7QnpBy1xuRy?usp=sharing

APIKey = "7752286654:AAHBhKDArDDNyvtHWy35bLacE47EeADpgAA";
APIFY_Key = "apify_api_EthNWfh1g4XL1q4rvihriMlKstBdat12XJRw";

client = ApifyClient(APIFY_Key)

# Prepare the Actor input
run_input = { "usernames": ["daniel.hernandez0599"] }

# Run the Actor and wait for it to finish
run = client.actor("shu8hvrXbJbY3Eb9W").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)

bot = telebot.TeleBot(APIKey);

@bot.message_handler(commands=['start','help'])
def sendWelcome(message):
    bot.reply_to(message, "Mi bot Silent King ")

@bot.message_handler(func=lambda message:True)
def echo_all(message):
    bot.reply_to(message, "Mensaje Recibido: "+ message.text)
bot.polling()

