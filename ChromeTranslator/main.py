import discord
from deep_translator import GoogleTranslator

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

CHANNELS_TO_TRANSLATE = ["𝔸𝕝𝕝𝕘𝕖𝕞𝕖𝕚𝕟", "𝔸𝕟𝕜ü𝕟𝕕𝕚𝕘𝕦𝕟𝕘𝕖𝕟", "𝕋𝕣𝕒𝕕𝕖𝕟"]

@client.event
async def on_ready():
    print(f'✅ Bot ist online als {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.name in CHANNELS_TO_TRANSLATE:
        original = message.content
        translated = GoogleTranslator(source='auto', target='en').translate(original)
        await message.channel.send(f"🇬🇧 **Englische Übersetzung:**\n> {translated}")

client.run("MTM2MjEzOTU2NTMwOTMwMTA1Ng.Gpap9c.FWQ4OzFoSaDuBpcsYJpIT11Fn9i64e-xgfY3qg")
