import discord
import random
import discord.ext

status = ["STATUS1", "STATUS2", "STATUS3", "STATUS4", "STATUS5"]
gods_hi = {}
#'.sa', '.SA', '.Sa', '.sA', "selamın aleykum", "Selamın aleykum", "selamınaleykum", "Selamınaleykum",
           #"Selamın Aleykum", "selamın aleyküm", "Selamın aleyküm", "selamınaleyküm", "Selamınaleyküm",
           #"Selamın Aleyküm"

class botclass(discord.Client):
    async def on_ready(self):
        print("BAŞLANGIÇ MESAJI")
        game = discord.Game(random.choice(status))
        await client.change_presence(status=discord.Status.online, activity=game)

    async def on_message(self, message):
        if message.author == client.user:
            return

        elif any(word in message.content for word in gods_hi) and str(message.author) == "KULLANICIadı ve ID":
            await message.channel.send('MESAJ')

        elif any(word in message.content for word in gods_hi) and str(message.author) == "KULLANICIadı ve ID":
            await message.channel.send('MESAJ')

        elif any(word in message.content for word in gods_hi) and str(message.author) == "KULLANICIadı ve ID":
            await message.channel.send('MESAJ')

        elif message.content == ".-KOMUT-" and str(message.author) == "KULLANICIadı ve ID":
            await message.channel.send('MESAJ')

        elif message.content == ".-KOMUT-":
            kemo = "<kullanıcıNO>"
            await message.channel.send(kemo + ' MESAJ')

        elif any(word in message.content for word in gods_hi) and str(message.author) == "KULLANICIadı ve ID":
            await message.channel.send('MESAJ :)')

        elif any(word in message.content for word in gods_hi):
            await message.channel.send('MESAJ')

        elif message.content == ".-KOMUT-":
            embed = discord.Embed(title = "MUTLU YILLLARRRR :tada: :tada:",
                                  description = "MESAJ")
            await message.channel.send(embed=embed)


        elif message.content == ".-KOMUT-":
            await message.channel.send("MESAJ")

        elif message.content == ".-KOMUT-":
            await message.channel.send("MESAJ")

        elif message.content == ".-KOMUT-":
            await message.channel.send("MESAJ")

        elif message.content == ".-KOMUT-":
            await message.channel.send("MESAJ")

        elif message.content == ".-KOMUT-":
            await message.channel.send("MESAJ")

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Hoşgeldin {0.mention} yardım istemek için başına nokta koyarak help yazabilirisin :)'.format(
                member)
            await guild.system_channel.send(to_send)


intents = discord.Intents.all()
intents.members = True

client = botclass(intents=intents)

client.run("TOKEN")





