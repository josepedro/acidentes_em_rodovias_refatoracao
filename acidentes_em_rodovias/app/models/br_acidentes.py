# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#


class BRAccidents():

    """Accidents in general of Brazilian highways"""

    def __init__(self):
        self.number_occurrenses = ''
        self.br = ''


class BRAcidentesAno(object):

    """ Acidentes em geral das rodovias separados por ano"""

    def __init__(self):
        self.quantidade_ocorrencias_list = []
        self.br = ''
        self.ano_list = []
