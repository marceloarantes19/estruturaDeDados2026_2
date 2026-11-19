from Elemento import Elemento
from NoABB import NoABB
class ArvoreBB:
  def __init__(self):
    self.__cabeca = None
  def getCabeca(self):
    return self.__cabeca 
  def arvoreVazia(self):
    return self.getCabeca() == None 
  def criaNo(self, chave = -1, nome = ""):
    return NoABB(Elemento(chave, nome))
  def inserir(self, chave, nome):
    no = self.criaNo(chave, nome)
    if self.arvoreVazia():
      self.__cabeca = no 
    else:
      self.insereNo(None, self.getCabeca(), no)
  def insereNo(self, pai, atual, no):
    #print("***** ", pai.getChave(), atual.getChave() if atual!=None else "none")
    if atual == None: # Insere o No na árvore
      if no.getChave() < pai.getChave():
        pai.setFe(no)
        print(pai.getFe().getValores())
      else:
        pai.setFd(no)
        print(pai.getFd().getValores())
    elif no.getChave() < atual.getChave():
      self.insereNo(atual, atual.getFe(), no)
    else:
      self.insereNo(atual, atual.getFd(), no)
  def preOrdem(self, no):
    if no!=None:
      print(no.getValores())
      self.preOrdem(no.getFe())
      self.preOrdem(no.getFd())
  def emOrdem(self, no):
    if no!=None:
      self.emOrdem(no.getFe())
      print(no.getValores()) 
      self.emOrdem(no.getFd())
  def posOrdem(self, no):
    if no!=None:
      self.posOrdem(no.getFe())
      self.posOrdem(no.getFd())
      print(no.getValores())
