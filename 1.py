import telebot
import config
from telebot import types
from string import Template
bot = telebot.TeleBot(config.token)
user_dict = {}
class User:
	def __init__(self, SET):
		self.SET = SET
		keys = ['fullname', 'phone', 'adress','append']
		for key in keys:
			self.key = None
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True, row_width=2)
	itembtn2 = types.KeyboardButton('/info')
	itembtn3 = types.KeyboardButton('/Заказ')
	itembtn4 = types.KeyboardButton('/Адрес')
	markup.add(itembtn2, itembtn3,itembtn4)
	bot.send_message(message.chat.id, "Сәлеметсізбе "+str(message.from_user.first_name)+',Pasha-ға қош келдіңіз.',reply_markup=markup)
@bot.message_handler(commands=['info'])
def send_about(message):
	markup = types.InlineKeyboardMarkup()
	btn_my_site= types.InlineKeyboardButton(text='Наша инста', url='https://www.instagram.com/pasha.taraz/')
	btn_my_wat = types.InlineKeyboardButton(text='whatsapp', url='wa.me/77077889977')
	markup.add(btn_my_site,btn_my_wat)
	bot.send_message(message.chat.id,'При Заказе на доставку от 5000тг.Coca-Cola в ПОДАРОК.')
	bot.send_message(message.chat.id, "Нажми на кнопку и перейди", reply_markup = markup)
@bot.message_handler(commands=['Адрес'])
def send_about(message):
	bot.send_message(message.chat.id,'Бауыржан Момышулы 2г/11 микр. Рядом(Остановка Жансая)')
@bot.message_handler(commands=['Заказ'])
def send_about(message):
	markup_inline = types.InlineKeyboardMarkup()
	button_turik = types.InlineKeyboardButton(text="🇹🇷  Завтрак", callback_data='breakfast/turik')
	button_salad = types.InlineKeyboardButton(text="Салат", callback_data='salad')
	button_2 = types.InlineKeyboardButton(text="2-блюда", callback_data='2')
	button_2_turik = types.InlineKeyboardButton(text="🇹🇷  блюда", callback_data='2_turik')
	button_kebab = types.InlineKeyboardButton(text="Шашлыки	🍢", callback_data='kebab')
	button_pide = types.InlineKeyboardButton(text="Пиде",callback_data='pide')
	button_pizza = types.InlineKeyboardButton(text="Пицца 🍕",callback_data='pizza')
	button_doner = types.InlineKeyboardButton(text="🌯&🌭",callback_data='doner/hot-dogs')
	button_chicken = types.InlineKeyboardButton(text="🍔&🍗",callback_data='burger/chicken')
	button_tea = types.InlineKeyboardButton(text="К чаю🥧",callback_data='tea')
	button_drinks = types.InlineKeyboardButton(text="Напитки🥤",callback_data='drinks')
	markup_inline.add(button_turik,button_salad,button_2,button_2_turik,button_kebab,button_pide,button_pizza,button_doner,button_chicken,button_tea,button_drinks)
	bot.send_message(message.chat.id,'танданыз:',reply_markup=markup_inline)












































@bot.callback_query_handler(func = lambda call: call.data == 'tea')
def answer(call):
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	itembtn1 = types.KeyboardButton('Пахлава(150тг)')
	itembtn2 = types.KeyboardButton('Лимон(150тг)')
	itembtn3 = types.KeyboardButton('Мед(200тг)')
	itembtn4 = types.KeyboardButton('Ревани(200тг)')
	markup.add(itembtn1,itembtn2,itembtn3,itembtn4)
	msg = bot.send_photo(call.message.chat.id, open("tea.png",'rb'),timeout=1000,reply_markup=markup)
	bot.register_next_step_handler(msg, process_city_step)
@bot.callback_query_handler(func = lambda call: call.data == 'drinks')
def answer(call):
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	itembtn1=types.KeyboardButton(text="1Л Cola/Sprite/Fanta")
	itembtn2=types.KeyboardButton(text="1Л Фьюс чай")
	itembtn3=types.KeyboardButton(text="1Л Сок Пико")
	itembtn4=types.KeyboardButton(text="1Л Бонаква")
	itembtn5=types.KeyboardButton(text="1Л Турецкий лимонад")
	itembtn6=types.KeyboardButton(text="1Л Турецкий айран")
	itembtn7=types.KeyboardButton(text="1Л Фруктовый компот")
	markup.add(itembtn1,itembtn2,itembtn3,itembtn4,itembtn5,itembtn6,itembtn7)
	msg = bot.send_photo(call.message.chat.id, photo=open("drinks.png",'rb'), timeout=1000,reply_markup=markup)
	bot.register_next_step_handler(msg, process_city_step)
@bot.callback_query_handler(func = lambda call: call.data == 'breakfast/turik')
def answer(call):
	keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	itembtn1=types.KeyboardButton(text="Турецкий завтрак")
	itembtn2=types.KeyboardButton(text="Омлет с овощами")
	itembtn3=types.KeyboardButton(text="Глазунья")
	itembtn4=types.KeyboardButton(text="Яичница с сыром")
	itembtn5=types.KeyboardButton(text="Сытный завтрак с котлетой")
	keyboard.add(itembtn1,itembtn2,itembtn3,itembtn4,itembtn5)
	msg = bot.send_photo(call.message.chat.id, open("breakfast.png",'rb'), timeout=1000,reply_markup=keyboard)
	bot.register_next_step_handler(msg, process_city_step)
@bot.callback_query_handler(func = lambda call: call.data == 'salad')
def answer(call):
	keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	itembtn1=types.KeyboardButton(text="Чобан салат")
	itembtn2=types.KeyboardButton(text="Греческий салат")
	itembtn3=types.KeyboardButton(text="Ачучук(острый)")
	itembtn4=types.KeyboardButton(text="Оливье")
	itembtn5=types.KeyboardButton(text="Свежий")
	itembtn6=types.KeyboardButton(text="Грибной салат(горячий)")
	itembtn7=types.KeyboardButton(text="Нежность")
	keyboard.add(itembtn1,itembtn2,itembtn3,itembtn4,itembtn5,itembtn6,itembtn7)
	msg = bot.send_photo(call.message.chat.id, open("salad.png",'rb'), timeout=1000,reply_markup=keyboard)
	bot.register_next_step_handler(msg, process_city_step)
@bot.callback_query_handler(func = lambda call: call.data == '2_turik')
def answer(call):
	keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	itembtn1=types.KeyboardButton(text="Pilav doner et")
	itembtn2=types.KeyboardButton(text="Pilav doner tavuk")
	itembtn3=types.KeyboardButton(text="Choban kavurma")
	itembtn4=types.KeyboardButton(text="Inegol kofte")
	itembtn5=types.KeyboardButton(text="Турецкий Сырбаз")
	itembtn6=types.KeyboardButton(text="Tavuk kavurma")
	itembtn7=types.KeyboardButton(text="Pideli kofte")
	itembtn8=types.KeyboardButton(text="Iskender kebab")
	itembtn9=types.KeyboardButton(text="Patlican kebab")
	itembtn10=types.KeyboardButton(text="Doner tabak tavuk")
	itembtn11=types.KeyboardButton(text="Аль-назик")
	itembtn12=types.KeyboardButton(text="Doner Tabak")
	itembtn13=types.KeyboardButton(text="Sach Tava")
	itembtn14=types.KeyboardButton(text="Giger Tava")
	keyboard.add(itembtn1,itembtn2,itembtn3,itembtn4,itembtn5,itembtn6,itembtn7,itembtn8,itembtn9,itembtn10,itembtn11,itembtn12,itembtn13,itembtn14)
	bot.send_photo(call.message.chat.id, open("2_turik.png",'rb'), timeout=1000,reply_markup=keyboard)
	msg = bot.send_photo(call.message.chat.id, open("2turik.png",'rb'), timeout=1000,reply_markup=keyboard)
	bot.register_next_step_handler(msg, process_city_step)
@bot.callback_query_handler(func = lambda call: call.data == '2')
def answer(call):
	keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	itembtn1=types.KeyboardButton(text="Манты")
	itembtn2=types.KeyboardButton(text="Бефстроганов")
	itembtn3=types.KeyboardButton(text="Жаренные манты")
	itembtn4=types.KeyboardButton(text="Куырдак")
	keyboard.add(itembtn1,itembtn2,itembtn3,itembtn4)
	msg = bot.send_photo(call.message.chat.id, open("2.png",'rb'), timeout=1000,reply_markup=keyboard)
	bot.register_next_step_handler(msg, process_city_step)
@bot.callback_query_handler(func = lambda call: call.data == 'kebab')
def answer(call):
	keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	itembtn1=types.KeyboardButton(text="Kuzu şiş")
	itembtn2=types.KeyboardButton(text="Tavuk şiş")
	itembtn3=types.KeyboardButton(text="Adana kebab")
	itembtn4=types.KeyboardButton(text="Urfa kebab")
	itembtn5=types.KeyboardButton(text="Pirzola")
	itembtn6=types.KeyboardButton(text="Adana dürüm на лаваше")
	itembtn7=types.KeyboardButton(text="Urfa dürüm на лаваше")
	itembtn8=types.KeyboardButton(text="Kuzu dürüm на лаваше")
	keyboard.add(itembtn1,itembtn2,itembtn3,itembtn4,itembtn5,itembtn6,itembtn7,itembtn8)
	msg = bot.send_photo(call.message.chat.id, open("kebab.png",'rb'), timeout=1000,reply_markup=keyboard)
	bot.register_next_step_handler(msg, process_city_step)
@bot.callback_query_handler(func = lambda call: call.data == 'pide')
def answer(call):
	keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	itembtn1=types.KeyboardButton(text="Пиде с сыром")
	itembtn2=types.KeyboardButton(text="Пиде(куриный донер)")
	itembtn3=types.KeyboardButton(text="Пиде(мясо донера)")
	itembtn4=types.KeyboardButton(text="Хачапури")
	itembtn5=types.KeyboardButton(text="Пиде(фарш)")
	itembtn6=types.KeyboardButton(text="Пиде(ассорти)")
	itembtn7=types.KeyboardButton(text="Лахмаджун")
	keyboard.add(itembtn1,itembtn2,itembtn3,itembtn4,itembtn5,itembtn6,itembtn7)
	msg = bot.send_photo(call.message.chat.id, open("pide.png",'rb'), timeout=1000,reply_markup=keyboard)
	bot.register_next_step_handler(msg, process_city_step)
@bot.callback_query_handler(func = lambda call: call.data == 'pizza')
def answer(call):
	keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	itembtn1=types.KeyboardButton(text="Маргарита")
	itembtn2=types.KeyboardButton(text="Мексикано")
	itembtn3=types.KeyboardButton(text="Пицца BBQ")
	itembtn4=types.KeyboardButton(text="Пепперони с халапеньо")
	itembtn5=types.KeyboardButton(text="4 сезона")
	itembtn6=types.KeyboardButton(text="Фирменная пицца от Pasha")
	itembtn7=types.KeyboardButton(text="Пицца Донер")
	itembtn8=types.KeyboardButton(text="Пицца с курицей")
	keyboard.add(itembtn1,itembtn2,itembtn3,itembtn4,itembtn5,itembtn6,itembtn7,itembtn8)
	msg = bot.send_photo(call.message.chat.id, open("pizza.png",'rb'), timeout=1000,reply_markup=keyboard)
	bot.register_next_step_handler(msg, process_city_step)
@bot.callback_query_handler(func = lambda call: call.data == 'doner/hot-dogs')
def answer(call):
	keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	itembtn1=types.KeyboardButton(text="Куриный донер")
	itembtn2=types.KeyboardButton(text="Куриный донер-бургер")
	itembtn3=types.KeyboardButton(text="Куриный донер полтора(1,5)")
	itembtn4=types.KeyboardButton(text="Говяжий донер")
	itembtn5=types.KeyboardButton(text="Говяжий донер полтора(1,5)")
	itembtn6=types.KeyboardButton(text="Ассорти донер")
	itembtn7=types.KeyboardButton(text="Ассорти донер полтора(1,5)")
	itembtn8=types.KeyboardButton(text="Куриный донер в батоне")
	itembtn9=types.KeyboardButton(text="Говяжий донер в батоне")
	itembtn10=types.KeyboardButton(text="Хот-дог с сардельками")
	itembtn11=types.KeyboardButton(text="Хот-дог с охотничьими сардельками")
	keyboard.add(itembtn1,itembtn2,itembtn3,itembtn4,itembtn5,itembtn6,itembtn7,itembtn8,itembtn9,itembtn10,itembtn11)
	msg = bot.send_photo(call.message.chat.id, open("donner.png",'rb'), timeout=1000,reply_markup=keyboard)
	bot.register_next_step_handler(msg, process_city_step)
@bot.callback_query_handler(func = lambda call: call.data == 'burger/chicken')
def answer(call):
	keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	itembtn1=types.KeyboardButton(text="Крылышки 6шт")
	itembtn2=types.KeyboardButton(text="Крылышки 12шт")
	itembtn12=types.KeyboardButton(text="Крылышки 24шт")
	itembtn3=types.KeyboardButton(text="Крылышки 32шт")
	itembtn4=types.KeyboardButton(text="Гамбургер(говяж)")
	itembtn5=types.KeyboardButton(text="Чизбургер(говяж)")
	itembtn6=types.KeyboardButton(text="Дабл бургер(говяж)")
	itembtn7=types.KeyboardButton(text="Дабл чизбургер(говяж)")
	itembtn8=types.KeyboardButton(text="Гамбургер(кур)")
	itembtn9=types.KeyboardButton(text="Чизбургер(кур)")
	itembtn10=types.KeyboardButton(text="Дабл бургер(кур)")
	itembtn11=types.KeyboardButton(text="Дабл чизбургер(кур)")
	keyboard.add(itembtn1,itembtn2,itembtn3,itembtn4,itembtn5,itembtn6,itembtn7,itembtn8,itembtn9,itembtn10,itembtn11,itembtn12)
	msg = bot.send_photo(call.message.chat.id, open("burger.png",'rb'), timeout=1000,reply_markup=keyboard)
	bot.register_next_step_handler(msg, process_city_step)
def process_city_step(message):
	chat_id = message.chat.id
	user_dict[chat_id] = User(message.text)

	# удалить старую клавиатуру
	markup = types.ReplyKeyboardRemove(selective=False)

	msg = bot.send_message(chat_id, 'Напишите адрес доставки:', reply_markup=markup)
	bot.register_next_step_handler(msg, adress)
def adress(message):

	chat_id = message.chat.id
	user = user_dict[chat_id]
	user.adress = message.text

	msg = bot.send_message(chat_id, 'Номер телефона:')
	bot.register_next_step_handler(msg, process_phone_step)
def process_phone_step(message):

	try:
		int(message.text)
		chat_id = message.chat.id
		user = user_dict[chat_id]
		user.phone = message.text

		msg = bot.send_message(chat_id, 'Тагы зат косу:')
		bot.register_next_step_handler(msg, append)
	except Exception as e:
		msg = bot.reply_to(message, 'Вы ввели что то другое. Пожалуйста введите номер телефона.')
		bot.register_next_step_handler(msg, process_phone_step)
def append(message):

	chat_id = message.chat.id
	user = user_dict[chat_id]
	user.append= message.text

	msg = bot.send_message(chat_id, 'Имя:')
	bot.register_next_step_handler(msg, process_carDate_step)
def process_carDate_step(message):

	chat_id = message.chat.id
	user = user_dict[chat_id]
	user.fullname = message.text

		# ваша заявка "Имя пользователя"
	bot.send_message(chat_id, getRegData(user, 'Спасибо, Ваш заказ принят! Ожидайте звонка менеджера! Pasha!.\n Ваша заявка:', message.from_user.first_name ), parse_mode="Markdown")
		# отправить в группу
	bot.send_message(config.chat_id, getRegData(user, 'Заявка от бота', bot.get_me().username), parse_mode="Markdown")
	bot.send_message(chat_id, 'кайтадан /start ')
def getRegData(user, title, name):
	t = Template('$title *$name* \n заказ: *$userSET* \n имя: *$fullname* \n Телефон: *$phone* \n Адрес: *$adress* \n Тагы косатын: *$append*')
	return t.substitute({
		'title': title,
		'name': name,
		'userSET': user.SET,
		'fullname': user.fullname,
		'phone': user.phone,
		'adress': user.adress,
		'append': user.append,
	})
@bot.message_handler(content_types=["text"])
def send_help(message):
    bot.send_message(message.chat.id, 'Помощь - /help')
@bot.message_handler(content_types=["photo"])
def send_help_text(message):
    bot.send_message(message.chat.id, 'Напишите текст')
bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()