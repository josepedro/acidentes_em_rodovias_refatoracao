# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#

"""@package UF
Declaração das classes para UF dos estados.

Este modulo contem declação da classe de modelo
para as UF de os estados.
"""


class Uf:

    """ States' UF """

    def __init__(self):
    	## Field to insert states' abreviation
        self.uf = ''
        ## Abbreviation of the Federal City
        self.tufuf = ''
        ## Denomination of the Federal City
        self.tufdenominacao = ''
