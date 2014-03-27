# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#

"""@package Envolvidos em acidentes
Declaração das classes para envovlidos em acidentes.

Este modulo contem declação das classes de modelo
para modelos nos acidentes
"""


class EnvolvidosAcidente:

    """ Envolvidos em acidentes"""

    def __init__(self):
        self.quantidade_envolvidos = 0
        self.quantidade_acidentes = 0
        self.ano = 0
