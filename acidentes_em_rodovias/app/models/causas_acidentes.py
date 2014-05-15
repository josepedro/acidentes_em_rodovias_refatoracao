# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#

"""@package Modelo de acidentes
Declaração das classes para causas ou tipos de acidentes.

Este modulo contem declação das classes de modelo
para acidentes contendo o tipo ou causa
"""


class Acidentes(object):

    """ Causes of accidents """

    def __init__(self):
        ## Field to insert cause
        self.causa = ''
        ## Field to insert type
        self.tipo = ''
        ## Field to insert how many occurrences
        self.quantidade_ocorrencias = 0


class AcidentesAno(Acidentes):

    """ Separate causes of accidents per year """

    def __init__(self):
        ## Field to insert list with how many occurrences
        self.quantidade_ocorrencias_list = []
        ## Field to insert list of years
        self.ano_list = []


class ProbabilidadeAcidentes(Acidentes):

    """ Probability of causes of accidents """

    def __init__(self):
        ## Field to insert probability
        self.probabilidade_por_limite_list = []


class MediaDesvioAcidentes(Acidentes):

    """ Average and standard deviations of the causes of accidents """

    def __init__(self):
        ## Field to insert average
        self.media = 0.0
        ## Field to insert standard deviation
        self.desvio = 0.0
