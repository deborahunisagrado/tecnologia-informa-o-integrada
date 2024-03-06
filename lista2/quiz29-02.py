#Crie uma função que conte o número de vogais em uma string. 
def conta_vogais(string): 
    string = string.lower()
    result = {} 
    vogais = 'aeiou' 
    for i in vogais: 
        if i in string: 
            result[i] = string.count(i) 
    return result 
 
print(conta_vogais('olaaa')) 

#Escreva um programa que substitua todas as ocorrências de uma letra em uma string por outra letra. 
def trocar_letra(letras):
    string = letras.lower()
    result = {}
    letra = 'a'
    nova_letra = 'r'
    for i in letra:
        if i in letras:
            result = string.replace(letra, nova_letra)

        return result

print(trocar_letra('nuieNVOwaaaaaaAAAA'))


#Crie uma função que retorne o número de palavras em uma string. 
def numero_palavras(frase):
  split_frase = len(frase.split())
  result = "There are " + str(split_frase) + " words."

  return result

print(numero_palavras("A vida é bela"))


#Crie uma função que conte o número de ocorrências de uma determinada palavra em uma frase.
def contagem_palavra(frase):
  frases = frase.lower()
  qtd = frases.count("python")
  return qtd

print(contagem_palavra("A linguagem de programação python é muito interessante. Python abre muitos caminhos."))


#Crie uma função que encontre os k maiores elementos em uma lista, mantendo a ordem original.
def maiores_elementos(lista):
  ordenado = sorted(lista)
  return ordenado[-3:] 

print(maiores_elementos([1,5,6,2,6,8,2,4,10,0,2,5,8]))


#Escreva um programa que implemente a soma de matrizes usando listas aninhadas.
def soma_matrizes(matriz1, matriz2):
    matriz_soma = []
    for i in range(len(matriz1)):
        linha_soma = []
        for j in range(len(matriz1[0])):
            elemento_soma = matriz1[i][j] + matriz2[i][j]           
            linha_soma.append(elemento_soma)

        matriz_soma.append(linha_soma)

    return matriz_soma

matriz1 = [[1, 2, 3], [4, 5, 6]]
matriz2 = [[7, 8, 9], [10, 11, 12]]
print(soma_matrizes(matriz1, matriz2))

#Crie uma função que encontre a interseção de duas listas sem usar conjuntos.
def intersecao(lista1, lista2):
  nova_lista = []
  for i in lista1:
    for j in lista2:
      if i == j:
        nova_lista.append(i)
  return nova_lista


lista1 = [1, 2, 3, 4, 9]
lista2 = [3, 9, 6, 7, 8]
print(intersecao(lista1, lista2))


#Crie uma função que embaralhe os elementos de uma lista de forma aleatória.
import random

def embaralhar(lista):
  random.shuffle(lista)
  return lista

test_list = [1, 4, 5, 6, 3]
print(embaralhar(test_list))

#Escreva um programa que encontre o par de elementos em uma lista cuja soma seja igual a um determinado valor.
def soma_elementos(lista):
  indices = []
  for i in range(len(lista) - 1):
    if lista[i] +  lista[i+1] == 9:
      indices.append([i, i + 1])
  return indices

test_list = [1, 4, 5, 6, 3]
print(soma_elementos(test_list))

#Criar um algoritmo para calcular a frequência que uma palavra aparece em um texto.
def frequencia_palavra(frase):
  frases = frase.lower()
  qtd = frases.count("foi")
  return f"A palavra 'foi' tem uma ocorrência de {qtd} vezes"

print(frequencia_palavra('foi o melhor dos tempos foi o pior dos tempos'))

#Escreva um programa que identifique todos os números primos em uma lista de números inteiros.
def numeros_primo(lista):
  nova_lista = []
  for i in lista:
    if i > 1:
      for j in range(2, i):
        if i % j == 0:
            break
      else:
          nova_lista.append(i)


  return nova_lista

print(numeros_primo([2, 3, 4, 5, 6, 7, 8, 9, 10]))

#Implemente um algoritmo para encontrar a menor string em uma lista de strings.
def menor_string(palavras):
  menor = palavras[0]
  for i in palavras:
    if menor < i:
      menor = i
  return menor


print(menor_string(["A", "vida", "é", "bela"]))

#Crie um algoritmo para ler um arquivo texto
nome_arquivo = 'lista2/arquivo.txt'

try:
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except FileNotFoundError:
    print(f'O arquivo "{nome_arquivo}" não foi encontrado.')
except Exception as e:
    print(f"Ocorreu um erro: {e}")


#Crie um algoritmo para ler um arquivo CSV
import csv

nome_arquivo_csv = 'lista2/dados.csv'

try:
    with open(nome_arquivo_csv, 'r', newline='', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)

        for linha in leitor_csv:
            print(linha)
except FileNotFoundError:
    print(f'O arquivo CSV "{nome_arquivo_csv}" não foi encontrado.')
except Exception as e:
    print(f"Ocorreu um erro: {e}")


#Crie um algoritmo para ler um arquivo JSON.
import json

nome_arquivo_json = 'lista2/dados.json'

try:
    with open(nome_arquivo_json, 'r', encoding='utf-8') as arquivo_json:
        dados = json.load(arquivo_json)
        print(dados)

except FileNotFoundError:
    print(f'O arquivo JSON "{nome_arquivo_json}" não foi encontrado.')
except Exception as e:
    print(f"Ocorreu um erro: {e}")


#Crie um algoritmo para consolidar um ou mais arquivos de texto de um diretório.
import os
import shutil

def consolidar_arquivos(diretorio, arquivo_destino):
    try:
        # Lista todos os arquivos no diretório
        arquivos = os.listdir(diretorio)

        with open(arquivo_destino, 'w', encoding='utf-8') as consolidado:
            for arquivo in arquivos:
                if arquivo.endswith('.txt'):
                    caminho_arquivo = os.path.join(diretorio, arquivo)

                    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo_atual:
                        conteudo_arquivo = arquivo_atual.read()
                        consolidado.write(conteudo_arquivo)

                    consolidado.write('\n')

        print(f'Consolidação concluída. Conteúdo consolidado em "{arquivo_destino}".')
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

diretorio_origem = 'lista2/arquivos'
arquivo_destino = 'lista2/novos_dados.txt'
consolidar_arquivos(diretorio_origem, arquivo_destino)


#Crie um algoritmo para ler dados de um CSV (que possui os meses e valores de vendas), retornando qual o mês teve mais vendas.
from pandas import *
arquivo_vendas = 'lista2/vendas.csv'

try:
    with open(arquivo_vendas, 'r', newline='', encoding='utf-8') as arquivo_csv:
        data = read_csv("lista2/vendas.csv")
        vendas = data['VENDAS'].tolist()
        mes = data['MES'].tolist()

        for i in range(len(vendas)):
          if vendas[i] == max(vendas):
              print(f'O mês com mais vendas foi {mes[i]}.')
except FileNotFoundError:
    print(f'O arquivo CSV "{arquivo_vendas}" não foi encontrado.')
except Exception as e:
    print(f"Ocorreu um erro: {e}")

#Crie um algoritmo para ler dados de um CSV (que possui os meses e valores de vendas), retornando qual o mês teve menos vendas.
arquivo_vendas = 'lista2/vendas.csv'

try:
    with open(arquivo_vendas, 'r', newline='', encoding='utf-8') as arquivo_csv:
        data = read_csv("lista2/vendas.csv")
        vendas = data['VENDAS'].tolist()
        mes = data['MES'].tolist()

        for i in range(len(vendas)):
          if vendas[i] == min(vendas):
              print(f'O mês com menos vendas foi {mes[i]}.')
except FileNotFoundError:
    print(f'O arquivo CSV "{arquivo_vendas}" não foi encontrado.')
except Exception as e:
    print(f"Ocorreu um erro: {e}")

#Crie um algoritmo para ler dados de um CSV (que possui o nome de vendedores e
#o valor de cada venda realizada), retornando qual a soma de vendas que teve cada vendedor. 
def calcular_soma_vendas(vendedores):
    vendas_por_vendedor = {}

    with open(vendedores, 'r', encoding='utf-8') as arquivo_csv:
        data = read_csv(vendedores)
        valor = data['VALOR_VENDA'].tolist()
        vendedor = data['NOME_VENDEDOR'].tolist()

        for i in range(len(valor)):
            if vendedor[i] in vendas_por_vendedor:
                vendas_por_vendedor[vendedor[i]] += valor[i]
            else:
                vendas_por_vendedor[vendedor[i]] = valor[i]

    return vendas_por_vendedor

vendedores_csv = 'lista2/vendedores.csv' 
print(calcular_soma_vendas(vendedores_csv))

#Crie um algoritmo para ler dados de um CSV (que possui o nome de vendedores e
#o valor de cada venda realizada), retornando qual o vendedor que mais vendeu e o que menos vendeu.
def calcular_soma_vendas(vendedores):
    vendas_por_vendedor = {}

    with open(vendedores, 'r', encoding='utf-8') as arquivo_csv:
        data = read_csv(vendedores)
        valor = data['VALOR_VENDA'].tolist()
        vendedor = data['NOME_VENDEDOR'].tolist()

        for i in range(len(valor)):
            if vendedor[i] in vendas_por_vendedor:
                vendas_por_vendedor[vendedor[i]] += valor[i]
            else:
                vendas_por_vendedor[vendedor[i]] = valor[i]

    print(f"O vendedor que mais vendeu foi {max(vendas_por_vendedor)}.")
    print(f"O vendedor que menos vendeu foi {min(vendas_por_vendedor)}.")

vendedores_csv = 'lista2/vendedores.csv' 
calcular_soma_vendas(vendedores_csv)