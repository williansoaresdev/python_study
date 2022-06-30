# Projeto que embarca o will_framework
# Willian Soares
# contact@williansoaresdev.com


# Importa o will_framework
from will_framework import will


# Instancia um objeto da classe principal do framework
will_tools = will.WillTools()


if (__name__ == "__main__"):
    # Bem vindo com a versão do framework
    print("Bem vindo, will_framework versao", will.will_framework_version())
    # Status da instancia, para checar que o objeto foi criado adequadamente
    print("WillTools Status:", will_tools.get_status())