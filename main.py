import matplotlib.pylot as plt

lawfulnesses = []
goodnesses = []

with open('ratings.txt') as ratings:
  for line in ratings:
    pair = line.split(' ')
    lawfulnesses.append(float(pair[0]))
    goodnesses.append(float(pair[1]))
    
plt.xlabel('Lawfulness')
plt.ylabel('Goodness')

plt.plot(lawfulnesses, goodnesses)
plt.show()
