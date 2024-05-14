import suptools as sup


def script():
  '''Visualise the distributions of card stats.'''

  from stats import Visual

  view = Visual("race").view()


if __name__ == "__main__":
  sup.run(script)
