import suptools as sup


def script():
  '''Save card art images to local storage as `.npy` files.'''

  import numpy as np
  from skimage.io import imread

  import suptools as sup
  import config

  source = config.ROOT / "assets/images"
  source = source.glob("*.jpg")

  for i, path in enumerate(source):
    sup.log(act = f"saving {i}")
    out = config.ROOT / "assets/arrays" / f"{path.stem}.npy"
    np.save(out, imread(path))


if __name__ == "__main__":
  sup.run(script)
