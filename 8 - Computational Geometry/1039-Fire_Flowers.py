"""
1039 - Fire Flowers by myoshiro
"""

from sys import stdin
from math import sqrt

for line in stdin:
  
  intLine = list(map(int,line.split()))

  distC = intLine[3] + sqrt(((intLine[5]-intLine[2])**2) + ((intLine[4]-intLine[1])**2))

  if intLine[0] < distC:
    print('MORTO')
  else:
    print('RICO')
