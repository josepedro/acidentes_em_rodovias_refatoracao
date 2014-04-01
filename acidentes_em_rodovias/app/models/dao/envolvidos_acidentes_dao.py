# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#

"""@package Envolvidos Acidentes DAO
Data Access Object (DAO) para causa de acidentes nas BRs.

Este modulo contem declação da classe que acessa os
dados no banco e os exporta para a controller
"""

import sys
import os
import inspect

from .generico_dao import GenericoDAO

from models.envolvidos_acidentes import *

from util.estatisticas_util import *


class EnvolvidosAcidentesDAO(GenericoDAO):

    """Envolvidos em Acidentes DAO"""

    def envolvidos_acidentes(self):
        query = """SELECT
                    `quantidade_envolvidos`, `quantidade_acidentes`, `ano`
                FROM `estatisticas_envolvido`;"""

        return self.transforma_dicionario_em_objetos(
            self.executa_query(query),
            "EnvolvidosAcidente",
            "envolvidos_acidentes"
        )

    def media_desvio_envolvidos(self):
        lista_envolvidos = self.envolvidos_acidentes()

        lista_medias = []
        for envolvido in lista_envolvidos:
            envolvidos = float(envolvido.quantidade_envolvidos)
            acidentes = float(envolvido.quantidade_acidentes)
            media = envolvidos / acidentes
            lista_medias.append(media)

        desvio = desvio_padrao(
            lista_medias
        )

        return lista_medias, desvio
