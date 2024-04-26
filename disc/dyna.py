'''
Stores dynamic response text.
'''

from suptools import WeightedList as FrozenWeightedList


def punctuate(text) -> str:
  '''Add punctuation to text.'''

  return text + punct.select()


punct = FrozenWeightedList(
  (12, "."),
  (10, "!"),
  (4, "?"),
  (2, "..."),
  (1, "!!"),
)


errors = FrozenWeightedList(
  (3000, "Something went wrong"),
  (3000, "An error occurred"),
  (3000, "An exception occurred"),
  (2500, "An error was encountered"),
  (2500, "An exception was encountered"),
  (2000, "Couldn’t do that"),
  (1000, "Nope couldn’t do that"),
  (2000, "Something failed"),
  (1000, r"Something failed ¯\_(ツ)_/¯"),
  (2000, "Something broke"),
  (1000, r"Something broke ¯\_(ツ)_/¯"),
  (500, "Something broke, lol "),
  (1000, "You’re out of luck, I’m afraid – something went wrong"),
  (1000, "The code has, unfortunately, thrown an error"),
  (1000, "Despite our best efforts, the code has broken"),
  (500, "On guard! An exception has occurred."),
  (500, "I’m not feeling so good..."),
  (500, "I’m broken again, dude..."),
  (500, "You’re killing me here..."),
  (200, "Alright, debugging time."),
  (200, "Uhhh..."),
  (200, "Yo, a little help here @SHARD-bot?"),
  (100, "Alright, debugging time..."),
  (100, "KOGEKI– I mean, "),
  (100, "Nandato?"),
  (50, "NANI?"),
  (50, "If you keep at this, I might get Copilot to start writing these error messages for me."),
  (50, "The fated event has happened..."),
  (50, "RED ALERT RED ALERT ERROR ERROR ERROR "),
  (10, "@Sup#2.0 my guy come fix me, I’ve broken again 0.o"),
)
