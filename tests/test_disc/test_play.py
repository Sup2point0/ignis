'''
Tests operations of Discord bot.
'''

from disc.cogs.play import Play


def test_ygordle_word_pick():
  test = lambda: Play(None).pick_ygordle_word("ygordle-words-5L")

  word = test()
  assert isinstance(word, str)
  assert len(word) == 5

  words = [test() for i in range(100)]
  assert all(isinstance(each, str) for each in words)
  assert all(len(each) == 5 for each in words)
