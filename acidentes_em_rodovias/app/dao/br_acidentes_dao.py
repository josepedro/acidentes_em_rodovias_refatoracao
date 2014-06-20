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
from .generico_dao import GenericoDAO

from app.models.br_acidentes import BRAcidentesAno


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

    def populate_queries(self, query_result):
        """ Populate the Queries

            @brief Local variable:

                query -
                    SQL instruction to query accidents from highways per year

                query_result -
                    Saves the results from the query

                last_br -
                    Saves the last type of accident listed, used for comparison

                br_name -
                    Highway's name

                br_accidents_year_list -
                    List of accidents per year

                brs_accidents_year -
                    A instance of BRAcidentesAno
        """

        last_br = ''
        br_accidents_year_list = []

        # Populate list of Queries
        for (br_name, amount_occurrences, year) in zip(
                query_result['br'].values(),
                query_result['quantidade_ocorrencias'].values(),
                query_result['ano'].values()
        ):
            br_name = br_name.decode('iso-8859-1').encode('utf8')

            if (last_br != br_name):
                brs_accidents_year = BRAcidentesAno()
                br_accidents_year_list.append(brs_accidents_year)
                brs_accidents_year.br = br_name
                last_br = br_name

            brs_accidents_year.ano_list.append(year)
            brs_accidents_year.quantidade_ocorrencias_list.append(
                amount_occurrences,
            )

        return br_accidents_year_list

    def acidentes_br_ano(self):
        """ Queries accidents by highways per year

            @brief Local variable:

                query -
                    SQL instruction to query accidents from highways per year

                query_result -
                    Saves the results from the query

                last_br -
                    Saves the last type of accident listed, used for comparison

                br_name -
                    Highway's name

                br_accidents_year_list -
                    List of accidents per year

                brs_accidents_year -
                    A instance of BRAcidentesAno



            @return A list of objects generated by the query
        """

        query = """SELECT bre.br, bre.quantidade_ocorrencias, bre.ano
                FROM estatisticas_br bre
                GROUP BY bre.ano, bre.br
                ORDER BY bre.br, bre.ano;"""

        query_result = self.executa_query(query)

        br_accidents_year_list = self.populate_queries(query_result)

        return br_accidents_year_list
