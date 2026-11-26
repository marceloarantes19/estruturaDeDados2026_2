from ArvoreBB import ArvoreBB, NoABB, Elemento  
lista = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
arvore = ArvoreBB()
for i in lista:
  arvore.inserir(i, "N - " + str(i))
ch = int(input("Digite a chave a ser removida [-1 para sair]: "))
while ch != -1:
  no = arvore.remover(ch)
  if no != None:
    print("No removido: ", no.getValores())
  else:
    print("No nao encontrado")
  arvore.emOrdem(arvore.getRaiz())
  ch = int(input("Digite a chave a ser removida [-1 para sair]: "))