from aiogram.types import(
    ReplyKeyboardMarkup,KeyboardButton,
    InlineKeyboardMarkup,InlineKeyboardButton,
    KeyboardButtonPollType # This is class for poll user
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


class Pagination(CallbackData,prefix="page"):
    page:int
    action:str

    

def paginator(page:int=0):
        builder=InlineKeyboardBuilder()
        builder.row(
        InlineKeyboardButton(text="⬅️",callback_data=Pagination(page=page,action="prev").pack()),
        InlineKeyboardButton(text="➡️",callback_data=Pagination(page=page,action="next").pack()),
        width=2
        )
        return builder.as_markup()
    




def main_kb()->ReplyKeyboardMarkup:
    keyboard=ReplyKeyboardMarkup(
        keyboard=[
            [
            KeyboardButton(text="Smiles"),
            KeyboardButton(text="Links")
        ],
            [
                KeyboardButton(text="Special Buttons"),
                KeyboardButton(text="Calculator")
            ]
                  ],
        resize_keyboard=True,
        input_field_placeholder="Enter message",
        selective=True,
        one_time_keyboard=True
    
    )
    return keyboard
def links_keyboard()->InlineKeyboardMarkup:
    keyboard_links=InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="YouTube",url="https://www.youtube.com")
                
            ],
            [
                InlineKeyboardButton(text="Vkontakte",url="https://vk.com/feed")
            ]
            
            ]
        )
    return keyboard_links
def special_buttons()->ReplyKeyboardMarkup:
    keyboard_special_buttons=ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="My location",request_location=True)
            ],
            [
                KeyboardButton(text="My contact",request_contact=True)
                
                ],
            [
                KeyboardButton(text="Poll",request_poll=KeyboardButtonPollType())
            ]
        ],
        selective=True,
        one_time_keyboard=True,
        resize_keyboard=True
    )
    return keyboard_special_buttons
def button_calculator()->ReplyKeyboardBuilder:
    builder=ReplyKeyboardBuilder()
    items=[
        "1","2","3","/",
        "4","5","6","*",
        "7","8","9","-",
        "0",".","=","+",

    ]    
    [builder.button(text=item) for item in items]
    
    builder.adjust(*[4]*4)
    return builder.as_markup()
