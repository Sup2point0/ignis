import suptools as sup


def script():
  '''Load a Yu-Gi-Oh deck exported from DuelingBook in XML format.'''

  import textwrap
  
  import ygo

  DECK = "Essence"
  line = "\n"

  with open(f"../assets/data/{DECK.lower()}.xml", "r") as file:
    data = ygo.deck.load(file.read())

  content = f'''
  # {DECK}

  <table>
    <tr>
      <td> total cards </td>
      <td> {sum(deck.get("cards-total", 0) for deck in data.values() if isinstance(deck, dict))}
    </tr>
    <tr>
      <td> unique cards </td>
      <td> {sum(deck.get("cards-unique", 0) for deck in data.values() if isinstance(deck, dict))}
    </tr>
  </table>

  ## Main Deck

  <table>
    <tr>
      <td> total cards </td>
      <td> {data["main"]["cards-total"]}
    </tr>
    <tr>
      <td> unique cards </td>
      <td> {data["main"]["cards-unique"]}
    </tr>
  </table>
  
  {f"  {line}  ".join(card for card in data["main"]["cards"].keys())}

  ## Extra Deck

  <table>
    <tr>
      <td> total cards </td>
      <td> {data["extra"]["cards-unique"]}
    </tr>
    <tr>
      <td> unique cards </td>
      <td> {data["extra"]["cards-unique"]}
    </tr>
  </table>
  
  {f"  {line}  ".join(card for card in data["extra"]["cards"].keys())}
  '''

  with open(f"../assets/out/{DECK}.md", "w") as file:
    file.write(textwrap.dedent(content).strip())


if __name__ == "__main__":
  sup.run(script)
