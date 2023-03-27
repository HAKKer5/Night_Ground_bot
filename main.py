from datetime import datetime
import telebot
from pycbrf import ExchangeRates
import random
import time
#import config
from telebot import types
from cbrf.models import DailyCurrenciesRates

bot = telebot.TeleBot('5871761173:AAGzSfS3RSD5-cAh79U5omOEB2-P0X3mmZM')










@bot.message_handler(commands=['start'])
def start(message):
    is_subscribed = bot.get_chat_member('@NIGHT_GROUND', message.chat.id).status == 'member'
    if is_subscribed is True:
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn2 = telebot.types.KeyboardButton('📈 Курс')
        item3 = telebot.types.KeyboardButton("🎉 Розыгрыши")
        item2 = telebot.types.KeyboardButton("✅ Расчитать стоимость")
        #item4 = telebot.types.KeyboardButton("😊 Как дела?")
        item5 = telebot.types.KeyboardButton("🎁 Акции")
        markup.add(itembtn2,item5, item3, item2)
        bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЗаинтересовались покупкой в нашем магазине? Бот поможет рассчитать стоимость товара по актуальному курсу!".format(message.from_user, bot.get_me()),
            parse_mode='html', reply_markup=markup)


    else:
        markup = types.InlineKeyboardMarkup(row_width=2)
        item3 = types.InlineKeyboardButton("Подписаться", url='https://t.me/NIGHT_GROUND')

        markup.add(item3)
        bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nДля пользования ботом вам необходимо быть подписчиком нашего канала!".format(message.from_user, bot.get_me()),
            parse_mode='html', reply_markup=markup)

        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn2 = telebot.types.KeyboardButton('Готово!')
        markup.add(itembtn2)
        time.sleep(2)
        bot.send_message(message.chat.id, "Нажмите на Готово, как все сделаете".format(message.from_user, bot.get_me()),
            parse_mode='html', reply_markup=markup)



last_time = {}



@bot.message_handler(content_types=['text'])
def message(message):
    if message.chat.type == 'private':
        if message.text == 'Готово!':
            is_subscribed = bot.get_chat_member('@NIGHT_GROUND', message.chat.id).status == 'member'
            if is_subscribed is True:
                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                itembtn2 = telebot.types.KeyboardButton('📈 Курс')
                item3 = telebot.types.KeyboardButton("🎉 Розыгрыши")
                item2 = telebot.types.KeyboardButton("✅ Расчитать стоимость")
                #item4 = telebot.types.KeyboardButton("😊 Как дела?")
                item5 = telebot.types.KeyboardButton("🎁 Акции")
                markup.add(itembtn2,item5, item3, item2)
                bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЗаинтересовались покупкой в нашем магазине? Бот поможет рассчитать стоимость товара по актуальному курсу!".format(message.from_user, bot.get_me()),
                    parse_mode='html', reply_markup=markup)


            else:
                markup = types.InlineKeyboardMarkup(row_width=2)
                item3 = types.InlineKeyboardButton("Подписаться", url='https://t.me/NIGHT_GROUND')
                markup.add(item3)
                # bot.send_message(message.chat.id, "ХЕР!".format(message.from_user, bot.get_me()),
                #     parse_mode='html', reply_markup=markup)


        is_subscribed = bot.get_chat_member('@NIGHT_GROUND', message.chat.id).status == 'member'
        if is_subscribed is True:
            if message.text == '✅ Расчитать стоимость':


                    daily = DailyCurrenciesRates()
                    daily.date
                    daily.get_by_id('R01375').name
                    global price
                    a = float(daily.get_by_id('R01375').value)

                    ################################################################################################################################################################

                    #price = a / 10
                    price = a

                    ################################################################################################################################################################

                    print(round((price), 2), 'Расчет.', 'Команда от: {0.first_name} {0.last_name}. id: {0.username} '.format(message.from_user, bot.get_me()))

                    v = bot.send_message(message.chat.id, 'Введи стоимость товара в Юанях')
                    bot.register_next_step_handler(v, returning)


            elif message.text == 'Рандомное число':
                        bot.send_message(message.chat.id, str(random.randint(0,1000)))




            elif message.text == '📈 Курс':
                    daily = DailyCurrenciesRates()
                    daily.date
                    daily.get_by_id('R01375').name

                    a = float(daily.get_by_id('R01375').value)

                    ################################################################################################################################################################

                    #price = a / 10
                    price = a
                    
                    ################################################################################################################################################################

                    print(price, 'Курс.', 'Команда от: {0.first_name} {0.last_name}. id: {0.username} '.format(message.from_user, bot.get_me()))
                    bot.send_message(message.chat.id, f'Курс юаня на сегодня: {round((11.55), 2)}')

            elif message.text == '🎁 Акции':

                    bot.send_message(message.chat.id, '''Сейчас мы проводим акцию "ПРИВЕДИ ДРУГА".

    Если вы приводите друга, который оформляет заказ вмести с вами - скидка 500 руб ВАМ и ДРУГУ!''')
                    print('Акции.', 'Команда от: {0.first_name} {0.last_name}. id: {0.username} '.format(message.from_user, bot.get_me()))

            elif message.text == '🎉 Розыгрыши':
                        is_subscribed = bot.get_chat_member('@NIGHT_GROUND', message.chat.id).status == 'member'
                        if is_subscribed is True:
                            bot.send_message(message.chat.id, "Уже совсем скоро! Следите за новостями в нашем канале.")
                            print('Розыгрыш.', 'Команда от: {0.first_name} {0.last_name}. id: {0.username} '.format(message.from_user, bot.get_me()))
                        else:
                            markup = types.InlineKeyboardMarkup(row_width=69)
                            item3 = types.InlineKeyboardButton("Подписаться", url='https://t.me/NIGHT_GROUND')
                            markup.add(item3)
                            bot.send_message(message.chat.id, f'Для участия в розыгрышах вам необходимо быть подписчиком нашего канала!', reply_markup=markup)
            elif message.text == 'Готово!':
                print('fake_error', 'Команда от: {0.first_name} {0.last_name}. id: {0.username} '.format(message.from_user, bot.get_me()))


            else:
                    bot.send_message(message.chat.id, '''Я не знаю что ответить 😢
        Нажмите /start''')
        else:
            markup = types.InlineKeyboardMarkup(row_width=2)
            item3 = types.InlineKeyboardButton("Подписаться", url='t.me/NIGHT_GROUND')

            markup.add(item3)
            bot.send_message(message.chat.id, "Для пользования ботом вам необходимо быть подписчиком нашего канала!".format(message.from_user, bot.get_me()),
                parse_mode='html', reply_markup=markup)

            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn2 = telebot.types.KeyboardButton('Готово!')
            markup.add(itembtn2)
            time.sleep(2)
            bot.send_message(message.chat.id, "Нажмите на Готово, как все сделаете".format(message.from_user, bot.get_me()),
                parse_mode='html', reply_markup=markup)



@bot.message_handler(commands=['return'])
def returning(message):
    if message.text.isdigit():
        d = int(message.text)

        if d >= 100000000:
            print("Слишком много")
            bot.send_message(message.chat.id, f'Сликом большое число!')
        else:
           if d <= 500:
                m = round((d *(11.55)+1400+700))
                bot.send_message(message.chat.id, f'Итоговая стоимость без доставки {m} руб.')
                markup = types.InlineKeyboardMarkup(row_width=2)
                item3 = types.InlineKeyboardButton("Связаться", url='https://t.me/MANAGER_NIGHT_GROUND')
                markup.add(item3)
                bot.send_message(message.chat.id, f'Для расчета стоимости доставки и оформления заказа, свяжитесь с менеджером.', reply_markup=markup)

                print(message.text)

           elif d >= 501:
                m = round((d *(11.55) + 700))
                last_price = round(m + (m/100*15))
                bot.send_message(message.chat.id, f'Итоговая стоимость без доставки {last_price} руб.')
                markup = types.InlineKeyboardMarkup(row_width=2)
                item3 = types.InlineKeyboardButton("Связаться", url='https://t.me/MANAGER_NIGHT_GROUND')
                markup.add(item3)
                bot.send_message(message.chat.id, f'Для расчета стоимости доставки и оформления заказа, свяжитесь с менеджером.', reply_markup=markup)

                print(message.text)

    else:
        bot.reply_to(message, f'Введите только число!')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'svaz':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                    text="С наступающим!")

    except Exception as e:
        print(repr(e))








bot.polling(none_stop=True)