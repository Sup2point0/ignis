'''
Implements the `predict` family of slash commands.
'''

import nextcord as disc
from nextcord import SlashOption
from nextcord.ext import commands


class predict(commands.Cog):
  '''Commands involving predicting using the neural network.'''

  def __init__(self, bot):
    self.bot = bot

  @ disc.slash_command()
  async def predict(self, ctx):
    pass

  @ predict.subcommand(name = "with-file")
  async def attribute(self, ctx,
    feature: str = SlashOption(
      "feature", "which feature of the card to predict",
      options = {"type": "kind", "attribute": "attribute"}, required = True,
    ),
    file: disc.Attachment,
  ):
    '''predict a feature of a card, given its art as an attachment'''

    await ctx.response.defer()

    raise NotImplementedError()
