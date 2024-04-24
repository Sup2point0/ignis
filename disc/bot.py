'''
Ai.
'''

import os
import traceback

import nextcord as disc
from nextcord import Embed
from nextcord import ui
from nextcord.ui import button
from nextcord.ext import commands

from dotenv import load_dotenv

import suptools as sup
from .cogs import cogs
from . import dyna
# from ignis import Ai


__version__ = "1.0.0"

bot = commands.Bot(intents = disc.Intents.none())


@ bot.event
async def on_application_command_error(ctx, error):
  '''Handle slash command exceptions.'''

  class Visual(ui.View):
    def __init__(self):
      super().__init__(timeout = 120)

    @ button(label = "View Output", custom_id = "root.debug")
    async def debug(self, button, ctx):
      button.disabled = True
      out = f"```{error}```"

      await ctx.response.edit_message(
        embed = Embed(
          title = "Error",
          decsription = out,
          colour = 0x9040f1,
        ),
        view = self,
      )
  
  out = dyna.errors.select()
  if not out.endswith((".", "!", "?", " ")):
    out += dyna.punct.select()
  
  await ctx.send(ephemeral = True,
    embed = Embed(
      title = "Error",
      description = out,
      colour = 0xff0090,
    ),
    view = Visual(),
  )

  trace = "\n".join(traceback.format_exception(error))
  print(trace)


def script():
  load_dotenv()
  # run this first, since some cogs depend on environment variables

  bot.remove_command("help")

  for cog in cogs:
    bot.add_cog(cog(bot))

  link = os.getenv("LINK")
  if link is None:
    raise ValueError("missing materials for Link Summon!")
  
  bot.run(token = link)
