from io import BufferedRandom
from typing import Text
import telebot
from telebot import types
from config import TOKEN
from keyboa import Keyboa

def main():
    bot = telebot.TeleBot(TOKEN)
    my_id = 536148350
    to_buy = []
    groceires_type = ["Пластиковая продукция", "Приправы", "Мясные продукты", 'Овощи и фрукты' , "Молочные продукты", "Чипсы и прочее", "Сладкое", "Бумажная продукция", "Яйца", "Алкоголь и остальная вода"]
    plastic = ['Пластиковые стаканчики', 'Пластиковые тарелки', 'Пластиковые столовые приборы', 'Мусорные пакеты']
    spices = ['Кетчуп', 'Горчица', 'Соус']
    milk = ['Молоко', 'Кефир', 'Йогурт', 'Сметана', 'Творог', 'Сыр', "Сливки"]
    snacks = ['Чипсы', 'Сухарики', 'Орешки']
    paper = ['Туалетная бумага', 'Салфетки', 'Бумажные полотенца']
    alco_water = ['Вода питьевая', 'Пиво', 'Сидр', 'Вино', 'Шампанское', 'Водка', 'Коньяк', "Пепси-кола", "Кока-кола", "Фанта", "Спрайт", "Яблочный сок", "Апельсиновый сок", 'Гранатовый сок', "Вишневый сок"]
    vegetables__fruits = ['Бананы', "Яблоки", "Мандарины", "Апельсины", "Груши", "Манго", "Киви", "Лимоны", "Помидоры", "Огурцы", "Лук", "Грибы"]
    sweet = ['Печенье', 'Конфеты', 'Шоколадки', 'Торт', 'Выпечка']
    meat = ['Сосиски', 'Филе', 'Крылья', 'Бедра', 'Ножки', 'Печенка куриная', "Колбаса", "Бекон"]


    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.send_message(message.chat.id, 'Бот создан для автоматизации покупок продуктов домой. Тоесть можно не звонить, не писать и тд, главное при себе иметь интернет :) . Сообщения со списком будут приходить мне автоматически. Для более детальной информации напишите /help')

    @bot.message_handler(commands=['help'])
    def send_help(message):
        bot.send_message(message.chat.id, 'Как было уже сказано - бот создан для удобства, чтобы никого не отвлекать. Для тех кто редко пользуется телеграммом или вовсе не знаком с ним: \
все команды начинаются с символа слеш (/). Для удобства выведу список команд которые есть на данном этапе:\n\n\
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

        markup_menu = types.InlineKeyboardMarkup(row_width=2).add(plastic_produtcts_btn)
        markup_menu.add(spices_products_btn, meat_products_btn)
        markup_menu.add(veg_fruits_products_btn, milk_products_btn)
        markup_menu.add(snack_products_btn, sweet_products_btn)
        markup_menu.add(paper_products_btn, eggs_btn, alco_water_products_btn)
        bot.send_message(message.chat.id, text='Выберете категерию продуктов', reply_markup=markup_menu)

    # @bot.message_handler(commands=['buy'])
    # def start_shopping(message):
    #     kb_porducts = Keyboa(items=)
    #     bot.send_message(message.chat.id, text = 'Выберете категорию продкутов', reply_markup=kb_porducts.keyboard)

    @bot.callback_query_handler(func=lambda call: True)
    def show_product_category(call):

        # Making keyboard for vegetables and fruits
        menu = types.InlineKeyboardMarkup()
        plastic_btn = types.InlineKeyboardButton(groceires_type[0], callback_data = 'plastic')
        spices_btn = types.InlineKeyboardButton(groceires_type[1], callback_data = 'spices')
        meat_btn = types.InlineKeyboardButton(groceires_type[2], callback_data = 'meat')
        veg_btn = types.InlineKeyboardButton(groceires_type[3], callback_data = 'vf')
        milk_btn = types.InlineKeyboardButton(groceires_type[4], callback_data = 'milk')
        snack_btn = types.InlineKeyboardButton(groceires_type[5], callback_data = 'snack')
        sweet_btn = types.InlineKeyboardButton(groceires_type[6], callback_data = 'sweet')
        paper_btn = types.InlineKeyboardButton(groceires_type[7], callback_data = 'paper')
        eggs_btn = types.InlineKeyboardButton(groceires_type[8], callback_data = 'eggs')
        water_btn = types.InlineKeyboardButton(groceires_type[9], callback_data = 'water')
        menu.add(plastic_btn)
        menu.add(spices_btn)
        menu.add(meat_btn)
        menu.add(veg_btn)
        menu.add(milk_btn)
        menu.add(snack_btn)
        menu.add(sweet_btn)
        menu.add(paper_btn)
        menu.add(eggs_btn)
        menu.add(water_btn)

        back_btn = types.InlineKeyboardButton('Вернуться назад', callback_data = 'back')

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
        markup_veg.add(back_btn)
        #-----------------------------------------------

        # Making keyboard for smth sweet
        markup_sweet = types.InlineKeyboardMarkup()

        cookie_btn = types.InlineKeyboardButton(sweet[0], callback_data=23)
        candy_btn = types.InlineKeyboardButton(sweet[1], callback_data=24)
        candy_btn = types.InlineKeyboardButton(sweet[1], callback_data=24)

        chocolate_btn = types.InlineKeyboardButton(sweet[2], callback_data=25)
        cake_btn = types.InlineKeyboardButton(sweet[3], callback_data=26)
        bakery_btn = types.InlineKeyboardButton(sweet[4], callback_data=27)

        markup_sweet.add(cookie_btn)
        markup_sweet.add(candy_btn)
        markup_sweet.add(chocolate_btn)
        markup_sweet.add(cake_btn)
        markup_sweet.add(bakery_btn)
        markup_sweet.add(back_btn)
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
        markup_meat.add(back_btn)
        #-------------------------------------------------------------

        # Making kyeboard for plastic products
        markup_plastic = types.InlineKeyboardMarkup()
        plastic_cup_btn = types.InlineKeyboardButton(plastic[0], callback_data = 36)
        plastic_plate_btn = types.InlineKeyboardButton(plastic[1], callback_data = 37)
        plastic_fork_spoon_btn = types.InlineKeyboardButton(plastic[2], callback_data = 38)
        plastic_garbage_btn = types.InlineKeyboardButton(plastic[3], callback_data = 39)
        markup_plastic.add(plastic_cup_btn)
        markup_plastic.add(plastic_plate_btn)
        markup_plastic.add(plastic_fork_spoon_btn)
        markup_plastic.add(plastic_garbage_btn)
        markup_plastic.add(back_btn)
        #------------------------------------------------------------

        # Making keyboard for milk products
        markup_milk = types.InlineKeyboardMarkup()
        milk_btn = types.InlineKeyboardButton(milk[0], callback_data = 40)
        kefir_btn = types.InlineKeyboardButton(milk[1], callback_data = 41)
        jogurt_btn = types.InlineKeyboardButton(milk[2], callback_data = 42)
        smetana_btn = types.InlineKeyboardButton(milk[3], callback_data = 43)
        tvorog_btn = types.InlineKeyboardButton(milk[4], callback_data = 44)
        vorog_btn = types.InlineKeyboardButton(milk[4], callback_data = 44)
        cheese_btn = types.InlineKeyboardButton(milk[5], callback_data = 45)
        cream_btn = types.InlineKeyboardButton(milk[6], callback_data = 46)
        markup_milk.add(milk_btn, kefir_btn)
        markup_milk.add(jogurt_btn, smetana_btn)
        markup_milk.add(tvorog_btn, cheese_btn, cream_btn)
        markup_milk.add(back_btn)
        #-----------------------------------------------------------

        # Making keyboard for spices
        markup_spices = types.InlineKeyboardMarkup()
        ketchup_btn = types.InlineKeyboardButton(spices[0], callback_data = 48)
        gorchiza_btn = types.InlineKeyboardButton(spices[1], callback_data = 49)
        sause_btn = types.InlineKeyboardButton(spices[2], callback_data = 50)
        markup_spices.add(ketchup_btn)
        markup_spices.add(gorchiza_btn)
        markup_spices.add(sause_btn)
        markup_spices.add(back_btn)
        #-----------------------------------------------------------

        # Making keyboard for snacks
        markup_snacks = types.InlineKeyboardMarkup()
        cheeps_btn = types.InlineKeyboardButton(snacks[0], callback_data = 51)
        syhari_btn = types.InlineKeyboardButton(snacks[1], callback_data = 52)
        nuts_btn = types.InlineKeyboardButton(snacks[2], callback_data = 53)
        markup_snacks.add(cheeps_btn)
        markup_snacks.add(syhari_btn)
        markup_snacks.add(nuts_btn)
        markup_snacks.add(back_btn)
        #-----------------------------------------------------------

        # Making keyboard for paper progucts
        markup_paper = types.InlineKeyboardMarkup()
        toailet_paper_btn = types.InlineKeyboardButton(paper[0], callback_data = 54)
        salfetki_btn = types.InlineKeyboardButton(paper[1], callback_data = 55)
        bym_polotenca_btn = types.InlineKeyboardButton(paper[2], callback_data = 56)
        markup_paper.add(toailet_paper_btn)
        markup_paper.add(salfetki_btn)
        markup_paper.add(bym_polotenca_btn)
        markup_paper.add(back_btn)
        #-----------------------------------------------------------

        # Making keyboard for alco and other water
        markup_water = types.InlineKeyboardMarkup()
        water_btn = types.InlineKeyboardButton(alco_water[0], callback_data = 57)
        beer_btn = types.InlineKeyboardButton(alco_water[1], callback_data = 58)
        sidr_btn = types.InlineKeyboardButton(alco_water[2], callback_data = 59)
        vine_btn = types.InlineKeyboardButton(alco_water[3], callback_data = 60)
        shamp_btn = types.InlineKeyboardButton(alco_water[4], callback_data = 61)
        vodka_btn = types.InlineKeyboardButton(alco_water[5], callback_data = 62)
        konjak_btn = types.InlineKeyboardButton(alco_water[6], callback_data = 63)
        pepsi_btn = types.InlineKeyboardButton(alco_water[7], callback_data = 64)
        coca_btn = types.InlineKeyboardButton(alco_water[8], callback_data = 65)
        fanta_btn = types.InlineKeyboardButton(alco_water[9], callback_data = 66)
        sprite_btn = types.InlineKeyboardButton(alco_water[10], callback_data = 67)
        apple_juice_btn = types.InlineKeyboardButton(alco_water[11], callback_data = 68)
        orange_juice_btn = types.InlineKeyboardButton(alco_water[12], callback_data = 69)
        granat_juice_btn = types.InlineKeyboardButton(alco_water[13], callback_data = 70)
        cherry_juice_btn = types.InlineKeyboardButton(alco_water[14], callback_data = 71)
        markup_water.add(water_btn, beer_btn)
        markup_water.add(beer_btn, sidr_btn)
        markup_water.add(vine_btn, shamp_btn)
        markup_water.add(vodka_btn, konjak_btn)
        markup_water.add(pepsi_btn, coca_btn)
        markup_water.add(fanta_btn, sprite_btn)
        markup_water.add(apple_juice_btn, orange_juice_btn)
        markup_water.add(granat_juice_btn, cherry_juice_btn)
        markup_water.add(back_btn)
        #-----------------------------------------------------------

        bot.answer_callback_query(callback_query_id=call.id, text = '')
        if call.data == '1':
            bot.send_message(call.message.chat.id, reply_markup = markup_plastic, text = 'Выберете что-то из пластиковой продукции')
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        elif call.data == '2':
            bot.send_message(call.message.chat.id, reply_markup = markup_spices, text = 'Выберете добавки')
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        elif call.data == '3':
            bot.send_message(call.message.chat.id, reply_markup=markup_meat, text='Выберете что-то из мясных продуктов')
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        elif call.data == '4':
            bot.send_message(call.message.chat.id, reply_markup=markup_veg, text='Выберете что-то из офощей или фруктов')
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        elif call.data == '5':
            bot.send_message(call.message.chat.id, reply_markup = markup_milk, text = 'Выбере что-то из молочной продукции')
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        elif call.data == '6':
            bot.send_message(call.message.chat.id, reply_markup = markup_snacks, text = 'Выберете что-то из снеков')
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        elif call.data == '7':
            bot.send_message(call.message.chat.id, reply_markup=markup_sweet, text='Выберете что-то из сладкого')
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        elif call.data == '8':
            bot.send_message(call.message.chat.id, reply_markup = markup_paper, text = 'Выбере что-то из бумажной продукции')
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        elif call.data == '9':
            to_buy.append(groceires_type[-2])
        elif call.data == '10':
            bot.send_message(call.message.chat.id, reply_markup = markup_water, text = 'Выберете что-то из напитков')
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        elif call.data == 'eggs':
            to_buy.append(groceires_type[-2])
        elif call.data == 'back':
            bot.send_message(call.message.chat.id, reply_markup = menu, text = 'Вы вернулись в меню покупок')
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        elif call.data == 'plastic':
            bot.send_message(call.message.chat.id, reply_markup = markup_plastic, text = 'Выберете что-то из пластиковой продукции')
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        elif call.data == 'spices':
            bot.send_message(call.message.chat.id, reply_markup = markup_spices, text = 'Выберете добавки')
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        elif call.data == 'meat':
            bot.send_message(call.message.chat.id, reply_markup = markup_meat, text = 'Выберете что-то из мясных продуктов')
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        elif call.data == 'vf':
            bot.send_message(call.message.chat.id, reply_markup = markup_veg, text = 'Выбере что-то из овощей или фркутов')
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        elif call.data == 'milk':
            bot.send_message(call.message.chat.id, reply_markup = markup_milk, text = 'Выберете что-то из молочной продукции')
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        elif call.data == 'snack':
            bot.send_message(call.message.chat.id, reply_markup = markup_snacks, text = 'Выберете что-то из снеков')
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        elif call.data == 'sweet':
            bot.send_message(call.message.chat.id, reply_markup = markup_sweet, text = 'Выберете что-то из сладкого')
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        elif call.data == 'paper':
            bot.send_message(call.message.chat.id, reply_markup = markup_paper, text = 'Выберете что-то из бумажной продукции')
        elif call.data == 'water':
            bot.send_message(call.message.chat.id, reply_markup = markup_water, text = 'Выберете что-то из напитков')
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    bot.polling()

if __name__ == '__main__':
    main()
		
		