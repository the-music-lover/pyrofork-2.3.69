from pyrogram import Client, filters
from config_manager import read_config, update_config


@Client.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("**Welcome To Streem-Bot 🚀**")


@Client.on_message(filters.document | filters.video)
async def private_receive_handler(client, message):
    cfg = read_config()
    BIN_CHANNEL = cfg["BIN_CHANNEL"]
    URL = cfg["URL"]

    file = message.document or message.video

    msg = await message.copy(
        chat_id=int(BIN_CHANNEL),
        caption=f"📂 **{file.file_name} | Requested By - {message.from_user.mention}**"
    )

    online = f"{URL}/watch/{msg.id}"
    download = f"{URL}/download/{msg.id}"

    await message.reply_text(
        text=(
            f"**📌 <a href='{online}'>Watch Online</a>**\n\n"
            f"**🌿 <a href='{download}'>Download</a>**"
        ),
        disable_web_page_preview=True
    )


@Client.on_message(filters.private & (filters.photo | filters.audio))
async def photo_audio_error(client, message):
    await message.reply_text("**❌ This format is not supported**")

@Client.on_message(filters.command("set_url"))
async def set_url(client, message):
    try:
        _, url, bin_channel = message.text.split(maxsplit=2)
        update_config(url, bin_channel)

        await message.reply_text(
            "**✅ Configuration Updated Successfully**\n\n"
            f"🌐 URL: `{url}`\n"
            f"📦 BIN_CHANNEL: `{bin_channel}`"
        )
    except ValueError:
        await message.reply_text(
            "**❌ Invalid format**\n\n"
            "`/set_url https://example.com -100123456789`"
        )

@Client.on_message(filters.command("show_url"))
async def show_url(client, message):
    cfg = read_config()

    await message.reply_text(
        "**📄 Current Configuration**\n\n"
        f"🌐 URL: `{cfg['URL']}`\n"
        f"📦 BIN_CHANNEL: `{cfg['BIN_CHANNEL']}`"
    )
