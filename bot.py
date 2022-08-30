import telebot
from telebot import types
from dict import dict

dicts = dict()
token = dicts['token']
bot=telebot.TeleBot(token)

global zacaz
zacaz = {}

#Обработчик анкеты
def name1(message):
	zacaz[message.from_user.id] = message.text
	msg = bot.send_message(message.chat.id, dicts['tel'])
	bot.register_next_step_handler(msg, tel)
	zacaz[message.from_user.id] = zacaz[message.from_user.id] + '\n' + '1'

def name2(message):
	zacaz[message.from_user.id] = message.text
	msg = bot.send_message(message.chat.id, dicts['tel'])
	bot.register_next_step_handler(msg, tel)
	zacaz[message.from_user.id] = zacaz[message.from_user.id] + '\n' + '2'

def name3(message):
	zacaz[message.from_user.id] = message.text
	msg = bot.send_message(message.chat.id, dicts['tel'])
	bot.register_next_step_handler(msg, tel)
	zacaz[message.from_user.id] = zacaz[message.from_user.id] + '\n' + '3'

def tel(message):
	zacaz[message.from_user.id] = zacaz[message.from_user.id] + '\n' + message.text
	msg = bot.send_message(message.chat.id, dicts['cyte'])
	bot.register_next_step_handler(msg, cyte)

def cyte(message):
	zacaz[message.from_user.id] = zacaz[message.from_user.id] + '\n' + message.text
	msg = bot.send_message(message.chat.id, dicts['np'])
	bot.register_next_step_handler(msg, np)	

def np(message):
	zacaz[message.from_user.id] = zacaz[message.from_user.id] + '\n' + message.text
	bot.send_message(message.chat.id, text = '<code>' + dicts['nambe_kart'] + '</code> \n' + dicts['screen'], \
			parse_mode = "HTML")

@bot.message_handler(content_types=["photo"])
def screen(message):
	try:
		bot.send_message(dicts['TO_ID'], zacaz[message.from_user.id])
		#a = message.photo.file_id
		#bot.send_photo(dicts['TO_ID'], a)
# Получаем id фотографии в Telegram
		photo_id = message.photo[-1].file_id
# Достаём картинку
		photo_file = bot.get_file(photo_id) # <class 'telebot.types.File'>
		photo_bytes = bot.download_file(photo_file.file_path) # <class 'bytes'>
# Отправить в дальнейшем можно таким образом
		del zacaz[message.from_user.id]
		bot.send_photo(dicts['TO_ID'], photo=photo_bytes)

		bot.send_message(message.chat.id, text = dicts['sencs1'])
		bot.send_message(message.chat.id, text = dicts['sencs2'])	
	except:
		pass


#обработчик ствртовой страницы
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(dicts['button1'])
    btn2 = types.KeyboardButton(dicts['button2'])
    btn3 = types.KeyboardButton(dicts['button3'])
    markup.add(btn1, btn3)
    markup.add(btn2)
    bot.send_message(message.chat.id, dicts['starts'].format(message.from_user), reply_markup=markup, \
        parse_mode = "HTML")

#обраьотчик клавиатуры
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == dicts['button1']):
        markup = types.InlineKeyboardMarkup()
        manual = types.InlineKeyboardButton(text = dicts['manual'], callback_data='manual')
        markup.add(manual)
        tea = types.InlineKeyboardButton(text = dicts['tea'], callback_data='tea')
        markup.add(tea)
        bot.send_message(message.chat.id, text = dicts['protea'], reply_markup=markup)

    elif(message.text == dicts['button2']):
        markup = types.InlineKeyboardMarkup()
        u1 = types.InlineKeyboardButton(text = dicts['v1'], callback_data='u1')
        markup.add(u1)
        u2 = types.InlineKeyboardButton(text = dicts['v2'], callback_data='u2')
        markup.add(u2)
        u3 = types.InlineKeyboardButton(text = dicts['v3'], callback_data='u3')
        markup.add(u3)
        bot.send_message(message.chat.id, text = dicts['select'], reply_markup=markup)

    elif(message.text == dicts['button3']):
        markup_url = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(dicts['insta'], url = dicts['url_inst'])
        markup_url.add(btn1)
        btn2 = types.InlineKeyboardButton(dicts['telega'], url = dicts['telega_url'])
        markup_url.add(btn2)
        bot.send_message(message.chat.id, text = dicts['go_insta'], reply_markup=markup_url)

#обработчик кнопок
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'u1':
        markup = types.InlineKeyboardMarkup()
        karta = types.InlineKeyboardButton(text = dicts['kart1'], callback_data='karta1')
        markup.add(karta)	
        bot.send_message(call.message.chat.id, text = dicts['vz'] + '\n' + dicts['v1'], reply_markup=markup)

    elif call.data == 'u2':
        markup = types.InlineKeyboardMarkup()
        karta = types.InlineKeyboardButton(text = dicts['kart2'], callback_data='karta2')
        markup.add(karta)
        bot.send_message(call.message.chat.id, text = dicts['vz'] + '\n' + dicts['v2'], reply_markup=markup)

    elif call.data == 'u3':
        markup = types.InlineKeyboardMarkup()
        karta = types.InlineKeyboardButton(text = dicts['kart3'], callback_data='karta3')
        markup.add(karta)	
        bot.send_message(call.message.chat.id, text = dicts['vz'] + '\n' + dicts['v3'], reply_markup=markup)

    elif call.data == 'karta1':
        msg = bot.send_message(call.message.chat.id, dicts['name'])
        bot.register_next_step_handler(msg, name1)

    elif call.data == 'karta2':
        msg = bot.send_message(call.message.chat.id, dicts['name'])
        bot.register_next_step_handler(msg, name2)

    elif call.data == 'karta3':
        msg = bot.send_message(call.message.chat.id, dicts['name'])
        bot.register_next_step_handler(msg, name3)

    elif call.data == 'manual':
        markup = types.InlineKeyboardMarkup()
        tea = types.InlineKeyboardButton(text = dicts['tea'], callback_data='tea')
        markup.add(tea)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, \
            text= dicts['manual_text'], parse_mode = "HTML", reply_markup=markup) 

    elif call.data == 'tea':
        markup = types.InlineKeyboardMarkup()
        manual = types.InlineKeyboardButton(text = dicts['manual'], callback_data='manual')
        markup.add(manual)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, \
            text= dicts['tea_text'], parse_mode = "HTML", reply_markup=markup)



if __name__ == '__main__': 
    try:
       bot.polling(none_stop=True) 
    except Exception as e:
       print(e) 
       time.sleep(15)