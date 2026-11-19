from Elemento import Elemento
from NoABB import NoABB 
from ArvoreBB import ArvoreBB

arvore = ArvoreBB()
ch = int(input("Chave [-1 para sair]: "))
while ch != -1:
  nome = input("Nome: ")
  arvore.inserir(ch, nome)
  arvore.emOrdem(arvore.getCabeca())
  ch = int(input("Chave [-1 para sair]: "))
