import json
import logging
import discord
import asyncio
import sys
from baseapp.cloner.cloner import Clone
from pypulse import Aplication


if sys.platform == "win32" and sys.version_info >= (3, 8, 0):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def main():
    fmt = "[%(levelname)s] %(message)s"

    data = json.loads(
        open(
            f"{Aplication.Vars.APLICATION_PATH}\\baseapp\\cloner\\data.json", "r"
        ).read()
    )

    logging.basicConfig(
        level=logging.INFO,
        handlers=[logging.FileHandler(data["route"], "w", "utf-8")],
        format=fmt,
    )

    client = discord.Client()

    @client.event
    async def on_ready():
        guild_from = client.get_guild(int(data.get("target")))
        guild_to = client.get_guild(int(data.get("destination")))
        if await Clone.guild_edit(guild_to, guild_from) != False:
            await Clone.roles_delete(guild_to)
            await Clone.channels_delete(guild_to)
            await Clone.roles_create(guild_to, guild_from)
            await Clone.categories_create(guild_to, guild_from)
            await Clone.channels_create(guild_to, guild_from)
            await client.close()

    try:
        await client.start(data["token"], bot=False)
    except:
        logging.info("Token Problems")
