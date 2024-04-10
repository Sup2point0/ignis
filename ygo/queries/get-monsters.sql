SELECT id, name, art, race, attribute
  FROM cards
  WHERE type = "monster"
    AND type = (:type)
    AND attribute = (:attribute)
  ORDER BY name
