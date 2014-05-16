# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#

"""@package Model UF Accidents
Declaration of classes to accidents in Brazilian UF's

This module contains the declaration of model classes
for accidents in UF.
"""

from app.models.uf import Uf

class UFAcidentes(Uf):

    """Model class for involved in accidents
    """

    def __init__(self):
        ## Field to insert how many occurrences
        self.quantidade_ocorrencias = ''
        ## Field to insert states' latitude
        self.latitude = 0.0
        ## Field to insert states' longitude
        self.longitude = 0.0


class UFAcidentesAno(Uf):

    """Model class for involved in accidents by year
    """

    def __init__(self):
        ## Field to insert list with how many occurrences
        self.quantidade_ocorrencias_list = []
        ## Field to insert list with years
        self.ano_list = []
