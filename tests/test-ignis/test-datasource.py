'''
Test sourcing data from `DataSource`.
'''

import suptools as sup
import ygo
from ignis import DataSource as DS


def test_load():
  data = ygo.sql.load_monster_arts([ygo.MonsterCard.attribute == "DARK"])[:69]
  ds = DS(data, "race", 26)
  sup.log(datasource = ds)


if __name__ == "__main__":
  sup.run(test_load)
