'''
Script for fetching and saving cards data from the YGOPRODECK API.
'''

if __name__ == "__main__":
  print("STATUS: RUNNING!")
  
  import ygo

  ygo.update_cards_data()

  print("STATUS: DONE!")
