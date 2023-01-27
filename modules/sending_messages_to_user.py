import modules.creating_bot as m_bot
import modules.creating_inline_keyboard as m_inline_keyboard

tech_name_list = ["Iphone 14 Starlight", "Iphone 14 Pro Deep Purple", "Ipad Pro 11 M2 Space Gray", "Apple Watch Series 8 Starlight", "Apple Airpods"]
picture_links = ["https://yabloki.ua/media/cache/app_product_page_small_slider_image/35/c4/82d0d5f440af49debf9eac7eb15b.png.webp",
                "https://yabloki.ua/media/cache/app_product_page_small_slider_image/53/f0/f1c56a97d1be1a3886e66ed8aa59.png.webp",
                "https://yabloki.ua/media/cache/app_product_page_small_slider_image/70/a6/72b74cc42cdd25320cd1731da81b.png.webp",
                "https://yabloki.ua/media/cache/app_product_page_small_slider_image/de/78/9da2c95977c9d41714b2efef7159.png.webp",
                "https://yabloki.ua/media/cache/app_product_page_small_slider_image/4f/5f/6f505f555513db8e18785db1e309.png.webp"]

def send_message_user(message):
    if message.text.lower() == "get picture":
        for i in range(5):
            m_bot.bot.send_photo(
                message.chat.id,
                picture_links[i],
                tech_name_list[i],
                reply_markup= m_inline_keyboard.inline_keyboard
            )