# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#

"""@package Envolvidos Acidentes DAO
Data Access Object (DAO) for involved in accidents

This module contains the class declaration that
accesses the database relating to involved in
accidents in the bank and exports them to the controller.
"""

import sys
import os
import inspect

from .generico_dao import GenericoDAO

from models.envolvidos_acidentes import *

from util.estatisticas_util import *


class EnvolvidosAcidentesDAO(GenericoDAO):

    """Queries the number of involved and the number of accidents per year
    """

    def envolvidos_acidentes(self):
        """ Queries the number of involved in accidents

            @brief Local variable:

                query -
                    SQL instruction to query the number of involved in
                accidents

            @return List of objects with the number of involved in
            accidents
        """

        query = """SELECT
                    `quantidade_envolvidos`, `quantidade_acidentes`, `ano`
                FROM `estatisticas_envolvido`;"""

        return self.transforma_dicionario_em_objetos(
            self.executa_query(query),
            "EnvolvidosAcidente",
            "envolvidos_acidentes"
        )

    def media_desvio_envolvidos(self):
        """ Queries the number of involved in accidents per year

            @brief Local variable:

                lista_envolvidos -
                    List of involved in accidents per year

                lista_medias -
                    List of averages involved in accidents

                envolvidos -
                    Number of involved

                acidentes -
                    Number of accidents

                media -
                    Average of involved in accidents

                desvio -
                    Standard deviation

            @return List of objects with the number of involved in
            accidents
        """

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
