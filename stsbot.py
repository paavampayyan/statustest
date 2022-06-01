from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
import os
import random

BOT_TOKEN = "1661092061:AAGd2JzLkVpb1VxZUvCi-RrvVHsNM2luGOA"
API_ID = "1280226"
API_HASH = "40c6be639fd3e699783cbb43c511cef0"

bot = Client(
    'redirector',
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)
print("bot starting")


@bot.on_message(filters.command(['start']) & filters.private)
def start(client, message):
    message.reply_text('Hello, i am redirector bot made by @nousername_psycho')
    message.reply_text('Send me a video. i will upload it to our channnel')

    return

@bot.on_message(filters.command(['id']))
def id(client, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    message.reply_text(f"bro {user_name} your id is `{user_id}`.")

    return

@bot.on_message(filters.text & filters.private & ~filters.user("@nousername_psycho"))
def text(client, message):
    approve_admin = "1445436774"
    message.reply_text("Please send me a video.")
    message.forward(chat_id=approve_admin)

    return 

@bot.on_message(filters.forwarded & filters.private)
def forwarded(client, message):
    message.reply_text("sorry forwarded messages not allowed. upload your video manualy")

    return  

@bot.on_message(filters.video & filters.private & ~filters.forwarded)
def post(client, message):
    user_name = message.from_user.first_name
    user_id = message.from_user.id
    approve_admin = "1445436774"
    message.reply_text(f"✅ Thanks {user_name}. Once our admin has approved your video, it will be uploaded to our channel. I will let you know if your video has been approved or rejected.")
    message.copy(chat_id=approve_admin, caption=f"{user_id} {user_name}")
    text = f"bro {user_name} send me a video. waiting for your approval"
    bot.send_message(chat_id=approve_admin, text=text)

    return

@bot.on_message(filters.command(['approve']))
def approve(client, message):
    video_admin = -1001277083311
    video = message.reply_to_message
    sub_user = video.caption.split()[0]
    sub_usr = video.caption.split()[1]
    m = message.reply_text("⏫ Uploading.")
    caption=f"**⬆️ Uploaded By: {sub_usr[:15]} **\n**📣 Channel: [Whatsapp Status](https://t.me/whatsapp_statusvideos_malayalam)**"
    x = video.copy(chat_id=video_admin, caption=caption)
    m.edit("✅ Uploaded.")
    text = f"**GOOD NEWS!** we approved your video ✅"
    bot.send_message(chat_id=sub_user, text=text,
                reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "View Your Post 👀",
                        url=x.link
                    ),
                ]
            ]
        ),
        parse_mode="markdown"
    )

    return

    
@bot.on_message(filters.command(['reject']))
def reject(client, message):
    video = message.reply_to_message
    sub_user = video.caption.split()[0]
    message.reply_text("rejected")
    text = f"**sorry!** we rejected your video. ❌ Our admins were not impressed."
    bot.send_message(chat_id=sub_user, text=text)

    return

@bot.on_message(filters.chat("@nousername_psycho") & filters.text)
def log_fix(client,message):
    targ = message.reply_to_message.caption.split()[0]
    reply = message.text
   
    bot.send_chat_action(targ, action="typing")
    message.copy(targ, reply)
    message.reply_text("♣️ done")
    
admins = [
    "@nousername_psycho"
]

@bot.on_message(filters.video & filters.user(admins))
def video(client, message):
    user_name = message.from_user.first_name
    target = -1001277083311
    message.reply_text(f"{user_name} thank you for your video. i will upload it soon as possible")
    message.copy(chat_id=target,
                 caption=f"**⬆️ Uploaded By: {user_name[:15]} **\n**📣 Channel: [Whatsapp Status](https://t.me/whatsapp_statusvideos_malayalam)**")


    return

@bot.on_message(filters.video & filters.chat("@stsredirect"))
def video_group(client, message):
    user_name = message.from_user.first_name
    target = -1001277083311
    message.reply_text(f"{user_name} thank you for your video. i will upload it soon as possible")
    message.copy(chat_id=target,
                 caption=f"**⬆️ Uploaded By: {user_name[:15]} **\n**📣 Channel: [Whatsapp Status](https://t.me/whatsapp_statusvideos_malayalam)**")
                 

    return

@bot.on_message(filters.command(['end']) & filters.user("@nousername_psycho"))
def end(client, message):
    target = "-1001277083311"
    stickers = [
        "CAACAgUAAxkBAAEFlJVgVMcFBJ18tDtXyQZ3RChKLlKXVgACcQADqZrmFo-EY9zlcy2SHgQ",
        "CAACAgUAAxkBAAEFlHtgVMZ59pQS_GykR6qHuyl9ubZ0qwACTAADqZrmFlICpI0or7euHgQ",
        "CAACAgUAAxkBAAEFlHxgVMZ7J76A22wyE_6jWGpV9BF24QACSwADqZrmFnqmUB_Di3d3HgQ",
        "CAACAgUAAxkBAAEFlIFgVMaH94bx0KVNxN29WIu7N_IqgAACMQADqZrmFhp_BxfZmAWsHgQ",
        "CAACAgUAAxkBAAEFlIRgVMaP3kHnj5cRxZwsi99GMzgD5wACXwADqZrmFuv92Og6ogv7HgQ",
    ]
    message.reply_text("sending end sticker.")
    bot.send_sticker(chat_id=target, sticker=f"{random.choice(stickers)}")

@bot.on_message(filters.text & filters.user("@nousername_psycho"))
def send(client, message):
    k = message.text
    if k in ("upload", "Upload"):
        video_admin = -1001277083311
        video = message.reply_to_message
        replyed_user = video.from_user.first_name
        # print(video)
        m = message.reply_text("⏫ Uploading to channel")
        caption=f"**⬆️ Uploaded By: {replyed_user[:15]} **\n**📣 Channel: [Whatsapp Status](https://t.me/whatsapp_statusvideos_malayalam)**"
        video.copy(chat_id=video_admin, caption=caption)
        m.edit("✅ Uploaded.")

    return


bot.run()
