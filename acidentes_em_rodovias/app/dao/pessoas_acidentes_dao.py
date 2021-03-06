# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#

"""@package Pessoa Acidentes DAO
Data Access Object (DAO) for people in accidents on highway

This module contains the class declaration that
accesses the database relating people who have suffered accidents
in the bank and exports them to the controller.
"""

from .generico_dao import GenericoDAO


class PessoasAcidentesDAO(GenericoDAO):

    """Queries' accidents from highway and accidents by gender
    """

    def acidentes_por_sexo_e_ano(self, sexo):
        """ Queries accidents by gender and year

            @brief Local variable:

                query -
                    SQL instruction to query accidents from highways.

            @param sexo Gender to look for.
            @return A list of objects generated by the query.
        """
        query = """SELECT a.ano, a.sexo, a.quantidade
                FROM acidentes_por_sexo AS a
                WHERE a.sexo = '%s'
                ORDER BY a.ano;""" % (sexo)

        return self.transforma_dicionario_em_objetos(
            self.executa_query(query),
            "PessoasAcidentes",
            "pessoas_acidentes"
        )

    def acidentes_por_sexo_geral(self, sexo):
        """ Queries accidents by gender

            @brief Local variable:

                query -
                    SQL instruction to query accidents from highways.

            @param sexo Gender to look for.
            @return A list of objects generated by the query.
        """
        query = """SELECT a.sexo, SUM(a.quantidade) AS quantidade
                FROM acidentes_por_sexo AS a
                WHERE a.sexo = '%s'
                ORDER BY a.ano;""" % (sexo)

        return self.transforma_dicionario_em_objetos(
            self.executa_query(query),
            "PessoasAcidentesGeral",
            "pessoas_acidentes"
        )
