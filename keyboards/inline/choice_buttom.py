from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

choice = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [

                                      InlineKeyboardButton(
                                          text="Добавить группу",
                                          callback_data="add_new_group"

                                      ),

                                      InlineKeyboardButton(
                                          text="Удалить группу",
                                          callback_data="buy:apple:5"

                                      )

                                  ],
                                  [

                                      InlineKeyboardButton(
                                          text="Редактировать группу ",
                                          callback_data="cancel"
                                      )

                                  ],
                                  [

                                      InlineKeyboardButton(
                                          text="Добавить канал",
                                          callback_data="add_channel"
                                      )

                                  ]
                              ])
pear_keyboard = InlineKeyboardMarkup()

PEAR_LINK = "https://www.sportmaster.ru/product/1259400/?PRODUCT_ID=1259401&nomobile=1&gclid=CjwKCAjw_Y_8BRBiEiwA5MCBJqYSqEZPNvFmOGQIu9durNrFsh-2_fAEcZ25StS1zVAUOdqp9vOXhxoCohEQAvD_BwE"
APPLE_LINK = "https://www.apple.com/ru/"

pear_link = InlineKeyboardButton(text="Купить тут", url=PEAR_LINK)

pear_keyboard.insert(pear_link)

apple_keyboard = InlineKeyboardMarkup()

apple_link = InlineKeyboardButton(text="Купить тут", url=APPLE_LINK)
back = InlineKeyboardButton(text="Назад", callback_data="back")

apple_keyboard.insert(apple_link)
apple_keyboard.insert(back)
pear_keyboard.insert(back)
