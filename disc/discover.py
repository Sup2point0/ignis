'''
Implements the `/discover` family of slash commands.
'''

import os
import random

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

    self.content: list[bytes | str] = {
      "cards": None,
      "archetypes": None,
    }
    '''Content from Assort. Initially stored as `bytes`, and lazily decoded to `str` when needed.'''


  ## utils ##
  class Keyless(Exception):
    '''GitHub API key not found.'''

  async def _load_data_(self, ctx):
    '''Asynchronously get custom content from Assort through the GitHub API.
    
    This will only be called once per bot lifespan.
    '''

    key = os.getenv("CYNEX")
    if key is None:
      await ctx.send("Error: Failed connecting to GitHub!")
      raise Discover.Keyless("cynex connection failed!")

    with Github(auth = Auth.Token()) as git:
      repo = git.get_repo("Sup2point0/Assort")
      content = repo.get_contents("Yu-Gi-Oh!")

      while content:
        file = content.pop(0)

        if file.type == "dir":
          folder = repo.get_contents(file.path)
          content.extend(folder)

        elif file.path.endswith(".md"):
          self.content.append(file.content)


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

    if not self.content["archetypes"]:
      await ctx.response.defer()
      await self._load_data_(ctx)

    if archetype is None:
      archetype = random.choice(self.content["archetypes"])
 