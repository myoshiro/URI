"""
1214 - Above Average by myoshiro
"""

C = int(input())

for i in range(C):
  
  line = input().split()

  N = int(line[0])

  intLine = line[1:]
  intLine = list(map(int,intLine))

  avg = sum(intLine) / N

  out = (len([x for x in intLine if x > avg]) / N)*100
  
  print('%.3f' % out + '%')
