from Elemento import Elemento
class NoABB:
  def __init__(self, dado = Elemento()):
    self.__dado = dado
    self.__fe = None
    self.__fd = None
  def getDado(self):
    return self.__dado 
  def setDado(self, d = Elemento()):
    self.__dado = d 
  def getFe(self):
    return self.__fe 
  def setFe(self, fe = None):
    self.__fe = fe 
  def getFd(self):
    return self.__fd 
  def setFd(self, fd = None):
    self.__fd = fd 
  def eFolha(self):
    return self.__fe == None and self.__fd == None 
  def temFe(self):
    return self.__fe != None 
  def temFd(self):
    return self.__fd != None
  def eFe(self, pai):
    return pai != None and pai.getFe() == self 
  def eFd(self, pai):
    return pai != None and pai.getFd() == self
  def getChave(self):
    return self.getDado().getChave()
  def getValores(self):
    return self.getDado().getValores()
  def setValores(self, valores):
    self.getDado().setValores(valores)
  def soTemFe(self):
    return self.temFe() and not self.temFd()
  def soTemFd(self):
    return self.temFd() and not self.temFe()
  
  
  