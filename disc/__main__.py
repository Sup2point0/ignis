'''
Runs the Discord bot, Ai.
'''

if __name__ == "__main__":
  import sys
  for each in sys.path:
    print(each)
  
  import suptools as sup
  from disc.bot import script

  sup.run(script, vitals = True)
