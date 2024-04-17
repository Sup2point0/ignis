'''
Script for fetching and saving cards data from the YGOPRODECK API.
'''

from scripts import Script


def script():
  import ygo

  ygo.sql.refresh()


if __name__ == "__main__":
  Script(script)
