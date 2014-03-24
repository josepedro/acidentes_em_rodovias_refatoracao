# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#


class UFAcidentes():

    """ UF dos acidentes """

    def __init__(self):
        self.uf = ''
        self.quantidade_ocorrencias = ''
        self.latitude = 0.0
        self.longitude = 0.0


class UFAcidentesAno():

    """ UF dos acidentes separados por ano """

    def __init__(self):
        self.uf = ''
        self.quantidade_ocorrencias_list = []
        self.ano_list = []
