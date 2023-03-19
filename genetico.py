import random
from itertools import permutations
from sklearn.utils import shuffle
from random import randint

# Leitura do arquivo
arquivo = open('matriz', 'r')

n, m = arquivo.readline().split() # pega o arquivo e divide em linhas e colunas n e m
linhas = arquivo.read().splitlines()

coordenadas = {}
pontoDaMatriz = []

for i in range(int(n)):
    line = linhas[i].split()
    for j in line:
        if j != '0':
            coordenadas[j] = (i, line.index(j))
            pontoDaMatriz.append(j)

pontoDaMatriz.remove('R')

# Função gerador da população inicial
def pop_gerador(pontoDeliver, popSize):
    populacao = []
    permutation = shuffle(list(permutations(pontoDeliver)))

    for i in range(popSize):
        populacao.append(list(permutation[i]))

    return populacao


# calculo o tamanho do caminho de uma rota
def fitnes(route):
    route_cost = 0
    contador = 0

    item = list(route)
    item.append('R')
    item.insert(0, 'R')

    while contador < len(item) - 1:
        y_cost = abs(coordenadas[route[contador]][0] - coordenadas[route[contador + 1]][0])
        x_cost = abs(coordenadas[route[contador]][1] - coordenadas[route[contador + 1]][1])
        route_cost += x_cost + y_cost
        contador += 1

    del (route[0], route[-1])

    return route_cost

# rank da população

def rank(populacao):
    populacao.sort(key=lambda x: x[0])
    return populacao

# seleção torneio
def selection(populacao, m, k):
    global most_adaptable
    most_adaptable: []
    tournament = []

    for i in range(m):
        participantes = random.sample(populacao, k)
        for j in participantes:
            tournament.append((fitnes(j), j))
        ganhadores = rank(tournament)[0][1]
        most_adaptable.append(ganhadores)

    return most_adaptable

#cruzamento realizado por PMX
def crossover(parente1,parente2):
    breakPoint = randint(1, len(parente1)-1)
    backup = parente2[:]
    offspring = []

    for child in range(2):
        for ponto in range(breakPoint):
            if parente1[ponto] != parente2[ponto]:
                temp = parente2[ponto]
                parente2[ponto] = parente1[ponto]

                for change_point in range(ponto + 1, len(parente2)):
                    if parente1[ponto] == parente2[change_point]:
                        parente2[change_point] = temp
                        break

        offspring.append(parente2)
        parente2 = parente1
        parente1 = backup

    return offspring


# mutação por swap com 0.05% de chance de ocorrer
def mutacao(route):
    if random.random() < 0.05:
        mutation_point = randint(0, len(route) - 2)
        backup = route[mutation_point]

        route[mutation_point] = route[mutation_point + 1]
        route[mutation_point + 1] = backup

        return route

def ag(n):
    p = pop_gerador(pontoDaMatriz, 100) #população inicial
    lower_const = float('inf')
    contadorGeracoes = 0
    lc_list = []

    while gc < n:
        s = selection(p,20,5) #seleção dos 20 mais aptos
        p = []
        for k in  range(50):
            pai1 = random.choice(s)
            pai2 = random.choice(s)

            filho1, filho2 = crossover(pai1, pai2)

            mutacao(filho1)
            mutacao(filho2)

            p.append(filho1)
            p.append(filho2)

            gc += 1

            current_solution = selection(p, 1, 100)[0]

            if fitness(current_solution) < lower_cost:
                lower_cost = fitness(current_solution)
                lc_list.append(str(lower_cost))
                best_solution = current_solution

        return best_solution, lc_list

result = ag(100)
print(' '.join(result[0]))
print(' '.join(result[1]))












