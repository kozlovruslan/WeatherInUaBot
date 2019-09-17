import telebot
import pyowm

owm = pyowm.OWM('2a20de11e71df20b380c797a60cc3749', language = "ua")
bot = telebot.TeleBot("976304578:AAEFKNuvi7D2Yv5d5mcV3yiO_dgPy1np7wE")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place( message.text )
	w = observation.get_weather()
	temp = w.get_temperature('celsius')["temp"]

	answer = "В місті " + message.text + " зараз " + w.get_detailed_status() + "\n"
	answer += "Температура зараз біля " + str(temp) + "\n\n"

	if temp < 10:
		answer +=("Брр як холодно, одягни шапку і теплі штани з начьосом!")
	elif temp < 16:
		answer += ("Щось зимно, одягайся тепліше")
	elif temp < 20:
		answer +=("Прохолодно, не забудь одягнути куртку")
	else:
		answer +=("На вулиці жарко, одягай шорти і гайда на пляж!")

	bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )
