# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#

"""@package Model Accident
Declaration of classes for accidents.

This module contains the declaration of model classes
for accidents in BRs
"""


class BR(object):

    """Basic class for BRs"""

    ## Field for insert highway's name
    br = ''


class BRAcidentes(BR):

    """Model class for accidents by BR
    """

    def __init__(self):
        ## Field to insert how many occurrences
        self.quantidade_ocorrencias = ''
        ## Field for insert highway's name


class BRAcidentesAno(BR):

    """Model class for accidents by BR and year
    """
    def __init__(self):
        ## Field to insert list with how many occurrences
        self.quantidade_ocorrencias_list = []
        ## Field to insert list with years
        self.ano_list = []
