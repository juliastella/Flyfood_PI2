# FlyFood
# 05/05/21
# Graziela Felix

from itertools import permutations

# FORMULA RECURSIVA DA GEOMETRIA DO TAXI


def geoTaxi(x1, y1, x2, y2):
    D = abs((x2-x1))+abs((y2-y1))
    return D

# LEITURA DE MATRIZ A PARTIR DE UM ARQUIVO .TXT

arquivo = open("matriz", "r") # ESCOLHENDO CASO TESTE
matriz = []
linha = arquivo.readline()
while linha != "":
    elementos = linha.split()
    matriz.append(elementos)
    linha = arquivo.readline()

arquivo.close()

# BUSCA NA MATRIZ e ARMAZENAGEM DE PONTOS EM UM DICIONÁRIO


pontos = []
dic_pontos = {}
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        letra = matriz[i][j]
        if matriz[i][j] == 'R':
            dic_pontos[letra] = (i, j)
        elif matriz[i][j] != '0':
            dic_pontos[letra] = (i, j)
            pontos.append(letra)
pontos = sorted(pontos)


# CALCULANDO PERMUTAÇÕES

permutacoes = permutations(pontos)
list_p = []
for i in list(permutacoes):
    list_p.append(i)

# CALCULANDO DISTANCIAS E VERIFICANDO MELHOR CAMINHO

m_caminho = 0
best_way = 'Best way'
for i in range(len(list_p)):
    pt = str(list_p[i][0])
    soma_dist = 0
    soma_dist = soma_dist + geoTaxi(dic_pontos['R'][0], dic_pontos['R'][1], dic_pontos[pt][0], dic_pontos[pt][1])
    for j in range(len(list_p[i])):
        if j == len(list_p[i])-1:
            pt = str(list_p[i][j])
            soma_dist = soma_dist + geoTaxi(dic_pontos[pt][0], dic_pontos[pt][1], dic_pontos['R'][0], dic_pontos['R'][1])
        else:
            ptA = str(list_p[i][j])
            ptB = str(list_p[i][j+1])
            soma_dist = soma_dist + geoTaxi(dic_pontos[ptA][0], dic_pontos[ptA][1], dic_pontos[ptB][0], dic_pontos[ptB][1])


    if i == 0:
        m_caminho = soma_dist
        best_way = str(list_p[0])
    else:
        if soma_dist < m_caminho:
            m_caminho = soma_dist
            best_way = str(list_p[i])

print(best_way, m_caminho)