import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters

load_dotenv()
TOKEN = os.getenv('TOKEN')


def get_main_keyboard():
    keyboard = [
        ["VPN", "Outlook"],
        ["Cloud", "Zoom"],
        ["Lync", "Newbee"],
        ["Help"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    name = user.first_name if user and user.first_name else 'Неизвестный'
    await update.message.reply_text(
        f"Здравствуй {name}!\nДля получения списка доступных команд напишите /help",
        reply_markup=get_main_keyboard()
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/vpn - VPN\n/cloud - Облако\n/outlook - Outlook\n/newbee - Новичку\n/zoom - Zoom\n/lync - Lync",
        reply_markup=get_main_keyboard()
    )


async def vpn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Подключение через cisco vpn", callback_data='cisco')],
        [InlineKeyboardButton("Подключение через удаленный рабочий стол", callback_data='vpnn')]
    ]
    await update.message.reply_text("<strong>Пожалуйста, выберите необходимый способ подключения или настройки удаленного доступа</strong>", parse_mode='HTML', reply_markup=InlineKeyboardMarkup(keyboard))

async def vpnn_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("Windows Xp", callback_data='xp')],
        [InlineKeyboardButton("Windows 7", callback_data='7')],
        [InlineKeyboardButton("Windows 10", callback_data='10')]
    ]
    await query.message.reply_text("<strong>Пожалуйста, выберите вашу операционную систему</strong>", parse_mode='HTML', reply_markup=InlineKeyboardMarkup(keyboard))


async def outlook(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Outlook 2007", callback_data='2007'), InlineKeyboardButton("Outlook 2010", callback_data='2010')],
        [InlineKeyboardButton("Outlook 2013", callback_data='2013'), InlineKeyboardButton("Outlook 2016", callback_data='2016')],
        [InlineKeyboardButton("Почта на телефоне", callback_data='phone'), InlineKeyboardButton("Смена пароля", callback_data='password')]
    ]
    await update.message.reply_text("<strong>Пожалуйста, выберите необходимый способ подключения или настройки удаленного доступа</strong>", parse_mode='HTML', reply_markup=InlineKeyboardMarkup(keyboard))

async def outlook_submenu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    if data == '2007':
        keyboard = [
            [InlineKeyboardButton("Добавление дополнительного почтового ящика", callback_data='2007Add')],
            [InlineKeyboardButton("Создание подписи электронной почты", callback_data='2007Create')]
        ]
        await query.message.reply_text("<strong>Пожалуйста, выберите необходимую инструкцию</strong>", parse_mode='HTML', reply_markup=InlineKeyboardMarkup(keyboard))
    elif data == '2010':
        keyboard = [
            [InlineKeyboardButton("Автоархивация", callback_data='2010AutoArchive')],
            [InlineKeyboardButton("Добавление дополнительного почтового ящика", callback_data='2010Add')],
            [InlineKeyboardButton("Заместитель", callback_data='2010Assistance')],
            [InlineKeyboardButton("Создание подписи электронной почты", callback_data='2010Create')]
        ]
        await query.message.reply_text("<strong>Пожалуйста, выберите необходимую инструкцию</strong>", parse_mode='HTML', reply_markup=InlineKeyboardMarkup(keyboard))
    elif data == '2013':
        keyboard = [
            [InlineKeyboardButton("Архивация", callback_data='2013Archive')],
            [InlineKeyboardButton("Автоархивация", callback_data='2013AutoArchive')],
            [InlineKeyboardButton("Добавление дополнительного почтового ящика", callback_data='2013Add')],
            [InlineKeyboardButton("Заместитель", callback_data='2013Assistance')],
            [InlineKeyboardButton("Создание подписи электронной почты", callback_data='2013Create')]
        ]
        await query.message.reply_text("<strong>Пожалуйста, выберите необходимую инструкцию</strong>", parse_mode='HTML', reply_markup=InlineKeyboardMarkup(keyboard))
    elif data == '2016':
        keyboard = [
            [InlineKeyboardButton("Установка Outlook2016", callback_data='2016Install')],
            [InlineKeyboardButton("Автоархивация", callback_data='2016AutoArchive')],
            [InlineKeyboardButton("Добавление дополнительного почтового ящика", callback_data='2016Add')],
            [InlineKeyboardButton("Заместитель", callback_data='2016Assistance')]
        ]
        await query.message.reply_text("<strong>Пожалуйста, выберите необходимую инструкцию</strong>", parse_mode='HTML', reply_markup=InlineKeyboardMarkup(keyboard))


async def file_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    files = {
        # VPN
        'cisco': ('Все необходимые действия описаны в файле:', './VPN/Cisco/Xp7.docx'),
        'xp': ('Все необходимые действия описаны в файле:', './VPN/Default/Xp.docx'),
        '7': ('Все необходимые действия описаны в файле:', './VPN/Default/Semerka.docx'),
        '10': ('Все необходимые действия описаны в файле:', './VPN/Default/Инструкция по настройке vpn.docx'),
        # Outlook
        'phone': ('Все необходимые действия описаны в файле:', './Outlook/Телефон/Настройка эл.почты на смартфоне.docx'),
        'password': ('Все необходимые действия описаны в файле:', './Outlook/Смена пароля через Outlook Web App.docx'),
        '2007Add': ('Все необходимые действия описаны в файле:', './Outlook/2007/Добавление доп. почтового ящика в MS Outlook.doc'),
        '2007Create': ('Все необходимые действия описаны в файле:', './Outlook/2007/Создание подписи электронной почты в Outlook 2007.docx'),
        '2010AutoArchive': ('', './Outlook/2010-2013/Автоархивация Outlook.docx'),
        '2010Add': ('Все необходимые действия описаны в файле:', './Outlook/2010-2013/Добавление доп. почтового ящика в MS Outlook.doc'),
        '2010Assistance': ('Все необходимые действия описаны в файле:', './Outlook/2010-2013/Заместитель Outlook.docx'),
        '2010Create': ('Все необходимые действия описаны в файле:', './Outlook/2010-2013/Создание подписи электронной почты в Outlook 2010 и 2013.docx'),
        '2013Archive': ('Все необходимые действия описаны в файле:', './Outlook/2010-2013/архивация Outlook 2013.docx'),
        '2013AutoArchive': ('Все необходимые действия описаны в файле:', './Outlook/2010-2013/Автоархивация Outlook.docx'),
        '2013Add': ('Все необходимые действия описаны в файле:', './Outlook/2010-2013/Добавление доп. почтового ящика в MS Outlook.doc'),
        '2013Assistance': ('Все необходимые действия описаны в файле:', './Outlook/2013-2016 вне домена/Заместитель Outlook.docx'),
        '2013Create': ('Все необходимые действия описаны в файле:', './Outlook/2010-2013/Создание подписи электронной почты в Outlook 2010 и 2013.docx'),
        '2016Install': ('Все необходимые действия описаны в файле:', './Outlook/2013-2016 вне домена/Outlook2016.docx'),
        '2016AutoArchive': ('Все необходимые действия описаны в файле:', './Outlook/2013-2016 вне домена/Автоархивация Outlook.docx'),
        '2016Add': ('Все необходимые действия описаны в файле:', './Outlook/2013-2016 вне домена/Добавление доп. почтового ящика в MS Outlook.doc'),
        '2016Assistance': ('Все необходимые действия описаны в файле:', './Outlook/2013-2016 вне домена/Заместитель Outlook.docx'),
    }
    if query.data in files:
        text, path = files[query.data]
        if text:
            await query.message.reply_text(text)
        await query.message.reply_document(document=open(path, 'rb'))

# Cloud
async def cloud(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ознакомьтесь с видеообучением и документацией по использованию облачного хранилища:")
    await update.message.reply_video(video=open('./Cloud/cloud.npptec.ru.mp4', 'rb'))
    await update.message.reply_document(document=open('./Cloud/Инструкция к облачному хранилищу cloud.npptec.doc', 'rb'))

# Newbee 
async def newbee(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ознакомьтесь с инструкцией, содержащей базовые потребности для новых сотрудников:")
    await update.message.reply_document(document=open('./Newbee/Instruktsia_Po_IT_Dlya_Novykh_Sotrudnikov (2).docx', 'rb'))

# Zoom 
async def zoom(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ознакомьтесь с инструкцией по работе в Zoom:")
    await update.message.reply_document(document=open('./Zoom/Инструкция для сотрудников ООО НПП ТЭК по работе в Zoom 2.pdf', 'rb'))

# Lync 
async def lync(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ознакомьтесь с инструкцией по установке MicrosoftLync:")
    await update.message.reply_document(document=open('./MicrosoftLync/Установка Microsoft Lync 2013.docx', 'rb'))
    # await update.message.reply_document(document=open('./MicrosoftLync/CA.cer', 'rb')) # если файл есть


async def button_menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if text == "vpn":
        await vpn(update, context)
    elif text == "outlook":
        await outlook(update, context)
    elif text == "cloud":
        await cloud(update, context)
    elif text == "zoom":
        await zoom(update, context)
    elif text == "lync":
        await lync(update, context)
    elif text == "newbee":
        await newbee(update, context)
    elif text == "help":
        await help_command(update, context)
    else:
        await update.message.reply_text("Пожалуйста, выберите команду из меню или используйте /help", reply_markup=get_main_keyboard())


def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("vpn", vpn))
    app.add_handler(CommandHandler("cloud", cloud))
    app.add_handler(CommandHandler("outlook", outlook))
    app.add_handler(CommandHandler("newbee", newbee))
    app.add_handler(CommandHandler("zoom", zoom))
    app.add_handler(CommandHandler("lync", lync))
    app.add_handler(CallbackQueryHandler(vpnn_callback, pattern="^vpnn$"))
    app.add_handler(CallbackQueryHandler(outlook_submenu, pattern="^(2007|2010|2013|2016)$"))
    app.add_handler(CallbackQueryHandler(file_callback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, button_menu_handler))
    print("Бот запущен!")
    app.run_polling()

if __name__ == '__main__':
    main() 