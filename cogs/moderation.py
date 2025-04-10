from discord.ext import commands
import discord

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="No reason"):
        await member.ban(reason=reason)
        await ctx.send(f"🔨 {member} banned: {reason}")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="No reason"):
        await member.kick(reason=reason)
        await ctx.send(f"👢 {member} kicked: {reason}")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member, *, reason="No reason"):
        muted = discord.utils.get(ctx.guild.roles, name="Muted")
        if not muted:
            muted = await ctx.guild.create_role(name="Muted")
            for ch in ctx.guild.channels:
                await ch.set_permissions(muted, send_messages=False, speak=False)
        await member.add_roles(muted)
        await ctx.send(f"🔇 {member} muted: {reason}")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member):
        muted = discord.utils.get(ctx.guild.roles, name="Muted")
        if muted in member.roles:
            await member.remove_roles(muted)
            await ctx.send(f"🔊 {member} unmuted")
        else:
            await ctx.send(f"{member} is not muted.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def softban(self, ctx, member: discord.Member, *, reason="No reason"):
        await member.ban(reason=reason)
        await member.unban()
        await ctx.send(f"💨 {member} softbanned: {reason}")

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self, ctx, seconds: int):
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.send(f"🐢 Slowmode set to {seconds}s")

async def setup(bot):
    await bot.add_cog(Moderation(bot))
