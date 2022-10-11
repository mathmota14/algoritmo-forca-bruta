from itertools import permutations

#Lê o arquivo texto que possui a matriz
arquivo = open("matriz.txt")
cod = arquivo.readlines()
lista = []

for dados in cod:
    a = dados.replace("\n", "")
    b = a.split(" ")
    lista.append(b)

#Irá descobrir a quantidade de linhas e colunas, além das coordenadas do restaurante e dos pontos de entrega
tamanho = lista.pop(0)
linha = int(tamanho[0])
coluna = int(tamanho[1])
coordenadas, local = [], []

for l in range(linha):
    for c in range(coluna):
        if lista[l][c] != "0":
            coordenadas.append((l, c))
            local.append(lista[l][c])

#Cria um dicionário para o restaurante e outro para os pontos de entrega
dicionario = dict(zip(local, coordenadas))
restaurante = {}
restaurante['R'] = dicionario.pop('R')

#Variável p com todas os caminhos possíveis, variável r que fica mudando cada vez que chega em um ponto de entrega e a variável rTemp fixa do restaurante
p = list(permutations(dicionario.keys(), len(dicionario)))
r = restaurante.get('R')
rTemp = restaurante.get('R')

partida, índice, resultado = 0, 0, 0

#Calcula o custo partindo do ponto R(restaurante) e passando por todos os pontos de entrega
for t in range(len(p)):
    for u in range(len(dicionario)):
        listinha = [p[t][u]]
        partida += sum(tuple(map(lambda i, j: abs(i - j), r, dicionario.get(listinha[0]))))
        r = dicionario.get(listinha[0])
    #Quando chega no último ponto de entrega o drone volta para o restaurante
    partida += sum(tuple(map(lambda i, j: abs(i - j), r, rTemp)))

    #Armazena na variável resultado apenas o menor custo e o índice desse caminho que pode ser encontrado na variável p
    if resultado == 0 or partida <= resultado:
        resultado = partida
        índiceEncontrado = índice
    #Reseta
    índice += 1
    partida = 0
    r = rTemp

#Mostra o menor custo com o melhor caminho a ser seguido
print("Menor custo:", resultado)
print("Melhor caminho:", "R", ' '.join(p[índiceEncontrado]), "R")