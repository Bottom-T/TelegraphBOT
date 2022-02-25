from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


# Help Message
@Client.on_message(filters.private & filters.incoming & filters.command("id"))
async def _help(bot, msg):
    await bot.send_message(
        msg.chat.id,
        Data.HELP,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons),
        reply_to_message_id=msg.message_id
    )
