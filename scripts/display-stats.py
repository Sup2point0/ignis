from scripts import Script


def script():
  '''
  Script for visualising the distributions of card stats.
  '''

  from stats import Visual

  view = Visual("race").view()


if __name__ == "__main__":
  Script(script)
