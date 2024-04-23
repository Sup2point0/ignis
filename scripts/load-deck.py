import suptools as sup


def script():
  '''Load a Yu-Gi-Oh deck exported from DuelingBook in XML format.'''

  import textwrap
  
  import ygo

  DECK = "Vengeance"

  with open(f"../assets/data/{DECK}.xml", "r") as file:
    data = ygo.deck.load(file.read())

  sup.log(data = data)

  content = f'''
  # {DECK}

  <table>
    <tr>
      <td> total cards </td>
      <td> {sum(deck.get("cards-total", 0) for deck in data)}
    </tr>
    <tr>
      <td> unique cards </td>
      <td> {sum(deck.get("cards-unique", 0) for deck in data)}
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
  
  {"  \n  ".join(card for card in data["main"])}

  ## Extra Deck

  <table>
    <tr>
      <td> total cards </td>
      <td> {sum(deck.get("cards-total", 0) for deck in data)}
    </tr>
    <tr>
      <td> unique cards </td>
      <td> {sum(deck.get("cards-unique", 0) for deck in data)}
    </tr>
  </table>
  
  {"  \n  ".join(card for card in data["extra"])}
  '''

  with open(f"../assets/out/{DECK}.md", "w") as file:
    file.write(textwrap.dedent(content).strip())


if __name__ == "__main__":
  sup.run(script)
