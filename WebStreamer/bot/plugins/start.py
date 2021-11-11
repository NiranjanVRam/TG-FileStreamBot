# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]
# Editz : Niranjan V Ram [@NiranjanVRam]

from pyrogram import filters, emoji
from WebStreamer.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

buttons = [[
            InlineKeyboardButton('🎬 JOIN FOR MOVIES 🎬', url='https://t.me/fhmoviechat')
            ],[
            InlineKeyboardButton('📺 SERIES', url='https://t.me/fhserieschat'),
            InlineKeyboardButton('🎶 MUSICS', url='https://t.me/fhmusics')
            ],[
            InlineKeyboardButton('❤️JOIN CHANNEL❤️', url='https://t.me/fileshomeofficial')
        ]]

#nvrcustom1=''

@StreamBot.on_message(filters.command(['start', 'help']))
async def start(_, m: Message):
    await m.reply_video(video='https://telegra.ph/file/0aafae80b932b721a9b9b.mp4', caption=f'Hey {m.from_user.mention(style="md")}, Send me a file to get an instant stream link.\n\n<b>©️ Powered By @fhmoviechat</b>',
                  reply_markup=InlineKeyboardMarkup(buttons))
