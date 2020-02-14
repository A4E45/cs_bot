from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import datetime
import time

date = str(time.strftime("%d-%m-%Y"))
updater = Updater(token="<Token>")
dispatcher = updater.dispatcher

# main function


def start(bot, update):
    button = [
        [InlineKeyboardButton("تحليل حقيقي", callback_data="1")],
        [InlineKeyboardButton("جبر خطي (1)", callback_data="2")],
        [InlineKeyboardButton("هندسة تحليلية فراغية", callback_data="3")],
        [InlineKeyboardButton("ميكانيكا 4", callback_data="4")],
        [InlineKeyboardButton("مقدمة في الاحصاء و الاحتمالات", callback_data="5")],
        [InlineKeyboardButton("رياضيات حيوية", callback_data="6")],
    ]
    reply_markup = InlineKeyboardMarkup(button)

    bot.send_message(chat_id=update.message.chat_id,
                     text="""
                    تم اضافة:
                     - محاضرة (1) تحليل حقيقي
                     - محاضر (1) رياضة حيوي
                     - كتاب التحليل الحقيقي
                     - كتاب الجبر الخطي
                     """,
                     reply_markup=reply_markup)

start_handler = CommandHandler("start", start)
help_handler = CommandHandler("help", start)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)

# buttons control function


def buttons(bot, update):
    query = update.callback_query
    # Real Analysis
    if query.data == "1":
        buttons = [
        [InlineKeyboardButton("محاضرات", callback_data="Real_Analysis_L")],
        [InlineKeyboardButton("سكاشن", callback_data="Real_Analysis_S")],
        [InlineKeyboardButton("كتاب التحليل الحقيقي", url="")],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        bot.send_message(chat_id=query.message.chat_id, text="تحليل حقيقي", reply_markup=reply_markup)

    if query.data == "Real_Analysis":
        buttons = [
        [InlineKeyboardButton("محاضرات", callback_data="Real_Analysis_L")],
        [InlineKeyboardButton("سكاشن", callback_data="Real_Analysis_S")],
        [InlineKeyboardButton("كتاب التحليل الحقيقي", url="")],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        bot.edit_message_text(chat_id=query.message.chat_id, text="تحليل حقيقي", message_id=query.message.message_id, reply_markup=reply_markup)

    if query.data == "Real_Analysis_L":
        buttons = [
                [InlineKeyboardButton("محاضرة 1", url="")],
                [InlineKeyboardButton("محاضرة 2", url="")],
                [InlineKeyboardButton("محاضرة 3", url="")],
                [InlineKeyboardButton("محاضرة 4", url="")],
                [InlineKeyboardButton("محاضرة 5", url="")],
                [InlineKeyboardButton("محاضرة 6", url="")],
                [InlineKeyboardButton("رجوع", callback_data="Real_Analysis")],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        bot.edit_message_text(chat_id=query.message.chat_id, text="محاضرات تحليل حقيقي", message_id=query.message.message_id, reply_markup=reply_markup)

    elif query.data == "Real_Analysis_S":
        buttons = [
            [InlineKeyboardButton("سكشن 1", url="")],
            [InlineKeyboardButton("سكشن 2", url="")],
            [InlineKeyboardButton("سكشن 3", url="")],
            [InlineKeyboardButton("سكشن 4", url="")],
            [InlineKeyboardButton("سكشن 5", url="")],
            [InlineKeyboardButton("سكشن 6", url="")],
            [InlineKeyboardButton("رجوع", callback_data="Real_Analysis")],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        bot.edit_message_text(chat_id=query.message.chat_id, text="سكاشن تحليل حقيقي", message_id=query.message.message_id, reply_markup=reply_markup)

    # Linear Algebra 1
    if query.data == "2":
        buttons = [
        [InlineKeyboardButton("محاضرات", callback_data="Linear_Algebra_1_L")],
        [InlineKeyboardButton("سكاشن", callback_data="Linear_Algebra_1_S")],
        [InlineKeyboardButton("كتاب الجبر الخطي", url="")],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        bot.send_message(chat_id=query.message.chat_id, text="جبر خطي (1)", reply_markup=reply_markup)

    if query.data == "Linear_Algebra_1":
        buttons = [
        [InlineKeyboardButton("محاضرات", callback_data="Linear_Algebra_1_L")],
        [InlineKeyboardButton("سكاشن", callback_data="Linear_Algebra_1_S")],
        [InlineKeyboardButton("كتاب الجبر الخطي", url="")],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        bot.edit_message_text(chat_id=query.message.chat_id, text="جبر خطي (1)",  message_id=query.message.message_id, reply_markup=reply_markup)

    if query.data == "Linear_Algebra_1_L":
        buttons = [
                [InlineKeyboardButton("محاضرة 1", url="")],
                [InlineKeyboardButton("محاضرة 2", url="")],
                [InlineKeyboardButton("محاضرة 3", url="")],
                [InlineKeyboardButton("محاضرة 4", url="")],
                [InlineKeyboardButton("محاضرة 5", url="")],
                [InlineKeyboardButton("محاضرة 6", url="")],
            [InlineKeyboardButton("رجوع", callback_data="Linear_Algebra_1")],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        bot.edit_message_text(chat_id=query.message.chat_id, text="محاضرات جبر خطي (1)", message_id=query.message.message_id,reply_markup=reply_markup)
    elif query.data == "Linear_Algebra_1_S":
        buttons = [
            [InlineKeyboardButton("سكشن 1", url="")],
            [InlineKeyboardButton("سكشن 2", url="")],
            [InlineKeyboardButton("سكشن 3", url="")],
            [InlineKeyboardButton("سكشن 4", url="")],
            [InlineKeyboardButton("سكشن 5", url="")],
            [InlineKeyboardButton("سكشن 6", url="")],
            [InlineKeyboardButton("رجوع", callback_data="Linear_Algebra_1")],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        bot.edit_message_text(chat_id=query.message.chat_id, text="سكاشن جبر خطي (1)", message_id=query.message.message_id,reply_markup=reply_markup)

    # Solid Analytic Geometry
    if query.data == "3":
        buttons = [
            [InlineKeyboardButton("محاضرات", callback_data="Solid_Analytic_Geometry_L")],
            [InlineKeyboardButton("سكاشن", callback_data="Solid_Analytic_Geometry_S")],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        bot.send_message(chat_id=query.message.chat_id, text="هندسة تحليلية فراغية", reply_markup=reply_markup)

    if query.data == "Solid_Analytic_Geometry":
        buttons = [
            [InlineKeyboardButton("محاضرات", callback_data="Solid_Analytic_Geometry_L")],
            [InlineKeyboardButton("سكاشن", callback_data="Solid_Analytic_Geometry_S")],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        bot.edit_message_text(chat_id=query.message.chat_id, text="هندسة تحليلية فراغية", message_id=query.message.message_id,reply_markup=reply_markup)
    if query.data == "Solid_Analytic_Geometry_L":
        buttons = [
                [InlineKeyboardButton("محاضرة 1", url="")],
                [InlineKeyboardButton("محاضرة 2", url="")],
                [InlineKeyboardButton("محاضرة 3", url="")],
                [InlineKeyboardButton("محاضرة 4", url="")],
                [InlineKeyboardButton("محاضرة 5", url="")],
                [InlineKeyboardButton("محاضرة 6", url="")],
            [InlineKeyboardButton("رجوع", callback_data="Solid_Analytic_Geometry")],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        bot.edit_message_text(chat_id=query.message.chat_id, text="محاضرات هندسة تحليلية فراغية", message_id=query.message.message_id, reply_markup=reply_markup)
    elif query.data == "Solid_Analytic_Geometry_S":
        buttons = [
            [InlineKeyboardButton("سكشن 1", url="")],
            [InlineKeyboardButton("سكشن 2", url="")],
            [InlineKeyboardButton("سكشن 3", url="")],
            [InlineKeyboardButton("سكشن 4", url="")],
            [InlineKeyboardButton("سكشن 5", url="")],
            [InlineKeyboardButton("سكشن 6", url="")],
            [InlineKeyboardButton("رجوع", callback_data="Solid_Analytic_Geometry")],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        bot.edit_message_text(chat_id=query.message.chat_id, text="سكاشن هندسة تحليلية فراغية", message_id=query.message.message_id, reply_markup=reply_markup)

    # Mechanics 4
    if query.data == "4":
        buttons = [
            [InlineKeyboardButton("محاضرات", callback_data="Mechanics_4_L")],
            [InlineKeyboardButton("سكاشن", callback_data="Mechanics_4_S")],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        bot.send_message(chat_id=query.message.chat_id, text="ميكانيكا 4", reply_markup=reply_markup)

    if query.data == "Mechanics_4":
        buttons = [
            [InlineKeyboardButton("محاضرات", callback_data="Mechanics_4_L")],
            [InlineKeyboardButton("سكاشن", callback_data="Mechanics_4_S")],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        bot.edit_message_text(chat_id=query.message.chat_id, text="ميكانيكا 4", message_id=query.message.message_id, reply_markup=reply_markup)

    if query.data == "Mechanics_4_L":
        buttons = [
                [InlineKeyboardButton("محاضرة 1", url="")],
                [InlineKeyboardButton("محاضرة 2", url="")],
                [InlineKeyboardButton("محاضرة 3", url="")],
                [InlineKeyboardButton("محاضرة 4", url="")],
                [InlineKeyboardButton("محاضرة 5", url="")],
                [InlineKeyboardButton("محاضرة 6", url="")],
            [InlineKeyboardButton("رجوع", callback_data="Mechanics_4")],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        bot.edit_message_text(chat_id=query.message.chat_id, text="محاضرات ميكانيكا 4", message_id=query.message.message_id, reply_markup=reply_markup)
    elif query.data == "Mechanics_4_S":
        buttons = [
            [InlineKeyboardButton("سكشن 1", url="")],
            [InlineKeyboardButton("سكشن 2", url="")],
            [InlineKeyboardButton("سكشن 3", url="")],
            [InlineKeyboardButton("سكشن 4", url="")],
            [InlineKeyboardButton("سكشن 5", url="")],
            [InlineKeyboardButton("سكشن 6", url="")],
            [InlineKeyboardButton("رجوع", callback_data="Mechanics_4")],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        bot.edit_message_text(chat_id=query.message.chat_id, text="سكاشن ميكانيكا 4", message_id=query.message.message_id, reply_markup=reply_markup)

    # Statistics
    if query.data == "5":
        buttons = [
            [InlineKeyboardButton("محاضرات", callback_data="Statistics_L")],
            [InlineKeyboardButton("سكاشن", callback_data="Statistics_S")],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        bot.send_message(chat_id=query.message.chat_id, text="الاحصاء و الاحتمالات", reply_markup=reply_markup)

    if query.data == "Statistics":
        buttons = [
            [InlineKeyboardButton("محاضرات", callback_data="Statistics_L")],
            [InlineKeyboardButton("سكاشن", callback_data="Statistics_S")],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        bot.edit_message_text(chat_id=query.message.chat_id, text="الاحصاء و الاحتمالات", message_id=query.message.message_id, reply_markup=reply_markup)

    if query.data == "Statistics_L":
        buttons = [
                [InlineKeyboardButton("محاضرة 1", url="")],
                [InlineKeyboardButton("محاضرة 2", url="")],
                [InlineKeyboardButton("محاضرة 3", url="")],
                [InlineKeyboardButton("محاضرة 4", url="")],
                [InlineKeyboardButton("محاضرة 5", url="")],
                [InlineKeyboardButton("محاضرة 6", url="")],
            [InlineKeyboardButton("رجوع", callback_data="Statistics")],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        bot.edit_message_text(chat_id=query.message.chat_id, text="محاضرات الاحصاء و الاحتمالات", message_id=query.message.message_id, reply_markup=reply_markup)
    elif query.data == "Statistics_S":
        buttons = [
            [InlineKeyboardButton("سكشن 1", url="")],
            [InlineKeyboardButton("سكشن 2", url="")],
            [InlineKeyboardButton("سكشن 3", url="")],
            [InlineKeyboardButton("سكشن 4", url="")],
            [InlineKeyboardButton("سكشن 5", url="")],
            [InlineKeyboardButton("سكشن 6", url="")],
            [InlineKeyboardButton("رجوع", callback_data="Statistics")],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        bot.edit_message_text(chat_id=query.message.chat_id, text="سكاشن الاحصاء و الاحتمالات", message_id=query.message.message_id, reply_markup=reply_markup)

    # Mathematical Biology
    if query.data == "6":
        buttons1 = [
            [InlineKeyboardButton("محاضرات", callback_data="Mathematical_Biology_L")],
            [InlineKeyboardButton("سكاشن", callback_data="Mathematical_Biology_S")],
            ]
        reply_markup = InlineKeyboardMarkup(buttons1)
        bot.send_message(chat_id=query.message.chat_id, text="رياضيات حيوية", reply_markup=reply_markup)

    if query.data == "Mathematical_Biology":
        buttons = [
            [InlineKeyboardButton("محاضرات", callback_data="Mathematical_Biology_L")],
            [InlineKeyboardButton("سكاشن", callback_data="Mathematical_Biology_S")],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        bot.edit_message_text(chat_id=query.message.chat_id, text="رياضيات حيوية",
                              message_id=query.message.message_id, reply_markup=reply_markup)

    if query.data == "Mathematical_Biology_L":
        buttons = [
                [InlineKeyboardButton("محاضرة 1", url="")],
                [InlineKeyboardButton("محاضرة 2", url="")],
                [InlineKeyboardButton("محاضرة 3", url="")],
                [InlineKeyboardButton("محاضرة 4", url="")],
                [InlineKeyboardButton("محاضرة 5", url="")],
                [InlineKeyboardButton("محاضرة 6", url="")],
            [InlineKeyboardButton("رجوع", callback_data="Mathematical_Biology")],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        bot.edit_message_text(chat_id=query.message.chat_id, text="محاضرات رياضيات حيوية",
                              message_id=query.message.message_id, reply_markup=reply_markup)
    elif query.data == "Mathematical_Biology_S":
        buttons = [
            [InlineKeyboardButton("سكشن 1", url="")],
            [InlineKeyboardButton("سكشن 2", url="")],
            [InlineKeyboardButton("سكشن 3", url="")],
            [InlineKeyboardButton("سكشن 4", url="")],
            [InlineKeyboardButton("سكشن 5", url="")],
            [InlineKeyboardButton("سكشن 6", url="")],
            [InlineKeyboardButton("رجوع", callback_data="Mathematical_Biology")],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        bot.edit_message_text(chat_id=query.message.chat_id, text="سكاشن رياضيات حيوية",
                              message_id=query.message.message_id, reply_markup=reply_markup)


button_handler = CallbackQueryHandler(buttons)
dispatcher.add_handler(button_handler)


def user_input(bot, update):
    if update.message.text.lower() == "start" or update.message.text.lower() == "/start" or update.message.text.lower() == "help" or update.message.text.lower() == "/help":
        button = [
            [InlineKeyboardButton("تحليل حقيقي", callback_data="1")],
            [InlineKeyboardButton("جبر خطي (1)", callback_data="2")],
            [InlineKeyboardButton("هندسة تحليلية فراغية", callback_data="3")],
            [InlineKeyboardButton("ميكانيكا 4", callback_data="4")],
            [InlineKeyboardButton("مقدمة في الاحصاء و الاحتمالات", callback_data="5")],
            [InlineKeyboardButton("رياضيات حيوية", callback_data="6")],
        ]
        reply_markup = InlineKeyboardMarkup(button)

        bot.send_message(chat_id=update.message.chat_id,
                         text="""
                    تم اضافة:
                     - محاضرة (1) تحليل حقيقي
                     - محاضر (1) رياضة حيوي
                     - كتاب التحليل الحقيقي
                     - كتاب الجبر الخطي
                     """,
                         reply_markup=reply_markup)
    else:
        if update.message.chat_id < 0:
            pass
        else:
            bot.send_message(chat_id=update.message.chat_id, text="""
            😢😢😢 لم يتم التعرف على الامر

   يمكنك استخدام امر /start لتشغيل البوت😀😀😀
            """)

user_input_handler = MessageHandler(Filters.text, user_input)
dispatcher.add_handler(user_input_handler)

updater.start_polling()
