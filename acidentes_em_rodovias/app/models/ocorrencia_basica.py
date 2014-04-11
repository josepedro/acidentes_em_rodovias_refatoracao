# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#

"""@package Municipios
Declaração das classes para ocorrencias.

Este modulo contem declação da classe de modelo
para Ocorrencias basicas
"""


class OcorrenciaBasica:

    """ Basic Occurrences """

    def __init__(self):
        ## Occurrences' id table
        self.ocoid = ''
        ## Occurrences' date table
        self.ocodataocorrencia = ''
        ## Occurrences register's date table
        self.ocodataregistro = ''
        ## Denomination table
        self.tmudenominacao = ''
        ## UF table
        self.tmuuf = ''
        ## Comunication type table
        self.tcodescricao = ''
        ## Accident type table
        self.ttadescricao = ''
        ## Accident cause table
        self.tcadescricao = ''
        ## Local of hightway
        self.lbrbr = ''
        ## Vehicle's brand table
        self.tmvdescricao = ''
        ## Vehicle's table
        self.tvvdescricao = ''
