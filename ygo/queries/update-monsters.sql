-- update data for a card

REPLACE INTO cards VALUES(
  :id,
  :name,
  :art,
  :type,
  :kind,
  :race,
  :attribute,
  :level,
  :attack,
  :defense,
  :pend
);
