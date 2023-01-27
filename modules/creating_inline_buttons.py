import telebot 

button_list = ["inline_bt2", "inline_bt3", "inline_bt4", "inline_bt5", "inline_bt6"]
url_list = ["https://yabloki.ua/ukr/iphone-14-starlight-128gb.html",
            "https://yabloki.ua/ukr/iphone-14-pro-deep-purple-128gb.html",
            "https://yabloki.ua/ukr/ipad-pro-11-m2-2022-wi-fi-lte-128gb-space-gray-mnyc3.html",
            "https://yabloki.ua/ukr/apple-watch-series-8-edition-41-mm-starlight.html",
            "https://yabloki.ua/ukr/apple-airpods-v-zarjadnom-futljare-2019-mv7n2.html"]
inline_bt1 = telebot.types.InlineKeyboardButton(text= "Замовити", callback_data = "замовити")

for a in range(5):
    button_list[a] = telebot.types.InlineKeyboardButton("Перейти до сайту", url_list[a])
