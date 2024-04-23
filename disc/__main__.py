'''
Runs the Discord bot, Ai.
'''

if __name__ == "__main__":
  import sys
  sys.path[0] = "/".join(sys.path[0].split("/")[:-1])
  ### TODO please, for the love of programming, fix this

  import suptools as sup
  from disc.bot import script

  sup.run(script, vitals = True)
