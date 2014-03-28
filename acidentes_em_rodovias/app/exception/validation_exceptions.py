# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#

"""@package validation exceptions
Exceções de validação.

Este modulo contem classes de controle de exceção para validação
"""
from exceptions import Exception


class DataInvalidaError(Exception):

    """docstring for InvalidDateError"""

    def __init__(self, message):
        """ Initialize module """
        Exception.__init__(self)
        self.message = message

    def __str__(self):
        """ How module shold be printed """
        return self.message


class ParametroInseguroClienteError(Exception):

    """docstring for ParametroInseguroClienteError"""

    def __init__(self, message):
        """ Initialize module """
        Exception.__init__(self)
        self.message = message

    def __str__(self):
        """ How module shold be printed """
        return self.message
