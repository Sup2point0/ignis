'''
Script for fetching and saving cards data from the YGOPRODECK API.
'''

from scripts import Script


def script():
  import ygo

  ygo.api.update_cards_data()


if __name__ == "__main__":
  Script(script)
