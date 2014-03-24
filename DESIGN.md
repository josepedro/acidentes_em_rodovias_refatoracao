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

####Comentários
Os comentários devem ser escritos no idioma da linguagem.
<pre><code># This is a simple comment.

# This comment occupies
# more than one line.
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

#####Variáveis
Variáveis com nome significativo, no idioma da linguagem, com inicial minúscla e, se possuir mais de uma palavra, separar com um '_'. Deve existir um espaço entre a variável e o sinal de atribuição/comparação, bem como entre o sinal de atribuição/comparação e o valor a ser atribuído/comparado.

<pre><code>cars_list = []
car.model = '208'</code></pre>

#####Tuplas, Listas e Dicionários
Tuplas, Listas e Dicionários devem ser descritos da seguinte forma:

<pre><code>tuple = (
    var_x,
    var_y,
    var_z,
)
</code></pre>

####Imports
Os imports devem seguir a seguinte ordem:

1. Imports de classes específicas de um pacote (`from os import path`), ordenados e separados por pacote.
2. Import de pacotes inteiros (`import os`).

<pre><code>from django.template import RequestContext
from django.http import HttpResponse

from exception.validation_exceptions import *
from exception.internal_exceptions import *

import MySQLdb
</code></pre>
