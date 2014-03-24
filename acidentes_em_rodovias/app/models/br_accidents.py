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
        self.number_occurrences = ''
        self.br = ''


class BRAccidentsYear():

    """Accidents in general of Brazilian highways separated by year"""

    def __init__(self):
        self.number_occurrences_list = []
        self.br = ''
        self.year_list = []
