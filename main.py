import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode, ContentType
from aiogram.filters import CommandStart

from aiogram.types import CallbackQuery, Message
from dotenv import load_dotenv

from keyboards import kb1, kb2, kb3, kb4, kb5, kb6, pages

load_dotenv()
TOKEN = os.getenv('TOKEN')

dp = Dispatcher()


@dp.message(CommandStart())
async def welcome_message(message: Message, bot: Bot):
    user_id = message.from_user.id
    text = "Free audios to listen and download 😊\n\nChoose Surah ✅"
    await bot.send_message(user_id, text, reply_markup=kb1)


@dp.message(F.content_type == [ContentType.PHOTO, ContentType.VIDEO, ContentType.TEXT,
                               ContentType.DOCUMENT, ContentType.STICKER,
                               ContentType.AUDIO, ContentType.VIDEO_NOTE])
async def send_quran(message: Message, bot: Bot):
    user_id = message.from_user.id
    await bot.send_message(user_id, "Assalamu Aleykum")


@dp.callback_query(lambda c: c.data)
async def handle_callback_query(call: CallbackQuery, bot: Bot):
    data = call.data
    if data == "pg1":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=kb1)
    elif data == "pg2":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=kb2)
    elif data == "pg3":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=kb3)
    elif data == "pg4":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=kb4)
    elif data == "pg5":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=kb5)
    elif data == "pg6":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=kb6)
    elif data == "fa":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/4", reply_markup=pages)
    elif data == "ba":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/5", reply_markup=pages)
    elif data == "im":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/6", reply_markup=pages)
    elif data == "ni":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/7", reply_markup=pages)
    elif data == "ma":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/8", reply_markup=pages)
    elif data == "ana":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/9", reply_markup=pages)
    elif data == "ara":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/10", reply_markup=pages)
    elif data == "anf":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/11", reply_markup=pages)
    elif data == "ta":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/12", reply_markup=pages)
    elif data == "yun":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/13", reply_markup=pages)
    elif data == "hu":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/14", reply_markup=pages)
    elif data == "yu":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/15", reply_markup=pages)
    elif data == "rad":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/16", reply_markup=pages)
    elif data == "ib":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/17", reply_markup=pages)
    elif data == "hi":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/18", reply_markup=pages)
    elif data == "nah":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/19", reply_markup=pages)
    elif data == "is":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/20", reply_markup=pages)
    elif data == "kaf":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/21", reply_markup=pages)
    elif data == "mar":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/22", reply_markup=pages)
    elif data == "taha":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/23", reply_markup=pages)
    elif data == "nex1":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=kb2)

    elif data == "anb":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/24", reply_markup=pages)
    elif data == "haj":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/25", reply_markup=pages)
    elif data == "mum":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/26", reply_markup=pages)
    elif data == "nur":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/27", reply_markup=pages)
    elif data == "fur":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/28", reply_markup=pages)
    elif data == "shu":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/29", reply_markup=pages)
    elif data == "nam":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/30", reply_markup=pages)
    elif data == "qa":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/31", reply_markup=pages)
    elif data == "ank":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/32", reply_markup=pages)
    elif data == "rum":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/33", reply_markup=pages)
    elif data == "luq":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/34", reply_markup=pages)
    elif data == "saj":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/35", reply_markup=pages)
    elif data == "ah":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/36", reply_markup=pages)
    elif data == "saba":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/37", reply_markup=pages)
    elif data == "fat":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/38", reply_markup=pages)
    elif data == "yas":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/39", reply_markup=pages)
    elif data == "saff":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/40", reply_markup=pages)
    elif data == "sad":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/41", reply_markup=pages)
    elif data == "zum":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/42", reply_markup=pages)
    elif data == "gaf":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/43", reply_markup=pages)
    elif data == "bk1":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=kb1)
    elif data == "nex2":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=kb3)

    elif data == "fus":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/44", reply_markup=pages)
    elif data == "shur":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/45", reply_markup=pages)
    elif data == "zuk":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/46", reply_markup=pages)
    elif data == "duk":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/47", reply_markup=pages)
    elif data == "jat":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/48", reply_markup=pages)
    elif data == "ahq":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/49", reply_markup=pages)
    elif data == "muh":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/50", reply_markup=pages)
    elif data == "fath":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/51", reply_markup=pages)
    elif data == "huj":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/52", reply_markup=pages)
    elif data == "qaf":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/53", reply_markup=pages)
    elif data == "zar":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/54", reply_markup=pages)
    elif data == "tur":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/55", reply_markup=pages)
    elif data == "naj":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/56", reply_markup=pages)
    elif data == "qam":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/57", reply_markup=pages)
    elif data == "rah":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/58", reply_markup=pages)
    elif data == "waq":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/59", reply_markup=pages)
    elif data == "had":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/60", reply_markup=pages)
    elif data == "muj":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/61", reply_markup=pages)
    elif data == "hash":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/62", reply_markup=pages)
    elif data == "mumt":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/63", reply_markup=pages)
    elif data == "bk2":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=kb2)
    elif data == "nex3":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=kb4)

    elif data == "saf":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/64", reply_markup=pages)
    elif data == "juma":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/65", reply_markup=pages)
    elif data == "muna":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/66", reply_markup=pages)
    elif data == "taga":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/67", reply_markup=pages)
    elif data == "taha":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/68", reply_markup=pages)
    elif data == "tahr":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/69", reply_markup=pages)
    elif data == "mul":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/70", reply_markup=pages)
    elif data == "qal":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/71", reply_markup=pages)
    elif data == "haq":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/72", reply_markup=pages)
    elif data == "maar":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/73", reply_markup=pages)
    elif data == "nuh":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/74", reply_markup=pages)
    elif data == "jin":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/75", reply_markup=pages)
    elif data == "muzam":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/76", reply_markup=pages)
    elif data == "muda":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/77", reply_markup=pages)
    elif data == "qi":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/78", reply_markup=pages)
    elif data == "ins":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/79", reply_markup=pages)
    elif data == "murs":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/80", reply_markup=pages)
    elif data == "nab":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/81", reply_markup=pages)
    elif data == "nazi":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/82", reply_markup=pages)
    elif data == "aba":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/83", reply_markup=pages)
    elif data == "bk3":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=kb3)
    elif data == "nex4":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=kb5)

    elif data == "tawk":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/84", reply_markup=pages)
    elif data == "inf":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/85", reply_markup=pages)
    elif data == "muta":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/86", reply_markup=pages)
    elif data == "inshi":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/87", reply_markup=pages)
    elif data == "bur":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/88", reply_markup=pages)
    elif data == "tari":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/89", reply_markup=pages)
    if data == "ala":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/90", reply_markup=pages)
    elif data == "gash":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/91", reply_markup=pages)
    elif data == "faj":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/92", reply_markup=pages)
    elif data == "bala":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/93", reply_markup=pages)
    elif data == "sham":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/94", reply_markup=pages)
    elif data == "layl":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/95", reply_markup=pages)
    elif data == "duha":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/96", reply_markup=pages)
    elif data == "inshir":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/97", reply_markup=kb5)
    elif data == "tin":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/98", reply_markup=pages)
    elif data == "alaq":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/99", reply_markup=pages)
    elif data == "qad":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/100", reply_markup=pages)
    elif data == "bayi":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/101", reply_markup=pages)
    elif data == "zal":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/102", reply_markup=pages)
    elif data == "adi":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/103", reply_markup=pages)
    elif data == "bk4":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=kb4)
    elif data == "nex5":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=kb6)

    elif data == "qari":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/104", reply_markup=pages)
    elif data == "taka":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/105", reply_markup=pages)
    elif data == "asr":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/106", reply_markup=pages)
    elif data == "huma":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/107", reply_markup=pages)
    elif data == "fil":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/108", reply_markup=pages)
    elif data == "qur":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/109", reply_markup=pages)
    elif data == "mau":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/110", reply_markup=pages)
    elif data == "kau":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/111", reply_markup=pages)
    elif data == "kafi":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/112", reply_markup=pages)
    elif data == "nasr":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/113", reply_markup=pages)
    elif data == "masad":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/114", reply_markup=pages)
    elif data == "ik":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/115", reply_markup=pages)
    elif data == "fala":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/116", reply_markup=pages)
    elif data == "nas":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_audio(chat_id=call.message.chat.id, audio="https://t.me/QarimSiddiq/117", reply_markup=pages)
    elif data == "p1":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=kb1)
    elif data == "p2":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=kb2)
    elif data == "p3":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=kb3)
    elif data == "p4":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=kb4)
    elif data == "bk5":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=kb5)
    elif data == "main_menu":
        await bot.send_message(call.message.chat.id, 'Welcome to the Main Menu 🫡', reply_markup=kb1)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    asyncio.run(main())
