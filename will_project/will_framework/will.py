# Framework para encapsular diversas rotinas nativas do python
# em classes próprias, permitindo assim fácil manutenção e evolução
# no futuro.


import datetime


# Versão do framework controlada manualmente
will_version = '1.0.1';


# alguns status de controle interno
will_status_ready = 'Ready'


# will_framework_version():
# @return A versão armazenada em "will_version"
def will_framework_version():
    return will_version


# classe para gerar logs das operacoes da aplicação
# como por exemplo o log por print("")
class WillLog:
    def __init__(self, owner):
        # indica se o log está ativo
        # se inativo, não irá jogar nenhum log no command
        self.__log_active = True
        # objeto pai (WillTools)
        self.__owner = owner


    # dt_log():
    # Imprime um texto no console desde que o log esteja ATIVO (__log_active)
    # Antecipado pela data hora do registro
    # @text: texto a ser impresso no console
    def dt_log(self, text):
        if self.__log_active:
            date = self.__owner.utils.date()
            hour = self.__owner.utils.full_hour()
            print("{} {} - {}".format(date, hour, text))


    # log():
    # Imprime um texto no console desde que o log esteja ATIVO (__log_active)
    # @text: texto a ser impresso no console
    def log(self, text):
        if self.__log_active:
            print(text)


    # text():
    # Imprime qualquer texto no console
    # Dica: este comando não respeita o __log_active, para isso, use o log()
    # @text: texto a ser impresso no console
    def text(self, text):
        print(text)


    pass


# classe WillUtils:
# agrega comandos simples que não precisam estar em
# uma classe própria
# se por acaso um conjunto de comandos começar
# a crescer demais, então ele pode ser encapsulado
# em uma classe
class WillUtils:
    # WillUtils.full_hour():
    # retorna a hora no formato hh:mm:ss
    def full_hour(self):
        now = datetime.datetime.now()
        return now.strftime("%H:%M:%S")


    # WillUtils.date():
    # retorna a data no formato dd/mm/yy
    def date(self):
        now = datetime.datetime.now()
        return now.strftime("%d/%m/%y")

    pass


# classe principal do framework
# agrega as demais classes e funcionalidades em
# uma única instância geral de controle
class WillTools:
    def __init__(self):
        # status de controle interno do objeto
        # inicia como "Pronto"
        self.__status = will_status_ready
        # ferramente de log do framework
        self.logs = WillLog(self)
        # utilidades gerais
        self.utils = WillUtils()


    # will_tools.get_status():
    # retorna o status da instancia
    def get_status(self):
        return self.__status


    pass