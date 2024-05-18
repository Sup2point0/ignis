import suptools as sup


def script():
  '''Asynchronously fetch the card arts from the YGOPRODECK API and save them to local storage.'''

  import asyncio

  import ygo

  data = ygo.sql.load(ygo.CardArt)
  sup.log(action = "collecting tasks...")
  asyncio.run(ygo.api.async_save_card_arts(data))


if __name__ == "__main__":
  sup.run(script)
