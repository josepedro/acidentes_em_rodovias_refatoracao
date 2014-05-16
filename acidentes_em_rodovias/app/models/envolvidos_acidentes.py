# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#

"""@package Model Involved in Accidents
Declaration of classes to involved in accidents.

This module contains the declaration of model classes
for involved in accidents.
"""

from app.models.pessoas_acidentes import PessoasAcidentes

class EnvolvidosAcidente(PessoasAcidentes):

    """Model class for involved in accidents
    """

    def __init__(self):
        ## Field to insert how many involved
        self.quantidade_envolvidos = 0
        ## Field to insert how many occurrences
        self.quantidade_acidentes = 0