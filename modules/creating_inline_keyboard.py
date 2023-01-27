import telebot 
import modules.creating_inline_buttons as m_inline_bt

inline_keyboard1 = telebot.types.InlineKeyboardMarkup(row_width= 2)
inline_keyboard2 = telebot.types.InlineKeyboardMarkup(row_width= 2)
inline_keyboard3 = telebot.types.InlineKeyboardMarkup(row_width= 2)
inline_keyboard4 = telebot.types.InlineKeyboardMarkup(row_width= 2)
inline_keyboard5 = telebot.types.InlineKeyboardMarkup(row_width= 2)

inline_keyboard1.add(m_inline_bt.inline_bt1, m_inline_bt.inline_bt2)
inline_keyboard2.add(m_inline_bt.inline_bt1, m_inline_bt.inline_bt3)
inline_keyboard3.add(m_inline_bt.inline_bt1, m_inline_bt.inline_bt4)
inline_keyboard4.add(m_inline_bt.inline_bt1, m_inline_bt.inline_bt5)
inline_keyboard5.add(m_inline_bt.inline_bt1, m_inline_bt.inline_bt6)
