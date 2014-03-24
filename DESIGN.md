#Document of style and design

This document defines the patterns of style and design adopted and is divided into three parts: Python, CSS and JavaScript.

##Python
####Head
<pre><code># -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#
</code></pre>

####Comments
The comments will be described into language of programming language.
<pre><code># This is a simple comment.

# This comment occupies
# more than one line.
</code></pre>

####Indentation
Always use 4 spaces to indent.
<pre><code>if __name__ == '__main__':
    print 'Hello, world'
</code></pre>

Always indent.
<pre><code>if x > 5:
    if x == 7:
        print x
    else:
        print x + 1
</code></pre>

####Nomenclatures and Declarations
#####Méthods and Functions
Name of method/function into language of programming language, with initial into lowercase and, if it have more than one word, break with '_'. Arguments separated with one space after comma, following example.
<pre><code>def function_sum(num1, num2):
    # ...
</code></pre>

#####Classes
Class name will be into language of programming language, initial uppercase and, if it have more than one word, break with letter into uppercase in the beginning of the other word. Each class have to have the comment with a short description.

<pre><code>class ClassOne():

    """This class is only a example."""

    def method_x():
        # ...
</code></pre>

#####Variables
Variables will be with meaning name, into language of programming language, with initial into uppercase and, if it have more than one word, break with '_'. One space will be among the variable and the attribution/comparison signal, as well as among attribution/comparison and value to be attributed/compared.

<pre><code>cars_list = []
car.model = '208'</code></pre>

#####Tuples, Lists e Dictionaries
Tuples, lists and dictionaries will be described into following pattern:

<pre><code>tuple = (
    var_x,
    var_y,
    var_z,
)
</code></pre>

####Imports
The imports will be follow pattern:

1. Imports of the especific classes from the package (`from os import path`), ordered and separated each package.
2. Import from entire package (`import os`).

<pre><code>from django.template import RequestContext
from django.http import HttpResponse

from exception.validation_exceptions import *
from exception.internal_exceptions import *

import MySQLdb
</code></pre>
