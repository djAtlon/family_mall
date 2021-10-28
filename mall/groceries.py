from io import BufferedRandom
from typing import Text
import telebot
from telebot import types
from config import TOKEN
from keyboa import Keyboa


def main():
    bot = telebot.TeleBot(TOKEN)
    mi_id = None
    to_buy = []
    groceires_type = ["Пластиковая продукция", "Приправы", "Мясные продукты", 'Овощи и фрукты' , "Молочные продукты", "Чипсы и прочее", "Сладкое", "Бумажная продукция", "Яйца", "Алкоголь и остальная вода"]
    spices = ['', '', '']
    vegetables__fruits = ['Бананы', "Яблоки", "Мандарины", "Апельсины", "Груши", "Манго", "Киви", "Лимоны", "Помидоры", "Огурцы", "Лук", "Грибы"]
    sweet = ['Печенье', 'Конфеты', 'Шоколадки', 'Торт', 'Выпечка']
    meat = ['Сосиски', 'Филе', 'Крылья', 'Бедра', 'Ножки', 'Печенка куриная', "Колбаса", "Бекон"]

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.send_message(message.chat.id, 'Бот создан для автоматизации покупок продуктов домой. Тоесть можно не звонить, не писать и тд, главное при себе иметь интернет :) . Сообщения со списком будут приходить мне автоматически. Для более детальной информации напишите /help')

    @bot.message_handler(commands=['help'])
    def send_help(message):
        bot.send_message(message.chat.id, 'Как было уже сказано - бот создан для удобства, чтобы никого не отвлекать. Для тех кто редко пользуется телеграммом или вовсе не знаком с ним: \
все команды начинаются с символа слеш (/). При вводе его в сообщение можно просмотреть все команды. Для удобства выведу список команд которые есть на данном этапе:\n\n\
/start - начать работу с ботом\n\
/help - получить более детальную информацию про бота\n\
/buy - создать список продуктов\n\
/end - завершить список покупок\n\n\
Если что-то не понятно пишите @curkymflex')
    
    @bot.message_handler(commands=['buy'])
    def start_shopping(message):
        plastic_produtcts_btn = types.InlineKeyboardButton(groceires_type[0], callback_data=1)
        spices_products_btn = types.InlineKeyboardButton(groceires_type[1], callback_data=2)
        meat_products_btn = types.InlineKeyboardButton(groceires_type[2], callback_data=3)
        veg_fruits_products_btn = types.InlineKeyboardButton(groceires_type[3], callback_data=4)
        milk_products_btn = types.InlineKeyboardButton(groceires_type[4], callback_data=5)
        snack_products_btn = types.InlineKeyboardButton(groceires_type[5], callback_data=6)
        sweet_products_btn = types.InlineKeyboardButton(groceires_type[6], callback_data=7)
        paper_products_btn = types.InlineKeyboardButton(groceires_type[7], callback_data=8)
        eggs_btn = types.InlineKeyboardButton(groceires_type[8], callback_data=9)
        alco_water_products_btn = types.InlineKeyboardButton(groceires_type[-1], callback_data=10)
        
        markup = types.InlineKeyboardMarkup(row_width=2).add(plastic_produtcts_btn)
        markup.add(spices_products_btn, meat_products_btn)
        markup.add(veg_fruits_products_btn, milk_products_btn)
        markup.add(snack_products_btn, sweet_products_btn)
        markup.add(paper_products_btn, eggs_btn, alco_water_products_btn)
        bot.send_message(message.chat.id, text='Выберете категерию продуктов', reply_markup=markup)

    # @bot.message_handler(commands=['buy'])
    # def start_shopping(message):
    #     kb_porducts = Keyboa(items=)
    #     bot.send_message(message.chat.id, text = 'Выберете категорию продкутов', reply_markup=kb_porducts.keyboard)
    
    @bot.callback_query_handler(func=lambda call: True)
    def show_product_category(call):
        # Making keyboard for vegetables and fruits
        markup_veg = types.InlineKeyboardMarkup()

        ban_btn = types.InlineKeyboardButton(vegetables__fruits[0], callback_data=11)
        apple_btn = types.InlineKeyboardButton(vegetables__fruits[1], callback_data=12)

        tangerines_btn = types.InlineKeyboardButton(vegetables__fruits[2], callback_data=13)
        oranges_btn = types.InlineKeyboardButton(vegetables__fruits[3], callback_data=14)

        pears_btn = types.InlineKeyboardButton(vegetables__fruits[4], callback_data=15)
        mango_btn = types.InlineKeyboardButton(vegetables__fruits[5], callback_data=16)

        kiwi_btn = types.InlineKeyboardButton(vegetables__fruits[6], callback_data=17)
        lemons_btn = types.InlineKeyboardButton(vegetables__fruits[7], callback_data=18)

        tomatoes_btn = types.InlineKeyboardButton(vegetables__fruits[8], callback_data=19)
        cucumbers_btn = types.InlineKeyboardButton(vegetables__fruits[9], callback_data=20)

        onion_btn = types.InlineKeyboardButton(vegetables__fruits[10], callback_data=21)
        mushrooms_btn = types.InlineKeyboardButton(vegetables__fruits[11], callback_data=22)

        markup_veg.add(ban_btn, apple_btn)
        markup_veg.add(tangerines_btn, oranges_btn)
        markup_veg.add(pears_btn, mango_btn)
        markup_veg.add(kiwi_btn, lemons_btn)
        markup_veg.add(tomatoes_btn, cucumbers_btn)
        markup_veg.add(onion_btn, mushrooms_btn)
        #-----------------------------------------------

        # Making keyboard for smth sweet
        markup_sweet = types.InlineKeyboardMarkup()
        
        cookie_btn = types.InlineKeyboardButton(sweet[0], callback_data=23)
        candy_btn = types.InlineKeyboardButton(sweet[1], callback_data=24)

        chocolate_btn = types.InlineKeyboardButton(sweet[2], callback_data=25)
        cake_btn = types.InlineKeyboardButton(sweet[3], callback_data=26)
        bakery_btn = types.InlineKeyboardButton(sweet[4], callback_data=27)

        markup_sweet.add(cookie_btn, candy_btn, cake_btn)
        markup_sweet.add(chocolate_btn, bakery_btn)
        #-----------------------------------------------

        # Making keyboard for meat
        markup_meat = types.InlineKeyboardMarkup()

        sausages_btn = types.InlineKeyboardButton(meat[0], callback_data=28)
        fillet_btn = types.InlineKeyboardButton(meat[1], callback_data=29)
        wings_btn = types.InlineKeyboardButton(meat[2], callback_data=30)
        hips_btn = types.InlineKeyboardButton(meat[3], callback_data=31)
        legs_btn = types.InlineKeyboardButton(meat[4], callback_data=32)
        liver_btn = types.InlineKeyboardButton(meat[5], callback_data=33)
        kolbasa_btn = types.InlineKeyboardButton(meat[6], callback_data=34)
        bacon_btn = types.InlineKeyboardButton(meat[7], callback_data=35)

        markup_meat.add(sausages_btn, fillet_btn)
        markup_meat.add(wings_btn, hips_btn)
        markup_meat.add(legs_btn, liver_btn)
        markup_meat.add(kolbasa_btn, bacon_btn)
        #-------------------------------------------------------------

        # Making plastic products
        markup_plastic = types.InlineKeyboardMarkup()

        bot.answer_callback_query(callback_query_id=call.id, text = '')
        if call.data == '3':
            bot.send_message(call.message.chat.id, reply_markup=markup_meat, text='Выберете что-то из мясных продуктов')
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        if call.data == '4':
            bot.send_message(call.message.chat.id, reply_markup=markup_veg, text='Выберете фрукты или овощи')
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        if call.data == '7':
            bot.send_message(call.message.chat.id, reply_markup=markup_sweet, text='Выберете что-то из сладкого')
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        


    bot.polling()

if __name__ == '__main__':
    main()