import discord
import asyncio
import random
import logging

class Clone:
    @staticmethod
    async def roles_delete(guild_to: discord.Guild):
        for role in guild_to.roles:
            try:
                if role.name != "@everyone":
                    await role.delete()
                    logging.info(f"the position {role.name} It has been deleted")
                    await asyncio.sleep(random.randint(1, 1))
            except discord.Forbidden:
                logging.error(
                    f"Error deleting job: {role.name} Insufficient permissions."
                )

            except discord.HTTPException as e:
                if e.status == 429:
                    logging.error(
                        f"Many requests were made. Waiting 60 seconds. Details: {e}"
                    )
                    await asyncio.sleep(60)
            except:
                logging.error(f"Unable to delete job {role.name} unidentified error")
                await asyncio.sleep(random.randint(9, 12))

    @staticmethod
    async def roles_create(guild_to: discord.Guild, guild_from: discord.Guild):
        roles = []
        role: discord.Role
        for role in guild_from.roles:
            if role.name != "@everyone":
                roles.append(role)
        roles = roles[::-1]
        for role in roles:
            try:
                await guild_to.create_role(
                    name=role.name,
                    permissions=role.permissions,
                    colour=role.colour,
                    hoist=role.hoist,
                    mentionable=role.mentionable,
                )
                logging.info(f"The position {role.name} Was raised")
                await asyncio.sleep(random.randint(1, 2))
            except discord.Forbidden:
                logging.error(
                    f"Error creating job: {role.name} Insufficient permissions."
                )
                await asyncio.sleep(random.randint(2, 3))
            except discord.HTTPException as e:
                if e.status == 429:
                    logging.error(
                        f"Many requests were made. Waiting 60 seconds. Details: {e}"
                    )
                    await asyncio.sleep(60)
            except:
                logging.error(f"Unable to create task {role.name} unidentified error")
                await asyncio.sleep(random.randint(9, 12))

    @staticmethod
    async def channels_delete(guild_to: discord.Guild):
        for channel in guild_to.channels:
            try:
                await channel.delete()
                logging.info(f"A category {channel.name} It has been deleted")
                await asyncio.sleep(1)
            except discord.Forbidden:
                logging.error(
                    f"Error deleting category: {channel.name} Insufficient permissions."
                )
                await asyncio.sleep(random.randint(2, 3))
            except discord.HTTPException as e:
                if e.status == 429:
                    logging.error(
                        f"Many requests were made. Waiting 60 seconds. Details: {e}"
                    )
                    await asyncio.sleep(60)
            except:
                logging.error(
                    f"Unable to delete channel {channel.name} unidentified error"
                )
                await asyncio.sleep(random.randint(9, 12))

    @staticmethod
    async def categories_create(guild_to: discord.Guild, guild_from: discord.Guild):
        channels = guild_from.categories
        channel: discord.CategoryChannel
        new_channel: discord.CategoryChannel
        for channel in channels:
            try:
                overwrites_to = {}
                for key, value in channel.overwrites.items():
                    role = discord.utils.get(guild_to.roles, name=key.name)
                    overwrites_to[role] = value
                new_channel = await guild_to.create_category(
                    name=channel.name, overwrites=overwrites_to
                )
                await new_channel.edit(position=channel.position)
                logging.info(f"A category {channel.name} Was raised")
                await asyncio.sleep(random.randint(1, 3))
            except discord.Forbidden:
                logging.error(
                    f"Error deleting category: {channel.name} Insufficient permissions."
                )
                await asyncio.sleep(random.randint(2, 3))
            except discord.HTTPException as e:
                if e.status == 429:
                    logging.error(
                        f"Many requests were made. Waiting 60 seconds. Details: {e}"
                    )
                    await asyncio.sleep(60)
            except:
                logging.error(
                    f"Unable to create category {channel.name} unidentified error"
                )
                await asyncio.sleep(random.randint(9, 12))

    @staticmethod
    async def channels_create(guild_to: discord.Guild, guild_from: discord.Guild):
        channel_text: discord.TextChannel
        channel_voice: discord.VoiceChannel
        category = None
        for channel_text in guild_from.text_channels:
            try:
                for category in guild_to.categories:
                    try:
                        if category.name == channel_text.category.name:
                            break
                    except AttributeError:
                        logging.warning(
                            f"The channel {channel_text.name} has no category!"
                        )
                        category = None
                        break

                overwrites_to = {}
                for key, value in channel_text.overwrites.items():
                    role = discord.utils.get(guild_to.roles, name=key.name)
                    overwrites_to[role] = value
                try:
                    new_channel = await guild_to.create_text_channel(
                        name=channel_text.name,
                        overwrites=overwrites_to,
                        position=channel_text.position,
                        topic=channel_text.topic,
                        slowmode_delay=channel_text.slowmode_delay,
                        nsfw=channel_text.nsfw,
                    )
                except:
                    new_channel = await guild_to.create_text_channel(
                        name=channel_text.name,
                        overwrites=overwrites_to,
                        position=channel_text.position,
                    )
                if category is not None:
                    await new_channel.edit(category=category)
                logging.info(f"The text channel {channel_text.name} Was raised")
                await asyncio.sleep(2.30)
            except discord.Forbidden:
                logging.error(f"Error creating text channel: {channel_text.name}")
                await asyncio.sleep(random.randint(8, 10))
            except discord.HTTPException as e:
                if e.status == 429:
                    logging.error(
                        f"Many requests were made. Waiting 60 seconds. Details: {e}"
                    )
                    await asyncio.sleep(60)
                    new_channel = await guild_to.create_text_channel(
                        name=channel_text.name,
                        overwrites=overwrites_to,
                        position=channel_text.position,
                    )
                if category is not None:
                    await new_channel.edit(category=category)
                logging.info(f"The channel {channel_text.name} has been created")
            except:
                logging.error(f"Error creating text channel: {channel_text.name}")
                await asyncio.sleep(random.randint(9, 12))

        category = None
        for channel_voice in guild_from.voice_channels:
            try:
                for category in guild_to.categories:
                    try:
                        if category.name == channel_voice.category.name:
                            break
                    except AttributeError:
                        logging.warning(
                            f"Voice channel {channel_voice.name} has no category!"
                        )
                        category = None
                        break

                overwrites_to = {}
                for key, value in channel_voice.overwrites.items():
                    role = discord.utils.get(guild_to.roles, name=key.name)
                    overwrites_to[role] = value
                try:
                    new_channel = await guild_to.create_voice_channel(
                        name=channel_voice.name,
                        overwrites=overwrites_to,
                        position=channel_voice.position,
                        bitrate=channel_voice.bitrate,
                        user_limit=channel_voice.user_limit,
                    )
                except:
                    new_channel = await guild_to.create_voice_channel(
                        name=channel_voice.name,
                        overwrites=overwrites_to,
                        position=channel_voice.position,
                    )
                if category is not None:
                    await new_channel.edit(category=category)
                logging.info(f"The voice channel {channel_voice.name} has been created")
                await asyncio.sleep(2.20)
            except discord.Forbidden:
                logging.error(f"Error in voice chanel: {channel_voice.name}")
                await asyncio.sleep(random.randint(6, 7))
            except discord.HTTPException as e:
                if e.status == 429:
                    logging.error(
                        f"Many requests were made. Waiting 60 seconds. Details: {e}"
                    )
                    await asyncio.sleep(60)
                    new_channel = await guild_to.create_voice_channel(
                        name=channel_voice.name,
                        overwrites=overwrites_to,
                        position=channel_voice.position,
                    )
                if category is not None:
                    await new_channel.edit(category=category)
                logging.info(f"The voice channel {channel_voice.name} has been created")
            except:
                logging.error(f"Error creating voice channel: {channel_voice.name}")

    @staticmethod
    async def emojis_create(guild_to: discord.Guild, guild_from: discord.Guild):
        emoji: discord.Emoji
        for emoji in guild_from.emojis:
            try:
                emoji_image = await emoji.url.read()
                await guild_to.create_custom_emoji(name=emoji.name, image=emoji_image)
                logging.info(f"The emoji {emoji.name} has been created")
                await asyncio.sleep(0.50)
            except discord.Forbidden:
                logging.error(
                    f"Error creating emoji: {emoji.name} Insufficient permissions."
                )
                await asyncio.sleep(random.randint(2, 3))
            except discord.HTTPException as e:
                if e.status == 429:
                    logging.error(
                        f"Many requests were made. Waiting 60 seconds. Details: {e}"
                    )
                    await asyncio.sleep(60)
            except:
                logging.error(f"Unable to create emoji {emoji.name} Unidentified error")
                await asyncio.sleep(random.randint(9, 12))

    @staticmethod
    async def guild_edit(guild_to: discord.Guild, guild_from: discord.Guild):
        try:
            try:
                icon_image = await guild_from.icon_url.read()
            except discord.errors.DiscordException:
                logging.error(f"Unable to read icon image from {guild_from.name}")
                icon_image = None
            await guild_to.edit(name=f"{guild_from.name}")
            if icon_image is not None:
                try:
                    await guild_to.edit(icon=icon_image)
                    logging.info(f"Changed group icon: {guild_to.name}")
                except:
                    logging.error(f"Error changing group icon: {guild_to.name}")
        except discord.LoginFailure:
            logging.error(
                "Unable to authenticate to account. Check that the token is correct."
            )
        except discord.Forbidden:
            logging.error(f"Error changing group icon: {guild_to.name}")
