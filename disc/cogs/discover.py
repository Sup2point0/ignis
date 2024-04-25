'''
Implements the `/discover` family of slash commands.
'''

import os
import random
from base64 import b64decode
from io import StringIO

import nextcord as disc
from nextcord import Embed, SlashOption
from nextcord import ui
from nextcord.ext import commands
from github import Github, Auth
from github.ContentFile import ContentFile
import fuzzywuzzy.process

import suptools as sup
from .. import dyna
from .error import ExceptionResponse


## NOTE Since PyGithub is synchronous (blocking), we lazy load as much as possible for these commands - first execution per lifetime may be slow as a result.


class Discover(commands.Cog):
  '''Commands relating to discovering my custom Yu-Gi-Oh creations.'''

  def __init__(self, bot):
    self.bot = bot

    self.content: dict[str, dict[str, str | dict]] = {
      "cards": None,
      "archetypes": None,
    }
    '''Content from Assort.'''


  ## utils ##
  async def _check_loaded_(self, ctx, content: str):
    '''Check if the content has been loaded, and if not, load it.'''
    
    if self.content[content] is None:
      # await ctx.response.defer()
      await self._load_content_(ctx)
  
  async def _load_content_(self, ctx):
    '''Synchronously fetch content from Assort through the GitHub API.
    
    This will only be called once per bot lifespan.
    '''

    # change it from `None`, so that we know we’re already loading
    self.content["archetypes"] = {}

    key = os.getenv("CYNEX")
    if key is None:
      raise ExceptionResponse("Cynex Error", "Failed to connect to GitHub")

    with Github(auth = Auth.Token(key)) as git:
      repo = git.get_repo("Sup2point0/Assort")
      
      archetypes = repo.get_contents("Yu-Gi-Oh!/archetypes")

    self.content["archetypes"] = {
      self._load_file_details_(file)
      for file in archetypes if not "readme" in file.name.casefold()
    }

  def _load_file_details_(self, file) -> dict:
    out = {
      "name": "",
      "content": "",
      "path": file.path,
    }

    content = StringIO()

    for line in sup.io.decode_base64_lines(file.content, lines = 10):
      if not out["name"]:
        if line.startswith("# "):
          out["name"] = line[2:]
      
      else:
        if ">" in line:
          continue
        if "##" in line or "<br>" in line:
          break
        content.write(line + "\n")

    out["content"] = content.getvalue()

    return out


  ## /discover ##
  @ disc.slash_command()
  async def discover(self, ctx):
    pass

  @ discover.subcommand()
  async def archetype(self, ctx,
    archetype: str = SlashOption(
      "archetype", "name of the archetype",
      required = False, default = None,
    ),
  ):
    '''discover a custom archetype'''

    await self._check_loaded_(ctx, "archetypes")

    if archetype is None:
      archetype = random.choice(self.content["archetypes"].keys())

    archetypes = (key.casefold() for key in self.content["archetypes"])

    try:
      found = archetypes[archetype.casefold()]
    except KeyError:
      await ctx.send(dyna.punctuate("No archetype with this name found"), ephemeral = True)
      return

    await ctx.send(embed = Embed(
      title = found["name"],
      url = "https://github.com/Sup2point0/Assort/blob/origin/" + found["path"],
      description = found["content"],
      colour = 0x40f190,
    ))
    
  @ archetype.on_autocomplete("archetype")
  async def fill_archetype(self, ctx, archetype):
    await self._check_loaded_(ctx, "archetypes")

    out = fuzzywuzzy.process.extract(archetype, self.content["archetypes"].keys(), limit = 12)
    await ctx.response.send_autocomplete(out)
