from Elemento import Elemento
from NoDuplo import No
class ListaDE:
  def __init__(self):
    self.__cabeca = No()
  def criaNo(self, chave, nome):
    elemento = Elemento(chave, nome)
    no = No(elemento)
    return no
  def primeiro(self):
    return self.__cabeca.getAnte()
  def ultimo(self):
    return self.__cabeca.getProx()
  def listaVazia(self):
    return self.primeiro() == None
  def insereNoInicio(self, chave, nome):
    no = self.criaNo(chave, nome) 
    if self.listaVazia(): 
      self.__cabeca.setAnte(no)
      self.__cabeca.setProx(no) 
    else:
      no.setProx(self.primeiro())
      self.primeiro().setAnte(no)
      self.__cabeca.setAnte(no)
  def retiraNoInicio(self):
    no = self.primeiro()
    if not self.listaVazia():
      if no.getProx() == None:
        self.__cabeca.setAnte(None)
        self.__cabeca.setProx(None)
      self.__cabeca.setAnte(no.getProx())
      self.primeiro().setAnte(None)
      no.setProx(None)
    return no
  def insereNoFim(self, chave, nome):
    no = self.criaNo(chave, nome) 
    if self.listaVazia(): 
      self.__cabeca.setAnte(no)
      self.__cabeca.setProx(no) 
    else:
      no.setAnte(self.ultimo())
      self.ultimo().setProx(no)
      self.__cabeca.setProx(no)
  def retiraNoFim(self):
    no = self.ultimo()
    if not self.listaVazia():
      if no.getAnte() == None:
        self.__cabeca.setAnte(None)
        self.__cabeca.setProx(None)
      self.__cabeca.setProx(no.getAnte())
      self.ultimo().setProx(None)
      no.setAnte(None)
    return no
  
