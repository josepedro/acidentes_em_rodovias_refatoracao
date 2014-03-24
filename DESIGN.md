#Documento de Estilo e Design

Este documento define os padrões de estilo e design que deverão ser seguidos neste projeto. As especificações serão divididas em três partes: Python, CSS e JavaScript.

##Python
####Cabeçalho
<pre><code># -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#
</code></pre>

####Identação
Sempre utilizar 4 espaços para identar.
<pre><code>if __name__ == '__main__':
    print 'Hello, world'
</code></pre>

Identar sempre.
<pre><code>if x > 5:
    if x == 7:
        print x
    else:
        print x + 1
</code></pre>

####Nomenclaturas e Declarações
#####Métodos e Funções
Nome do método/função no idioma da linguagem, com inicial minúscula e, se possuir mais de uma palavra, separar com um '_'. Argumentos separados com um espaço após a vírgula, como no exemplo abaixo.
<pre><code>def function_sum(num1, num2):
    # ...
</code></pre>

#####Classes
Nome da classe no idioma da linguagem, inicial maiúscula e, se possuir mais de uma palavra, as suas letras iniciais devem ser maiúsculas também. Cada classe deve conter um comentário com uma breve descrição.

<pre><code>class ClassOne():
    """This class is only a example."""
    def method_x():
        # ...
</code></pre>

