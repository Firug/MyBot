import telebot as tl
# переменная, отвечающая за бота
bot = tl.TeleBot('1424798953:AAHVYXlwr4WG-oOOidUmfvqOCgmKvu3hoVU')
# декоратор, с помощью которого бот будет отвечать на /start
@bot.message_handler(commands=['start'])
# реакция на комманду 'start'
def start_message(message):
	bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

@bot.message_handler(content_types=['text'])
# реакция на обычные сообщения
def send_message(message):
	if message.text.lower() == 'привет':
		bot.send_message(message.chat.id, 'Привет, круто программируешь')
	elif message.text.lower() == 'я тебя боюсь':
		bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMbX6JAo49t5hoFnq4tdNm5uBxdufQAAhgBAAL3AsgPwrhLNhgCELoeBA')
	else:
		bot.send_message(message.chat.id, 'неплохо для начала')

#отправка стикера^
@bot.message_handler(content_types = ['sticker'])
# узнаем id файла
def message_get(message):
	print(message)
# с помощью polling бот будет обновляться
bot.polling()