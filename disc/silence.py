'''
Implements the `silence` decorator for silencing exceptions from commands.
'''

from typing import Iterable

import suptools as sup


def silence(
  exceptions = Exception | Iterable[Exception],
):
  '''Silence exceptions from an asynchronous function.
  
  Used as a decorator.
  '''

  def decorator(func):
    async def wrapper(*args, **kwargs):
      try:
        return await func(*args, **kwargs)
      except exceptions as e:
        sup.log(act = f"@silence: silenced exception {e}")

    wrapper.__doc__ = func.__doc__

    return wrapper
  return decorator
