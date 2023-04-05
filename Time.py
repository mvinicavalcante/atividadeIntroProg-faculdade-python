from Atleta import *

class Time:

    atletas = []

    def __init__(self, nome):
        self.nome = nome 
    
    def adicionarAtleta(self, atleta):
        self.atletas.append(atleta)
    
    def getInfos(self):
        print("Nome do time: ", self.nome)
        print("Atletas: ")
        for atleta in self.atletas:
            print("          -", atleta.nome)
        print("")