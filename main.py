from itertools import permutations

file = open('matriz', 'r')

n, m = file.readline().split()
lines = file.read().splitlines()

coordenadas = {}
pontosDistribuicao = []

for i in range(int(n)):
    line = lines[i].split()
    for j in line:
        if j != '0':
            coordenadas[j]= (i, line.index(j))
            pontosDistribuicao.append(j)

print(coordenadas)
print(pontosDistribuicao)

pontosDistribuicao.remove('R')
shorteste_cost = float('inf')


