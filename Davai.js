const { Telegraf, Markup } = require('telegraf')

require('dotenv').config()

const command = require('./commands')

const bot = new Telegraf(process.env.BOT_TOKEN)

//bot.start((ctx)=>console.log(ctx.message))

bot.start((ctx) => ctx.reply(`Здравствуй ${ctx.message.from.first_name ? ctx.message.from.first_name : 'Неизвестный'}!
Для получения списка доступных команд напишите /help`)) //вступительное сообщение

bot.command('h' ,(ctx) => ctx.reply(command.commands)) //команда хелп, добавить остальные команды

function ButtonAction(name, photo, video, text, file) {
    bot.action(name, async (ctx) => {
        try {
            await ctx.answerCbQuery()
            if(photo !== false) {
                await ctx.replyWithPhoto({
                    source : photo
                })
            }
            if(video !== false) {
                await ctx.replyWithVideo({
                    source : video
                })
            }
            if(text !== '') {
                await ctx.replyWithHTML(text, {

                })
            }
            if(file !== false) {
                await ctx.replyWithDocument({
                    source : file
                })
            }
        } catch (error) {
            console.error(error)
        }
    })
}

//VPN
bot.command('vpn', async (ctx) => {
    try {
        await ctx.replyWithHTML('<strong>Пожалуйста, выберите необходимый способ подключения или настройки удаленного доступа</strong>',
            Markup.inlineKeyboard(
                [
                    [Markup.button.callback('Подключение через cisco vpn', 'cisco')],
                    [Markup.button.callback('Подключение через удаленный рабочий стол', 'vpnn')]
                ]
            ))
    } catch (error) {
        console.error(error)
    }
})

bot.action('vpnn', async (ctx) => {
    try {
        await ctx.replyWithHTML('<strong>Пожалуйста, выберите вашу операционную систему</strong>',
            Markup.inlineKeyboard(
                [
                    [Markup.button.callback('Windows Xp', 'xp')],
                    [Markup.button.callback('Windows 7', '7')],
                    [Markup.button.callback('Windows 10', '10')]
                ]
            ))
    } catch (error) {
        console.error(error)
    }
})

ButtonAction('cisco', false, false, 'Все необходимые действия описаны в файле:', './VPN/Cisco/Xp7.docx')
ButtonAction('xp', false, false, 'Все необходимые действия описаны в файле:', './VPN/Default/Xp.docx')
ButtonAction('7', false, false, 'Все необходимые действия описаны в файле:', './VPN/Default/Semerka.docx')
ButtonAction('10', false, false, 'Все необходимые действия описаны в файле:', './VPN/Default/Инструкция по настройке vpn.docx')


//Cloud
bot.command('cloud', async (ctx) => {
    await ctx.reply(
        `Ознакомьтесь с видеообучением и документацией по использованию облачного хранилища:`)
    await ctx.replyWithVideo({source:'./Cloud/cloud.npptec.ru.mp4'})
    await ctx.replyWithDocument({source: './Cloud/Инструкция к облачному хранилищу cloud.npptec.doc'})
})

//Outlook
bot.command('outlook', async (ctx) => {
    try {
        await ctx.replyWithHTML('<strong>Пожалуйста, выберите необходимый способ подключения или настройки удаленного доступа</strong>',
            Markup.inlineKeyboard(
                [
                    [Markup.button.callback('Outlook 2007', '2007'), Markup.button.callback('Outlook 2010', '2010')],
                    [Markup.button.callback('Outlook 2013', '2013'), Markup.button.callback('Outlook 2016', '2016')],
                    [Markup.button.callback('Почта на телефоне', 'phone'), Markup.button.callback('Смена пароля', 'password')]
                ]
            ))
    } catch (error) {
        console.error(error)
    }
})

bot.action('2007', async (ctx) => {
    try {
        await ctx.replyWithHTML('<strong>Пожалуйста, выберите необходимую инструкцию</strong>',
            Markup.inlineKeyboard(
                [
                    [Markup.button.callback('Добавление дополнительного почтового ящика', '2007Add')],
                    [Markup.button.callback('Создание подписи электронной почты', '2007Create')]
                ]
            ))
    } catch (error) {
        console.error(error)
    }
})

bot.action('2010', async (ctx) => {
    try {
        await ctx.replyWithHTML('<strong>Пожалуйста, выберите необходимую инструкцию</strong>',
            Markup.inlineKeyboard(
                [
                    [Markup.button.callback('Автоархивация', '2010AutoArchive')],
                    [Markup.button.callback('Добавление дополнительного почтового ящика', '2010Add')],
                    [Markup.button.callback('Заместитель', '2010Assistance')],
                    [Markup.button.callback('Создание подписи электронной почты', '2010Create')]
                ]
            ))
    } catch (error) {
        console.error(error)
    }
})

bot.action('2013', async (ctx) => {
    try {
        await ctx.replyWithHTML('<strong>Пожалуйста, выберите необходимую инструкцию</strong>',
            Markup.inlineKeyboard(
                [
                    [Markup.button.callback('Архивация', '2013Archive')],
                    [Markup.button.callback('Автоархивация', '2013AutoArchive')],
                    [Markup.button.callback('Добавление дополнительного почтового ящика', '2013Add')],
                    [Markup.button.callback('Заместитель', '2013Assistance')],
                    [Markup.button.callback('Создание подписи электронной почты', '2013Create')]
                ]
            ))
    } catch (error) {
        console.error(error)
    }
})

bot.action('2016', async (ctx) => {
    try {
        await ctx.replyWithHTML('<strong>Пожалуйста, выберите необходимую инструкцию</strong>',
            Markup.inlineKeyboard(
                [
                    [Markup.button.callback('Установка Outlook2016', '2016Install')],
                    [Markup.button.callback('Автоархивация', '2016AutoArchive')],
                    [Markup.button.callback('Добавление дополнительного почтового ящика', '2016Add')],
                    [Markup.button.callback('Заместитель', '2016Assistance')]
                ]
            ))
    } catch (error) {
        console.error(error)
    }
})

ButtonAction('phone', false, false, 'Все необходимые действия описаны в файле:', './Outlook/Телефон/Настройка эл.почты на смартфоне.docx')
ButtonAction('password', false, false, 'Все необходимые действия описаны в файле:', './Outlook/Смена пароля через Outlook Web App.docx')
ButtonAction('2007Add', false, false, 'Все необходимые действия описаны в файле:', './Outlook/2007/Добавление доп. почтового ящика в MS Outlook.doc')
ButtonAction('2007Create', false, false, 'Все необходимые действия описаны в файле:', './Outlook/2007/Создание подписи электронной почты в Outlook 2007.docx')
ButtonAction('2010AutoArchive', false, false, '', './Outlook/2010-2013/Автоархивация Outlook.docx')
ButtonAction('2010Add', false, false, 'Все необходимые действия описаны в файле:', './Outlook/2010-2013/Добавление доп. почтового ящика в MS Outlook.doc')
ButtonAction('2010Assistance', false, false, 'Все необходимые действия описаны в файле:', './Outlook/2010-2013/Заместитель Outlook.docx')
ButtonAction('2010Create', false, false, 'Все необходимые действия описаны в файле:', './Outlook/2010-2013/Создание подписи электронной почты в Outlook 2010 и 2013.docx')
ButtonAction('2013Archive', false, false, 'Все необходимые действия описаны в файле:', './Outlook/2010-2013/архивация Outlook 2013.docx')
ButtonAction('2013AutoArchive', false, false, 'Все необходимые действия описаны в файле:', './Outlook/2010-2013/Автоархивация Outlook.docx')
ButtonAction('2013Add', false, false, 'Все необходимые действия описаны в файле:', './Outlook/2010-2013/Добавление доп. почтового ящика в MS Outlook.doc')
ButtonAction('2013Assistance', false, false, 'Все необходимые действия описаны в файле:', './Outlook/2013-2016 вне домена/Заместитель Outlook.docx')
ButtonAction('2013Create', false, false, 'Все необходимые действия описаны в файле:', './Outlook/2010-2013/Создание подписи электронной почты в Outlook 2010 и 2013.docx')
ButtonAction('2016Install', false, false, 'Все необходимые действия описаны в файле:', './Outlook/2013-2016 вне домена/Outlook2016.docx')
ButtonAction('2016AutoArchive', false, false, 'Все необходимые действия описаны в файле:', './Outlook/2013-2016 вне домена/Автоархивация Outlook.docx')
ButtonAction('2016Add', false, false, 'Все необходимые действия описаны в файле:', './Outlook/2013-2016 вне домена/Добавление доп. почтового ящика в MS Outlook.doc')
ButtonAction('2016Assistance', false, false, 'Все необходимые действия описаны в файле:', './Outlook/2013-2016 вне домена/Заместитель Outlook.docx')


//Newbee
bot.command('newbee', async (ctx) => {
    await ctx.reply(
        `Ознакомьтесь с инструкцией, содержащей базовые потребности для новых сотрудников:`)
    await ctx.replyWithDocument({source: './Newbee/Instruktsia_Po_IT_Dlya_Novykh_Sotrudnikov (2).docx'})
})

//Zoom
bot.command('zoom', async (ctx) => {
    await ctx.reply(
        `Ознакомьтесь с инструкцией по работе в Zoom:`)
    await ctx.replyWithDocument({source: './Zoom/Инструкция для сотрудников ООО НПП ТЭК по работе в Zoom 2.pdf'})
})

//MicrosoftLync
bot.command('lync', async (ctx) => {
    await ctx.reply(
        `Ознакомьтесь с инструкцией по установке MicrosoftLync:`)
    await ctx.replyWithDocument({source: './MicrosoftLync/Установка Microsoft Lync 2013.docx'})
    await ctx.reply(
        `Также, Вы можете сразу скачать установщик:`)
    await ctx.replyWithDocument({source: './MicrosoftLync/CA.cer'})
})

//bot.command('find', async (ctx) => {})

bot.launch() //запускает бота

// Enable graceful stop
process.once('SIGINT', () => bot.stop('SIGINT'))
process.once('SIGTERM', () => bot.stop('SIGTERM'))

/*
try {

} catch (error) {
    console.error(error)
}

 */
