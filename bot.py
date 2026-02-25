import discord
import requests

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        # Prevent bot from replying to itself
        if message.author == self.user:
            return

        # $hello command
        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')

        # $meme command
        if message.content.startswith('$meme'):
            try:
                response = requests.get("https://meme-api.com/gimme")
                data = response.json()

                meme_url = data["url"]
                title = data["title"]
                subreddit = data["subreddit"]

                await message.channel.send(f"**{title}**\nFrom r/{subreddit}\n{meme_url}")

            except Exception as e:
                await message.channel.send("Oops! I couldn't fetch a meme right now.")
                print(e)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('YOUR_KEY')  