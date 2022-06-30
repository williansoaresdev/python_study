# Framework para encapsular diversas rotinas nativas do python
# em classes próprias, permitindo assim fácil manutenção e evolução
# no futuro.


# Versão do framework controlada manualmente
will_version = '1.0.0';


# alguns status de controle interno
will_status_ready = 'Ready'


# will_framework_version():
# @return A versão armazenada em "will_version"
def will_framework_version():
    return will_version


# classe principal do framework
# agrega as demais classes e funcionalidades em
# uma única instância geral de controle
class WillTools:
    def __init__(self):
        # status de controle interno do objeto
        # inicia como "Pronto"
        self.__status = will_status_ready


    # will_tools.get_status():
    # retorna o status da instancia
    def get_status(self):
        return self.__status


    pass