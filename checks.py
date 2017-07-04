from discord.ext import commands
from discord.utils import get


def group_exists_check():
    def predicate(ctx):
        print(ctx)
        if not ctx:
            return False

        def to_text_channel_name(voice_channel):
            formatted_name = voice_channel.replace(" ", "_").lower()
            return formatted_name

        voice_name = get_content_from_ctx(ctx)
        text_name = to_text_channel_name(voice_name)
        # fails if channels/roles already exist
        author = ctx.message.author
        server = author.server
        if get(server.channels, name=voice_name):
            print("A")
            return False
        if get(server.channels, name=text_name):
            print("B")
            return False
        if get(server.roles, name=voice_name):
            print("C")
            return False
        # fails if author is not in a voice channel
        if not author.voice_channel:
            print("D")
            return False
        print("E")
        return True
    return commands.check(predicate)


def get_content_from_ctx(ctx):
    content = ctx.message.content
    cmd = ctx.command.qualified_name
    return content[(content.find(cmd) + len(cmd)):].strip()
