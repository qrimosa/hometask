import modules.creating_bot as m_bot

@m_bot.bot.callback_query_handler(func= lambda callback: callback.data)

def request_processing(callback):
    if callback.data == "замовити":
        m_bot.bot.send_message(callback.message.chat.id, "Замовлення прийнято до обробки.\nОчікуйте на зворотній зв'язок.")