import numpy as np
import sys

# recebe um arquivo e retorna a instancia
def learqv(nome_arquivo):
    instanciamatriz = np.loadtxt(nome_arquivo)
    return instanciamatriz

# recebe uma matriz e retorna o numero de linhas e colunas da matriz
def getdimensaomatriz(matriz):
    numLinhas, numColunas = matriz.shape
    return numLinhas, numColunas

# recebe o nome da instância, a matriz e suas dimensões, após isso, imprime essas informaçoes e salva em um arquivo
def resultado(nomeInstancia, matriz, numLinhas, numColunas):
    print(f"Nome da instância: {nomeInstancia}")
    print(f"Matriz de dimensão: {numLinhas} linhas x {numColunas} colunas")
    with open(f"resultado_{nomeInstancia}.txt", "w") as f:
        f.write(f"Nome da instância: {nomeInstancia}\n")
        f.write(f"Matriz de dimensão: {numLinhas} linhas x {numColunas} colunas\n")

# le a matriz através do nome da instancia e nos dá o resultado
def main(nomeInstancia):
    instanciamatriz = learqv(nomeInstancia)
    numLinhas, numColunas = getdimensaomatriz(instanciamatriz)
    resultado(nomeInstancia, instanciamatriz, numLinhas, numColunas)

# caso um argumento seja passado, chama a função. Se nao for chamado, exibe mensagem de erro ensinando a consertar
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("utilizar: python atividade 1.py <nomeInstancia>")
    else:
        nomeInstancia = sys.argv[1]
    main(nomeInstancia)