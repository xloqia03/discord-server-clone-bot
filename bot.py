import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from colorama import init, Fore

init(autoreset=True)
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", 0))

intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{Fore.GREEN}[+] Logged in as {bot.user} (ID: {bot.user.id})")
    print(f"{Fore.CYAN}[+] Bot is active and ready for server migration tasks.")

@bot.command(name="clone", help="نسخ هيكل السيرفر الحالي بالكامل إلى السيرفر الجديد")
@commands.has_permissions(administrator=True)
async def clone(ctx, target_guild_id: int):
    await ctx.send("🔄 جاري بدء عملية استنساخ السيرفر والهيكل... يرجى الانتظار.")
    
    source_guild = ctx.guild
    target_guild = bot.get_guild(target_guild_id)
    
    if not target_guild:
        await ctx.send("❌ لم يتم العثور على السيرفر المستهدف أو أن البوت ليس موجوداً فيه.")
        return

    try:
        await ctx.send("🧹 جاري تنظيف السيرفر المستهدف من الرتب والقنوات القديمة...")
        for role in target_guild.roles:
            if role.name != "@everyone" and not role.managed:
                try:
                    await role.delete()
                except:
                    pass

        roles_mapping = {}
        source_roles = sorted(source_guild.roles, key=lambda r: r.position)
        for role in source_roles:
            if role.name == "@everyone":
                roles_mapping[role.id] = target_guild.default_role
                continue
            try:
                new_role = await target_guild.create_role(
                    name=role.name,
                    permissions=role.permissions,
                    color=role.color,
                    hoist=role.hoist,
                    mentionable=role.mentionable
                )
                roles_mapping[role.id] = new_role
            except Exception as e:
                print(f"Error creating role {role.name}: {e}")

        await ctx.send("✅ تم نسخ الرتب بنجاح، جاري إنشاء الفئات والقنوات...")

        for category in source_guild.categories:
            try:
                overwrites = {}
                for target_role, perm in category.overwrites.items():
                    if target_role.id in roles_mapping:
                        overwrites[roles_mapping[target_role.id]] = perm
                
                new_cat = await target_guild.create_category(name=category.name, overwrites=overwrites)
                
                for channel in category.text_channels:
                    text_overwrites = {}
                    for target_role, perm in channel.overwrites.items():
                        if target_role.id in roles_mapping:
                            text_overwrites[roles_mapping[target_role.id]] = perm
                    
                    await target_guild.create_text_channel(
                        name=channel.name,
                        category=new_cat,
                        topic=channel.topic,
                        slowmode_delay=channel.slowmode_delay,
                        nsfw=channel.nsfw,
                        overwrites=text_overwrites
                    )
                
                for channel in category.voice_channels:
                    voice_overwrites = {}
                    for target_role, perm in channel.overwrites.items():
                        if target_role.id in roles_mapping:
                            voice_overwrites[roles_mapping[target_role.id]] = perm
                            
                    await target_guild.create_voice_channel(
                        name=channel.name,
                        category=new_cat,
                        bitrate=channel.bitrate,
                        user_limit=channel.user_limit,
                        overwrites=voice_overwrites
                    )
            except Exception as e:
                print(f"Error creating category {category.name}: {e}")

        for channel in source_guild.text_channels:
            if channel.category is None:
                try:
                    await target_guild.create_text_channel(name=channel.name, topic=channel.topic)
                except:
                    pass

        for channel in source_guild.voice_channels:
            if channel.category is None:
                try:
                    await target_guild.create_voice_channel(name=channel.name)
                except:
                    pass

        await ctx.send("🚀 تم الانتهاء من استنساخ السيرفر والهيكل بنجاح تام!")
    except Exception as e:
        await ctx.send(f"❌ حدث خطأ أثناء عملية الاستنساخ: {str(e)}")

if __name__ == "__main__":
    bot.run(TOKEN)
