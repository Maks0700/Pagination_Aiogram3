#Welcome to aiogram 3.10 YEEEEEEEEEEEEEEAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHH
import asyncio
from aiogram import Bot,Dispatcher,F #Magic F (filter) for simply checking text
from aiogram.types import Message,CallbackQuery
from dotenv import load_dotenv
import os
from pprint import pprint
from aiogram.filters import Command,CommandObject,CommandStart
from random import randint
from aiogram.enums.dice_emoji import DiceEmoji #emoji
from KEYBOARDS import main_kb,links_keyboard,special_buttons,button_calculator,paginator,Pagination
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest 
from aiogram.enums import ContentType


load_dotenv(".env")

smiles=[
    ["🥑","AVOCADO"],
    ["🍓","VERY TASTE"],
    ["😍","CUDDLE?"],
    ["💃","ARE U DANCING"]
]


bot=Bot(os.getenv("api"),parse_mode="Markdown")
dp=Dispatcher()




    


@dp.message(CommandStart())
async def greeting(message:Message):
    await message.answer(f"Welcome to my bot, dear {message.from_user.first_name}",reply_markup=main_kb())

@dp.callback_query(Pagination.filter(F.action.in_(["prev","next"])))
async def process(call:CallbackQuery,callback_data:Pagination):
    page_num=int(callback_data.page)
    page_main=page_num-1 if page_num>0 else 0
    if callback_data.action=="next":
        
        page_main=page_num+1 if page_num<(len(smiles)-1) else page_num
    with suppress(TelegramBadRequest):
        await call.message.edit_text(f"{smiles[page_main][0]} {smiles[page_main][1]}",reply_markup=paginator(page=page_main))    
    await call.answer("All good, don't worry!!")
@dp.message(F.text.in_(["Links"]))
async def button_links(message:Message):
    await message.answer("Your Links",reply_markup=links_keyboard())


@dp.message(F.text.in_(["Calculator"]))
async def buttons_calc(message:Message):
    await message.answer("Your Calculator",reply_markup=button_calculator())

@dp.message(F.text.in_(["Special buttons"]))
async def special_buttons(message:Message):
    await message.answer("Your Spcecial buttons",reply_markup=special_buttons())


@dp.message(F.text.in_(["Smiles"]))
async def smiles_button(message:Message):
    await message.answer(f"{smiles[0][0]} {smiles[0][1]}",reply_markup=paginator(page=0))

async def main():
    try:
        await bot.delete_webhook(drop_pending_updates=True)# for skip all update
        pprint("Bot is success!!")
        await dp.start_polling(bot)
    except Exception:
        return -1


    
    

if __name__=="__main__":
    asyncio.run(main())