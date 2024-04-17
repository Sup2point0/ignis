class Script:
  b = "-" * 20

  def __init__(self, script):
    print(f"{Script.b} STATUS: Running! {Script.b}")
    script()
    print(f"{Script.b} STATUS: Done! {Script.b}")
