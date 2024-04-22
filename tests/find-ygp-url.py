import suptools as sup
import ygo


def script():
  '''
  Test that we can find the URL on Yugipedia of a card.
  '''

  card = int(sup.input("id"))
  print(ygo.link.url(card))


if __name__ == "__main__":
  sup.run(script)
