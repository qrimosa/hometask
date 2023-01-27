import modules.creating_buttons as m_buttons
import telebot

keyboard = telebot.types.ReplyKeyboardMarkup()
keyboard.add(m_buttons.button, m_buttons.button2, m_buttons.button3)