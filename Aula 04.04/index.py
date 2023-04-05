x = 1

listaDeContas = []

while(x == 1) :
    
    def cadastrar(): 
        conta = {}
        conta['numero'] = input("Digite o número\n")
        conta['saldo'] = int(input("Digite o saldo\n"))
        conta['titular'] = input("Digite o nome\n")

        for c in listaDeContas:
            if c['titular'] == conta['titular']:
                if c['numero'] == conta['numero']:
                    print("Conta já cadastrada para este titular.")
                    return

        listaDeContas.append(conta)
        print(listaDeContas)


    def exibirPorNumero(numero):
        for x in listaDeContas:
           if(x['numero'] == numero):
            print(x)

    def pessoaMaisRica():
        saldosPorTitular = {}
        for conta in listaDeContas:
            titular = conta['titular']
            saldo = conta['saldo']
            if titular not in saldosPorTitular:
                saldosPorTitular[titular] = saldo
            else:
                saldosPorTitular[titular] += saldo

        titularMaisRico = max(saldosPorTitular, key=saldosPorTitular.get)
        saldoMaisRico = saldosPorTitular[titularMaisRico]
        print(f"Titular mais rico: {titularMaisRico} (saldo total de {saldoMaisRico})")



    acao = input("Digite: \n1 para cadastrar\n2 para exibir por número\n3 para exibir a pessoa mais rica\n4 para parar o sistema\n")

    if(acao == "1") :
        cadastrar()
    elif(acao == "2"):
        numero = input("Digite o número:\n")
        exibirPorNumero(numero)
    elif(acao == "3"):
        pessoaMaisRica()
    elif(acao == "4"):
        x = 0
    else: print("Comando errado")