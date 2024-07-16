from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [[InlineKeyboardButton("🍡 C͒H͒A͒T͒-G͒P͒T͒🍡", callback_data="mplus HELP_ChatGPT"),InlineKeyboardButton("▫️ G͒R͒O͒U͒P͒S͒ ▫️", callback_data="mplus HELP_Group"),InlineKeyboardButton("🦯 S͒T͒I͒C͒K͒E͒R͒ 🦯", callback_data="mplus HELP_Sticker")],
    [InlineKeyboardButton("🏷️ T͒A͒G͒-A͒L͒L͒ 🏷️", callback_data="mplus HELP_TagAll"),
    InlineKeyboardButton("🎋 I͒N͒F͒O͒ 🎋", callback_data="mplus HELP_Info"),InlineKeyboardButton("🧨 E͒X͒T͒R͒A͒ 🧨", callback_data="mplus HELP_Extra")],
    [InlineKeyboardButton("🌾 I͒M͒A͒G͒E͒ 🌾", callback_data="mplus HELP_Image"),
    InlineKeyboardButton("🕸️ A͒C͒T͒I͒O͒N͒ 🕸️", callback_data="mplus HELP_Action"),InlineKeyboardButton("🔍 S͒E͒A͒R͒C͒H͒ 🔎", callback_data="mplus HELP_Search")],    
    [InlineKeyboardButton("🍭 F͒O͒N͒T͒ 🍭", callback_data="mplus HELP_Font"),
    InlineKeyboardButton("🍹 G͒A͒M͒E͒S͒ 🍹", callback_data="mplus HELP_Game"),InlineKeyboardButton("🏮 T͒-G͒R͒A͒P͒H͒ 🏮", callback_data="mplus HELP_TG")],
    [InlineKeyboardButton("🏓 I͒M͒P͒O͒S͒T͒E͒R͒ 🏓", callback_data="mplus HELP_Imposter"),
    InlineKeyboardButton("🗻 T͒R͒U͒T͒H͒-D͒A͒R͒E͒ 🗻", callback_data="mplus HELP_TD"),InlineKeyboardButton("📍 H͒A͒S͒H͒T͒A͒G͒ 📍", callback_data="mplus HELP_HT")], 
    [InlineKeyboardButton("🛸 T͒T͒S͒ 🛸", callback_data="mplus HELP_TTS"),
    InlineKeyboardButton("🎐 F͒U͒N͒ 🎐", callback_data="mplus HELP_Fun"),InlineKeyboardButton("🩹 Q͒U͒I͒L͒Y͒ 🩹", callback_data="mplus HELP_Q")],          
    [InlineKeyboardButton("<🔪", callback_data=f"settings_back_helper"), 
    InlineKeyboardButton("🔪>", callback_data=f"managebot123 settings_back_helper"),
    ]]