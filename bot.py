import os
import discord
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# آيدي سيرفرك الأساسي المحمي
PROTECTED_GUILD_ID = 746092533150515250  
# آيدي حسابك الشخصي الصحيح على ديسكورد
YOUR_DISCORD_USER_ID = 541784687409102858

class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()
        print(f"Synced slash commands globally.")

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

client = MyClient()

@client.tree.command(name="clone", description="Clone and migrate server structure with strict security alert system.")
@app_commands.describe(source_guild_id="The ID of the source server to copy from")
async def clone(interaction: discord.Interaction, source_guild_id: str):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("❌ You need Administrator permissions to use this command.", ephemeral=True)
        return

    # فحص الحماية: هل الآيدي المدخل هو سيرفرك الأساسي المحمي؟
    if int(source_guild_id) == PROTECTED_GUILD_ID:
        await interaction.response.send_message("🛡️ Security Alert: This is a protected server and cannot be cloned!", ephemeral=True)
        
        # طباعة التحذير في الترمينال
        warning_msg = (
            f"🚨 SECURITY ALERT: Unauthorized clone attempt detected!\n"
            f"👤 User: {interaction.user} (ID: {interaction.user.id})\n"
            f"🌐 Target Server (Where command was run): {interaction.guild.name} (ID: {interaction.guild.id})\n"
            f"🎯 Attempted to clone protected server ID: {source_guild_id}"
        )
        print(warning_msg)

        # إرسال رسالة خاصة (DM) لك بمعلومات المحاولة على الآيدي الصحيح
        try:
            owner = await client.fetch_user(YOUR_DISCORD_USER_ID)
            if owner:
                embed = discord.Embed(
                    title="🚨 محاولة نسخ سيرفر محمي!",
                    description="حاول شخص ما محاولة نسخ سيرفرك الأساسي المحمي!",
                    color=discord.Color.red()
                )
                embed.add_field(name="👤 المستخدم", value=f"{interaction.user} (`{interaction.user.id}`)", inline=False)
                embed.add_field(name="🏰 السيرفر المُستهدف (الجديد)", value=f"{interaction.guild.name} (`{interaction.guild.id}`)", inline=False)
                embed.add_field(name="🔒 السيرفر المحمي", value=str(source_guild_id), inline=False)
                await owner.send(embed=embed)
                print("📩 Security DM notification sent successfully to owner.")
        except Exception as e:
            print(f"⚠️ Failed to send DM to owner: {e}")

        return

    await interaction.response.send_message(f"🚀 Starting full server and permissions cloning process...", ephemeral=True)
    
    target_guild = interaction.guild
    source_guild = client.get_guild(int(source_guild_id))
    
    if not source_guild:
        try:
            source_guild = await client.fetch_guild(int(source_guild_id))
        except Exception as e:
            print(f"❌ Error fetching source guild: {e}")
            return

    print(f"📦 Cloning FROM [{source_guild.name}] TO [{target_guild.name}] with Permissions")

    # 1. Clone Roles & Map them
    role_mapping = {}
    roles = sorted(source_guild.roles, key=lambda r: r.position)
    for role in roles:
        if role.is_default() or role.managed:
            continue
        try:
            new_role = await target_guild.create_role(
                name=role.name,
                permissions=role.permissions,
                color=role.color,
                hoist=role.hoist,
                mentionable=role.mentionable
            )
            role_mapping[role.id] = new_role
            print(f"✅ Created role: {role.name}")
        except Exception as e:
            print(f"⚠️ Failed to create role {role.name}: {e}")

    # Helper function to map overwrites
    def get_mapped_overwrites(channel, new_category=None):
        overwrites = {}
        for target, overwrite in channel.overwrites.items():
            if isinstance(target, discord.Role):
                if target.is_default():
                    overwrites[target_guild.default_role] = overwrite
                elif target.id in role_mapping:
                    overwrites[role_mapping[target.id]] = overwrite
            elif isinstance(target, discord.Member):
                pass
        return overwrites

    # 2. Clone Categories and Channels with Overwrites
    for category in source_guild.categories:
        try:
            cat_overwrites = get_mapped_overwrites(category)
            new_cat = await target_guild.create_category(
                name=category.name,
                position=category.position,
                overwrites=cat_overwrites
            )
            print(f"📁 Created Category with permissions: {category.name}")
            
            for channel in category.channels:
                try:
                    chan_overwrites = get_mapped_overwrites(channel)
                    if isinstance(channel, discord.TextChannel):
                        await target_guild.create_text_channel(
                            name=channel.name,
                            category=new_cat,
                            topic=channel.topic,
                            slowmode_delay=channel.slowmode_delay,
                            nsfw=channel.nsfw,
                            position=channel.position,
                            overwrites=chan_overwrites
                        )
                        print(f"💬 Created Text Channel with permissions: {channel.name}")
                    elif isinstance(channel, discord.VoiceChannel):
                        await target_guild.create_voice_channel(
                            name=channel.name,
                            category=new_cat,
                            bitrate=channel.bitrate,
                            user_limit=channel.user_limit,
                            position=channel.position,
                            overwrites=chan_overwrites
                        )
                        print(f"🔊 Created Voice Channel with permissions: {channel.name}")
                except Exception as e:
                    print(f"⚠️ Failed to create channel {channel.name}: {e}")
        except Exception as e:
            print(f"⚠️ Failed to create category {category.name}: {e}")

    print("✨ Full server and permissions cloning process completed successfully!")

if __name__ == "__main__":
    if not TOKEN:
        print("❌ Error: DISCORD_TOKEN is not set in the .env file!")
    else:
        client.run(TOKEN)
