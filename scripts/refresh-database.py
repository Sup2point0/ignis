from scripts import Script


def script():
  '''
  Script for fetching and saving cards data from the YGOPRODECK API.
  '''

  import ygo

  ygo.sql.refresh()


if __name__ == "__main__":
  Script(script)
