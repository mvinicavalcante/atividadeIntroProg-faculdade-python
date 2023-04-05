from Atleta import *
from Time import *

flamengo = Time("Flamengo")

atleta1 = Atleta("Marcos", 19)
atleta2 = Atleta("Edielson", 20)
atleta3 = Atleta("Pedro", 20)
atleta4 = Atleta("Jardel", 22)
print(atleta1.getAllInfos())

flamengo.adicionarAtleta(atleta1)
flamengo.adicionarAtleta(atleta2)
flamengo.adicionarAtleta(atleta3)
flamengo.adicionarAtleta(atleta4)

flamengo.getInfos()

