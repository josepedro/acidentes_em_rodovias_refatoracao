# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#

"""@package BR Acidentes DAO
Data Access Object (DAO) for accidents in highway

This module contains the class declaration that
accesses the database relating to highway accidents
in the bank and exports them to the controller.
"""


import sys
import os
import inspect

from .generico_dao import GenericoDAO

from app.models.br_acidentes import *


class BRAcidentesDAO(GenericoDAO):

    """Queries' accidents from highway and accidents by highway per year
    """

    def acidentes_br_geral(self):
        """ Queries accidents from highways

            @brief Local variable:

                query -
                    SQL instruction to query accidents from highways

            @return A list of objects generated by the query
        """
        query = """SELECT bre.br, SUM(bre.quantidade_ocorrencias)
                AS quantidade_ocorrencias
                FROM estatisticas_br bre
                GROUP BY bre.br
                ORDER BY bre.quantidade_ocorrencias DESC
                LIMIT 10;"""

        return self.transforma_dicionario_em_objetos(
            self.executa_query(query),
            'BRAcidentes',
            'br_acidentes'
        )

    def acidentes_br_ano(self):
        """ Queries accidents by highways per year

            @brief Local variable:

                query -
                    SQL instruction to query accidents from highways per year

                resultado_query -
                    Saves the results from the query

                ultima_br -
                    Saves the last type of accident listed, used for comparison

                br -
                    Highway's name

                br_acidentes_ano_list -
                    List of accidents per year

                brs_acidentes_ano -
                    A instance of BRAcidentesAno



            @return A list of objects generated by the query
        """

        query = """SELECT bre.br, bre.quantidade_ocorrencias, bre.ano
                FROM estatisticas_br bre
                GROUP BY bre.ano, bre.br
                ORDER BY bre.br, bre.ano;"""

        resultado_query = self.executa_query(query)

        br_acidentes_ano_list = []
        ultima_br = ''
        for (br, quantidade_ocorrencias, ano) in zip(
                resultado_query['br'].values(),
                resultado_query['quantidade_ocorrencias'].values(),
                resultado_query['ano'].values()
        ):
            br = br.decode('iso-8859-1').encode('utf8')

            if (ultima_br != br):
                brs_acidentes_ano = BRAcidentesAno()
                br_acidentes_ano_list.append(brs_acidentes_ano)
                brs_acidentes_ano.br = br
                ultima_br = br

            brs_acidentes_ano.ano_list.append(ano)
            brs_acidentes_ano.quantidade_ocorrencias_list.append(
                quantidade_ocorrencias,
            )

        return br_acidentes_ano_list
