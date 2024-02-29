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
  split_frase = len(frase.split(""))
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


#Crie uma função que embaralhe os elementos de uma lista de forma aleatória.

#Escreva um programa que encontre o par de elementos em uma lista cuja soma seja igual a um determinado valor.

#Criar um algoritmo para calcular a frequência que uma palavra aparece em um texto.

#Escreva um programa que identifique todos os números primos em uma lista de números inteiros.

#Implemente um algoritmo para encontrar a menor string em uma lista de strings.

#Crie um algoritmo para ler um arquivo texto

#Crie um algoritmo para ler um arquivo CSV

#Crie um algoritmo para ler um arquivo JSON.

#Crie um algoritmo para consolidar um ou mais arquivos de texto de um diretório.

#Crie um algoritmo para ler dados de um CSV (que possui os meses e valores de vendas), retornando qual o mês teve mais vendas.

#Crie um algoritmo para ler dados de um CSV (que possui os meses e valores de vendas), retornando qual o mês teve menos vendas.

#Crie um algoritmo para ler dados de um CSV (que possui o nome de vendedores e
#o valor de cada venda realizada), retornando qual a soma de vendas que teve cada vendedor. 


#Crie um algoritmo para ler dados de um CSV (que possui o nome de vendedores e
#o valor de cada venda realizada), retornando qual o vendedor que mais vendeu e o que menos vendeu.
