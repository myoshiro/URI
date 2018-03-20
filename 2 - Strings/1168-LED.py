"""
1168 - LED by myoshiro
"""
bag = [6,2,5,5,4,5,6,3,7,6,6]

N = int(input())

for i in range(N):
  
  leds=0
  
  line = input()
  
  for c in line:
    leds += bag[int(c)]
    
  print(str(leds) + ' leds')
