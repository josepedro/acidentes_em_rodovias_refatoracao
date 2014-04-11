# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#

"""@package Model Persons accidents
Declaration of classes to persons involved in accidents.

This module contains the declaration of model classes
for persons involved in accidents.
"""


class PessoasAcidentes:

    """Model class for persons involved in accidents by year
    """

    def __init__(self):
        ## Field to insert year
        self.ano = ''
        ## Field to insert person's gender
        self.sexo = ''
        ## Field to insert how many occurrences
        self.quantidade = ''


class PessoasAcidentesGeral:

    """Model class for persons involved in accidents
    """

    def _init__(self):
        ## Field to insert person's gender
        self.sexo = ''
        ## Field to insert how many occurrences
        self.quantidade = ''
