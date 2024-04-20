'''
Script for fetching and saving cards data from the YGOPRODECK API.
'''

import suptools as sup


def script():
  import ygo

  ygo.api.update_cards_data()


if __name__ == "__main__":
  sup.run(script)
