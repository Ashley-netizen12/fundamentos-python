class Ropa:
    def __init__(self, polera, camisa, pantalon, falda, short, precio):
     
     self.__polera = polera
     self.__camisa = camisa
     self.__pantalon = pantalon
     self.__falda = falda 
     self.__short = short
     self.__precio = precio

    def get_polera (self):
        return self.__polera 
    
    def get_camisa(self):
     return self.__camisa

    def get_pantalon(self):
     return self.__pantalon     

    def get_falda(self):
      return self.__falda

    def get_short(self):
      return self.__short

    def get_precio(self):
        return self.__precio
    
    def set_polera(self, polera):
        self.__polera = polera

    def set_camisa(self, camisa):
     self.__camisa = camisa

    def set_pantalon(self, pantalon):
        self.__pantalon = pantalon

    def set_falda(self, falda):
        self.__falda = falda

    def set_short(self, short):
        self.__short = short

    def set_precio(self, precio):
        self.__precio = precio