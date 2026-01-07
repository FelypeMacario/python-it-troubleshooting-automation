# Felype Fogo Macario Data:07/01/2026
#Automatização de Troubleshooting
# Buscando a melhora e eficiência do atendimento, este programa foi criado para automatizar
# e ajudar na causa raiz, até sua solução.




aut = input("Necessita de ajuda? (sim/nao): ").lower()

if aut == "sim":
    print("Selecione o ramo do incidente:")

    print("1- Impressora")
    print("2- Internet")
    print("3- Email")
    print("4- Computador")

    opcao = input("Digite o número do incidente: ")

    if opcao == "1":
        print("Iniciando Troubleshooting de Impressora.")
        resp =""
        while resp != "sim" and resp != "nao":
            resp = input("A impressora liga? sim/nao: ").lower()
            if resp == "nao":
                print("Verifique os cabos de energia: ")
            else:
                print("Prosseguir com Diagnóstico")

    elif opcao == "2":
        print("Iniciando Troubleshooting de Internet.")
        resp =""
        while resp != "sim" and resp != "nao":
            resp = input("O computador está com o gateway correto? sim/nao: ").lower()
            if resp == "nao":
                print("Verifique as configrações de rede IPv4: ")
            else:
                print("Prosseguir com Diagnóstico")

    elif opcao == "3":
        print("Iniciando Troubleshooting de Email.")
        resp =""
        while resp != "sim" and resp != "nao":
            resp = input("A impressora liga? sim/nao: ").lower()
            if resp == "nao":
                print("Verifique os cabos de energia: ")
            else:
                print("Prosseguir com Diagnóstico")


    elif opcao == "4":
        print("Iniciando Troubleshooting de Computador.")
        resp =""
        while resp != "sim" and resp != "nao":
            resp = input("O computador liga?: ").lower()
            if resp == "nao":
                print("Verifique os cabos de energia: ")
            else:
                print("Prosseguir com Diagnóstico")

    else:
        print("Opção inválida.")

elif aut == "nao":
    print("Atendimento finalizado")

else:
    print("Não entendi, digite novamente.")
