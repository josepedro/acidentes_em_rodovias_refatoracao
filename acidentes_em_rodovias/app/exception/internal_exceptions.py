# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#

"""@package internal exceptions
Exceções de validações internas.

Este modulo contem classes de controle de exceção
para validações internas
"""
from exceptions import Exception


class ResultadoConsultaNuloError(Exception):

    """docstring for ResultadoConsultaNuloError"""

    def __init__(self, message):
        """ Initialize module """
        Exception.__init__(self)
        self.message = message

    def __str__(self):
        """ How module shold be printed """
        return self.message
