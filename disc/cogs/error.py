'''
Handles application errors.
'''

from dataclasses import dataclass

import nextcord as disc
from nextcord import Embed
from nextcord import ui
from nextcord.ui import button
from nextcord.ext import commands


@ dataclass
class ExceptionResponse(Exception):
  '''Special exception class for handling bot errors.'''

  title: str = None
  desc: str = None


class Error(commands.Cog):
  '''Error handlers.'''
  
  def __init__(self, bot):
    self.bot = bot

  @ commands.Cog.listener()
  async def on_application_command_error(ctx, error):
    '''Handle slash command exceptions.'''

    class Visual(ui.View):
      def __init__(self):
        super().__init__(timeout = 120)

      @ button(label = "View Output", custom_id = "root.debug")
      async def debug(self, button, ctx):
        button.disabled = True

        await ctx.response.edit_message(
          embed = Embed(
            title = error.get("title", "Error"),
            decsription = f"```{error}```",
            colour = 0x9040f1,
          ),
          view = self,
        )
    
    if isinstance(error, ExceptionResponse):
      out = error.desc
    else:
      out = dyna.errors.select()
    
    if not out.endswith((".", "!", "?", " ")):
      out += dyna.punct.select()
    
    await ctx.send(ephemeral = True,
      embed = Embed(
        title = error.get("title", "Error"),
        description = out,
        colour = 0xff0090,
      ),
      view = Visual(),
    )

    trace = "\n".join(traceback.format_exception(error))
    print(trace)
