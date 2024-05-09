from classes import *
import sql

sql.setup_database()
sql.update_cards([
  Card(card_id = 69, name = "testing", card_type = "monster", kind = "normal", race = "cyberse", attribute = "dark", level = 2, is_effect = False, is_pend = False),
  Card(card_id = 42, name = "suppety", card_type = "monster", kind = "normal", race = "cyberse", attribute = "dark", level = 2, is_effect = False, is_pend = False)
])
print(f"fetched... {sql.load_monsters()}")
