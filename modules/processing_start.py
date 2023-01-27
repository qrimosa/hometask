import modules.creating_bot as m_bot
import modules.creating_keyboard as m_keyboard
import modules.sending_messages_to_user as m_message_user

@m_bot.bot.message_handler(commands = ["start"])
def bot_start(message):
    m_bot.bot.send_message(
        message.chat.id, 
        "Hi User!",
        reply_markup=m_keyboard.keyboard
    )
    m_bot.bot.register_next_step_handler(message, m_message_user.send_message_user)