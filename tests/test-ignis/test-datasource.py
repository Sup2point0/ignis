'''
Test sourcing data from `DataSource`.
'''

import suptools as sup
import ygo
from ignis import DataSource as DS


def test_load():
  data = ygo.sql.load_monster_arts([ygo.MonsterCard.attribute == "DARK"])[:69]
  ds = DS(data, "race", 26)
  assert len(ds) == 2
  
  batch = ds[0]
  for row in batch:
    sup.log(row = row)
  assert len(batch[0]) == 32
  assert len(batch[1]) == 32


if __name__ == "__main__":
  sup.run(test_load)
