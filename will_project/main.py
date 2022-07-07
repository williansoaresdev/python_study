# Projeto que embarca o will_framework
# Willian Soares
# contact@williansoaresdev.com


# Importa o will_framework
from will_framework import will


# Indica até quando o programa deve continuar sendo executado
continua_executando = True
# Tipos de menu possíveis
tipo_menu_principal = "principal"
tipo_menu_primario = "primario"
# Indica qual menu deve ser construído
menu_atual = tipo_menu_principal
# Tipos de respostas do aplicativo
respostas_sair = "S"
# Respostas do menu principal
resposta_menu_primario = "1"
resposta_apres_logs    = "3"
resposta_outros        = "8"
# Respostas para Manipulação de Dados primarios
respostas_strings = "1"
respostas_numeros = "2"
respostas_datas   = "3"


# Instancia um objeto da classe principal do framework
will_tools = will.WillTools()


# apresenta_logs():
# apresenta como usar o WillTools para gerar logs no console
# ou imprimir outras questões textuais
def apresenta_logs():
    print("[---> GERANDO LOGS]")
    print("---")
    print("# sempre imprime o texto no console")
    print("will_tools.logs.text(\"Testando\")")
    will_tools.logs.text("Testando")
    print("---")
    print("# imprime SOMENTE se log ativo:")
    print("will_tools.logs.log(\"Testando log\")")
    will_tools.logs.log("Testando log")
    print("---")
    print("# imprime com a data/hora:")
    print("will_tools.logs.dt_log(\"Testando log\")")
    will_tools.logs.dt_log("Testando log com a data/hora")


# apresenta_outros_comandos():
# apresenta outras utilidades básicas do framework
def apresenta_outros_comandos():
    print("[---> OUTROS COMANDOS]")
    print("---")
    print("# data e hora atual")
    print("will_tools.utils.date()")
    print("will_tools.utils.full_hour()")
    print("Hoje é {} {}".format(will_tools.utils.date(), will_tools.utils.full_hour()))


# boas_vindas():
# apenas imprime o texto de boas vindas e testa
# a versão e status do will_framework
def boas_vindas():
    # Bem vindo com a versão do framework
    will_tools.logs.text("Bem vindo, will_framework versao {}".format(will.will_framework_version()))
    # Status da instancia, para checar que o objeto foi criado adequadamente
    print("WillTools Status:", will_tools.get_status())


# imprime_menu():
# imprime o menu atual da aplicação
# pode ser o menu principal ou um menu específico
def imprime_menu():
    if menu_atual == tipo_menu_principal:
        menu_principal()
    elif menu_atual == tipo_menu_primario:
        menu_primario()
    else:
        print("Menu nao identificado.")


# manipula_datas():
# Apresenta como usar o willframework para manipular datas
def manipula_datas():
    print("Em desenvolvimento...")


# manipula_numeros():
# Apresenta como usar o willframework para manipular números
def manipula_numeros():
    print("Em desenvolvimento...")


# manipula_strings():
# Apresenta como usar o willframework para manipular strings
def manipula_strings():
    print("Em desenvolvimento...")


# menu_primario():
# imprime o menu de opções de dados primários que podem ser
# verificados no willframework
def menu_primario():
    print("---------------------------------------------")
    print("Escolha uma opcao para verificar:")
    print("1) Manipulacao de Strings")
    print("2) Manipulacao de Numeros")
    print("3) Manipulacao de Datas")
    print("---------------------------------------------")
    print("S) Voltar para o menu principal.")


# menu_principal():
# imprime o menu de opções de itens que podem ser
# verificados no willframework
def menu_principal():
    print("---------------------------------------------")
    print("Escolha uma opcao para verificar:")
    print("1) Dados primarios (str, num, data)")
    print("2) Arquivos de Texto, JSON ou XML")
    print("3) Logs e observabilidade")
    print("4) Consumo de APIs")
    print("5) Consumo de Bases de Dados")
    print("6) Envio de Email")
    print("8) Outros comandos")
    print("---------------------------------------------")
    print("S) Para sair.")


# processa_resposta_menu_primario():
# verifica se o menu foi corretamente respondido e da
# o prosseguimento na rotina solicitada
def processa_resposta_menu_primario(resposta):
    # Já verifica se o usuário quer voltar para o menu princpal
    if resposta == respostas_sair:
        global menu_atual
        menu_atual = tipo_menu_principal
    else:
        print("Resposta invalida.")

    return True


# processa_resposta_menu_princpal():
# verifica se o menu foi corretamente respondido e da
# o prosseguimento na rotina solicitada
def processa_resposta_menu_princpal(resposta):
    # Já verifica se o usuário quer sair da aplicação
    if resposta == respostas_sair:
        return False
    # Outras respostas...
    elif resposta == resposta_menu_primario:
        global menu_atual
        menu_atual = tipo_menu_primario
    elif resposta == resposta_apres_logs:
        apresenta_logs()
    elif resposta == resposta_outros:
        apresenta_outros_comandos()
#    elif resposta == respostas_strings:
#        manipula_strings()
#    elif resposta == respostas_numeros:
#        manipula_numeros()
#    elif resposta == respostas_datas:
#        manipula_datas()
    else:
        print("Resposta invalida.")

    return True


# processa_resposta():
# verifica se o menu foi corretamente respondido e da
# o prosseguimento na rotina solicitada
def processa_resposta(resposta):
    # Testa as respostas no maiusculo
    resposta = resposta.upper()
    # checa qual resposta deve ser processada
    if menu_atual == tipo_menu_principal:
        return processa_resposta_menu_princpal(resposta)
    elif menu_atual == tipo_menu_primario:
        return processa_resposta_menu_primario(resposta)
    else:
        return False


if (__name__ == "__main__"):
    # apresenta as boas vindas e testa a versão do framework
    boas_vindas()

    # apresenta o menu de opções enquanto o programa estiver rodando
    while continua_executando:
        imprime_menu()
        resposta = input("Resposta: ")
        # executa até que o usuário decida sair da aplicação:
        if not processa_resposta(resposta):
            continua_executando = False