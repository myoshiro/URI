a = float(input())

if a < 0 or a > 100:
  print('Fora de intervalo')
elif a <= 50:
  if a <= 25:
    print('Intervalo [0,25]')
  else:
    print('Intervalo (25,50]')
else:
  if a <= 75:
    print('Intervalo (50,75]')
  else:
    print('Intervalo (75,100]')
