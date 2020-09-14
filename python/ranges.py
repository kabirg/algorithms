test = [2,5,3,4,8,5,9]

print(f'length: {len(test)} \n')

x = range(len(test))
for n in x:
  print(f'{n}: {test[n]}')

print('\n---------------------\n')

x = range(3, len(test))
for n in x:
  print(f'{n}: {test[n]}')
