# will_framework

Framwork que encapsula rotinas nativas do python em uma classe própria para melhor manutenção e evolução de código no futuro.

### Instalação
Copie a pasta will_framework para a raíz de seu projeto, então para importar bastará:

    from will_framework import will

### Para checar a versão em utilização:

    will_framework_version()


### Instancia um objeto da classe principal do framework

    will_tools = will.WillTools()

### Checa o status da instancia

    # esperado 'Ready'
    will_tools.get_status()

