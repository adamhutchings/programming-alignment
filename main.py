import matplotlib.pylot as plt

lawfulnesses = []
goodnesses = []

with open('ratings.txt') as ratings:
  for line in ratings:
    pair = line.split(' ')
    lawfulnesses.append(int(pair[0]))
    goodnesses.append(int(pair[1]))
    
plt.xlabel('Lawfulness')
plt.ylabel('Goodness')

plt.plot(lawfulnesses, goodnesses)
plt.show()
