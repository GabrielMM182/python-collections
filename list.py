idade1 = 39
idade2 = 30
idade3 = 27
idade4 = 18

print(idade1)
print(idade2)
print(idade3)
print(idade4)

idades = [39, 30, 27 , 18]

type(idades) # ver o type da list idades que no caso e int

len(idades) #tamanho da list idades

idades[2] #27

idades.append(15) #adiciona 15 no final
idades.remove(15) # remove o 17

idades.clear() #remove tudo da lista

4 in idades # verifica se 4 esta dentro da lista idades

if 60 in idades:
    idades.remove(60)
    print("idade  {} removida com sucesso".format(60))
else:
    print("idades {} nao contem na lista".format(60))

idades.insert(0, 1) # insere o valor 1 na primeira posição 0 

idades = [20, 39, 18]
idades.extend([24, 33]) # adiciona mais de um valor em uma lista 
idades

idades_ano_que_vem = []
for idade in idades:
    idades_ano_que_vem.append(idade +1) # vai adicionar +1 em cada valor de idades suando for 
idades_ano_que_vem

idades_ano = [(idade+1) for idade in idades] # mesma logica do codigo de cima so que mais resumido

[idade + 1 for idade in idades if idade > 21] # verifica se mesmo adicionando mais 1 a list idade vai ser maior que 21 

def proximo_ano(idade): 
  return idade+1 # função

[proximo_ano(idade) for idade in idades if idade > 21] # mesma logica do codigo de cima chamando a função proximo_ano

def faz_processamento_de_visualizacao(lista = None): # vai verificar se a lista esta None ate ela tiver não adicionar o vlaor 13 no final
  if lista == None:
     lista = list()
     print(len(lista))
     print(lista)
     lista.append(13)
