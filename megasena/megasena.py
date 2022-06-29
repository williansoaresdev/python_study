import random

# apresentacao()
# Da a mensagem de boas vindas e cria o menu principal da aplicação
def apresentacao():
    print("# ------------------------------------------------------------ #")
    print("#                                                              #")
    print("#      Bem vindo ao gerador de numeros para Mega Sena          #")
    print("#                                                              #")
    print("# ------------------------------------------------------------ #")
    print("#                                                              #")
    print("#  Você pode gerar de 6 à 15 dezenas para seu jogo e se tornar #")
    print("#  o mais novo milionário do país. Vamos nessa?                #")
    print("#                                                              #")
    print("#  Opções:                                                     #")
    print("#  - Informe o número de dezenas desejado de 6 à 15;           #")
    print("#  - Ou 's' para sair.                                         #")
    print("#                                                              #")
    print("# ------------------------------------------------------------ #")


# usuario_quer_continuar_jogando():
# checa se o usuário quer continuar jogando
# para SAIR, as respostas válidas são: "s" ou "S"
def usuario_quer_continuar_jogando(resposta_usuario):
    return ((resposta_usuario != "s") and (resposta_usuario != "S"))


# gera_dezenas():
# gera as dezenas para o jogo na quantidade desejada
def gera_dezenas(quantidade_dezenas):
    print("")
    print("---> Gerando jogo de {} dezenas:".format(quantidade_dezenas))
    print("")
    # prepara os numeros do jogo
    str_jogos = ""
    feitos = 0
    while feitos < quantidade_dezenas:
        dezena = "{:02d}".format(random.randrange(1, 60))
        if str_jogos.find(dezena) < 0:
            if str_jogos != "":
                str_jogos = str_jogos + " - "
            str_jogos = str_jogos + dezena
            feitos = (feitos + 1)

    # imprime a sequencia
    print("---> " + str_jogos)
    print("")
    input("Pressione ENTER para continuar.")


# processa_resposta_usuario():
# Processa a resposta do usuário, e se for número de 6 a 15
# gera as devidas dezenas, se for S ou s não processará nada pois irá sair
# se for outra coisa, avisa que a resposta foi inválida.
def processa_resposta_usuario(resposta_usuario):
    # não precisa fazer nada se for para sair:
    if (resposta_usuario == "s") or (resposta_usuario == "S"):
        return

    # para controlar as validações
    prosseguir = True

    # checa se é mesmo um número que preencheu
    if not resposta_usuario.isnumeric():
        prosseguir = False

    # checa se é número de 6 a 15
    if prosseguir:
        resposta_dezenas = int(resposta_usuario)
        if (resposta_dezenas < 6) or (resposta_dezenas > 15):
            prosseguir = False

    if prosseguir:
        gera_dezenas(resposta_dezenas)
    else:
        input("---- Ops! RESPOSTA INVÁLIDA. Pressione ENTER para continuar ---- ")


# runProgram()
# Programa principal, se apresenta e  e segue mostrando
# as opções para o usuário, continua permitindo novos
# games até que o usuário decida sair.
def run_program():
    # String para controle das respostas do usuário
    resposta_usuario = ""
    # enquanto o usuário não desejar sair da aplicação:
    while usuario_quer_continuar_jogando(resposta_usuario):
        # se apresenta ao usuário
        apresentacao()
        # solicita uma reposta
        resposta_usuario = input("Qual sua resposta? --> ")
        # valida a resposta e apresenta as dezenas
        processa_resposta_usuario(resposta_usuario)


# Executa o programa principal:
run_program()