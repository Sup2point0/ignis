'''
Script for fetching and saving cards data from the YGOPRODECK API.
'''

if __name__ == "__main__":
  print("STATUS: RUNNING!")
  
  from ygo_api import *

  data = get_cards_data()
  save_cards_data(data)

  print("STATUS: DONE!")
