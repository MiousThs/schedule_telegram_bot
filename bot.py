import config
import telebot
import para
bot = telebot.TeleBot(config.token)

pola = para.Para(config.database_name)

@bot.message_handler(commands=['start'])
def start_menu(message):
	markup = telebot.types.ReplyKeyboardMarkup()
	markup.row('/next', '/week')
	markup.row('/today', '/tomorrow')
	bot.send_message(message.chat.id, 'It`s time to choose..', reply_markup=markup)

@bot.message_handler(commands=['next'])
def next_para(message):
	bot.send_message(message.chat.id, pola.get_next())

@bot.message_handler(commands=['today'])
def today_paru(message):
	bot.send_message(message.chat.id, 'Зараз перевірю в розкладі...')
	bot.send_message(message.chat.id, pola.get_today())

@bot.message_handler(commands=['tomorrow'])
def tomorrow_paru(message):
	bot.send_message(message.chat.id, 'Хмм...завтра:')
	bot.send_message(message.chat.id, pola.get_tomorrow())

@bot.message_handler(commands=['week'])
def what_week(message):
	bot.send_message(message.chat.id, pola.get_week())

@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
	bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
	bot.polling(none_stop=True)