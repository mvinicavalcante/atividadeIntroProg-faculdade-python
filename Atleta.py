class Atleta:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def setNome(self, newNome):
        self.nome = newNome

    def setIdade(self, newIdade):
        self.idade = newIdade
    
    def getAllInfos(self):
        return self.nome, self.idade
        
        
