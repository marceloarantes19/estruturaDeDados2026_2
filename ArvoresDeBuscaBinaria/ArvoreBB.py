from Elemento import Elemento
from NoABB import NoABB
class ArvoreBB:
  def __init__(self):
    self.__raiz = None
  def getRaiz(self):
    return self.__raiz 
  def arvoreVazia(self):
    return self.getRaiz() == None 
  def eRaiz(self, no):
    return no == self.getRaiz()
  def criaNo(self, chave = -1, nome = ""):
    return NoABB(Elemento(chave, nome))
  def inserir(self, chave, nome):
    no = self.criaNo(chave, nome)
    if self.arvoreVazia():
      self.__raiz = no 
    else:
      self.insereNo(None, self.getRaiz(), no)
  def insereNo(self, pai, atual, no):
    if atual == None: # Insere o No na árvore
      if no.getChave() < pai.getChave():
        pai.setFe(no)
      else:
        pai.setFd(no)
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
  def remover(self, chave):
    ret = None
    if not self.arvoreVazia():
      ret = self.removeNo(None, self.getRaiz(), chave)
    return ret
  def removeNo(self, pai, atual, chave):
    ret = None
    if atual == None: # O nó não foi encontrado
      ret = None
    elif chave < atual.getChave(): # o nó a ser removido está na subárvore esquerda
      ret = self.removeNo(atual, atual.getFe(), chave)
    elif chave > atual.getChave(): # o nó a ser removido está na subárvore direita
      ret = self.removeNo(atual, atual.getFd(), chave)
    else: # o nó a ser removido é o atual
      # CASOS TRIVIAIS FOLHAS E NÓS COM UM FILHO
      ret = atual 
      if atual.eFolha(): # o nó a ser removido é uma folha
        if self.eRaiz(atual):
          self.__raiz = None
        elif atual.eFe(pai):
          pai.setFe(None)
        else:
          pai.setFd(None)
      elif atual.soTemFe(): # o nó a ser removido só tem filho à esquerda
        if self.eRaiz(atual):
          self.__raiz = atual.getFe()
        elif atual.eFe(pai):
          pai.setFe(atual.getFe())
        else:
          pai.setFd(atual.getFe())
        atual.setFe(None)
      elif atual.soTemFd(): # o nó a ser removido só tem filho à direita
        if self.eRaiz(atual):
          self.__raiz = atual.getFd()
        elif atual.eFe(pai):
          pai.setFe(atual.getFd())
        else:
          pai.setFd(atual.getFd())
        atual.setFd(None)
      else: # o nó a ser removido tem dois filhos
        antescessor = self.getAntescessor(atual.getFe())
        valores = antescessor.getValores()
        ret = self.removeNo(atual, atual.getFe(), antescessor.getChave())
        atual.setDado(antescessor.getDado())
        ret.setValores(valores)
    return ret
  def getAntescessor(self, atual):
    if atual.getFd() != None:
      return self.getAntescessor(atual.getFd())
    else:
      return atual