import numpy as np

def calculate(list):
  """list: containing 9 digits"""
  if len(list)!=9:
    raise ValueError("List must contain nine numbers.")
  ar = np.array(list).reshape((3,3))
  print(ar)

  calculations=None
  return calculations