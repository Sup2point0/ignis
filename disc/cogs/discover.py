'''
Implements the `/discover` family of slash commands.
'''

import os
import random
from base64 import b64decode
from io import BytesIO

import nextcord as disc
from nextcord import Embed, SlashOption
from nextcord import ui
from nextcord.ext import commands

from github import Github, Auth
from github.Repository import Repository
from github.ContentFile import ContentFile
from github.GithubException import UnknownObjectException


## NOTE Since PyGithub is synchronous (blocking), we lazy load as much as possible for these commands - first execution per lifetime may be slow as a result.


class Discover(commands.Cog):
  '''Commands relating to discovering my custom Yu-Gi-Oh creations.'''

  def __init__(self, bot):
    self.bot = bot

    self.content: dict[str, dict[str, bytes]] = {
      "cards": None,
      "archetypes": None,
    }
    '''Content from Assort. Initially stored as `bytes`, and lazily decoded to `str` when needed.'''


  ## utils ##
  class Keyless(Exception):
    '''GitHub API key not found.'''

  async def _load_content_(self, ctx):
    '''Synchronously fetch content from Assort through the GitHub API.
    
    This will only be called once per bot lifespan.
    '''

    # change it from `None`, so that we know we’re already loading
    self.content["archetypes"] = {}

    key = os.getenv("CYNEX")
    if key is None:
      await ctx.send("Error: Failed connecting to GitHub!")
      raise Discover.Keyless("cynex connection failed!")

    with Github(auth = Auth.Token(key)) as git:
      repo = git.get_repo("Sup2point0/Assort")
      
      archetypes = repo.get_contents("Yu-Gi-Oh!/archetypes/")
      self.content["archetypes"] = {
        base64decode(BytesIO(file.content).readline()): file.content
        for file in archetypes
        if not "readme" in file.name.casefold()
      }


  ## /discover ##
  @ disc.slash_command()
  async def discover(self, ctx):
    pass


  ## /discover archetype ##
  @ discover.subcommand()
  async def archetype(self, ctx,
    archetype: str = SlashOption(
      "archetype", "name of the archetype",
      required = False, default = None,
    ),
  ):
    '''discover a custom archetype'''

    if self.content["archetypes"] is None:
      await ctx.response.defer()
      await self._load_data_(ctx)

    if archetype is None:
      archetype = random.choice(self.content["archetypes"].keys())

    content = BytesIO(self.content[archetype])
 
