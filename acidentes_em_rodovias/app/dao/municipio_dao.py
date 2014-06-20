# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#

"""@package Municipio DAO
Data Access Object (DAO) for Brazilian municipalities

This module contains the class declaration that
accesses the database relating Brazilian municipalities
in the bank and exports them to the controller.
"""

from app.dao.generico_dao import GenericoDAO


class MunicipioDAO(GenericoDAO):

    """Queries the Brazilian municipalities
    """

    def lista_municipios(self, uf, limite=0):
        """ Queries the Brazilian municipalities

            @brief Local variable:

                select_sql -
                    SQL instruction to query the municipalities of a state
                result_select_sql -
                    Result of select query
                county_list -
                    list of counties

            @param uf Abreviation of the state's name
            @param limite Limits the query. Default 0.

            @return List of Brazilian municipalities
        """
        if(limite != 0):
            limite = 'LIMIT %s' % limite
        else:
            limite = ''

        select_sql = """SELECT DISTINCT tmucodigo, tmudenominacao, tmuuf
                FROM municipio tmu
                INNER JOIN ocorrencia oco ON oco.ocomunicipio = tmu.tmucodigo
                WHERE tmu.tmuuf = '%s'
                ORDER BY tmudenominacao %s; """ % (uf, limite)

        result_select_sql = self.executa_query(select_sql)
        county_list = self.transforma_dicionario_em_objetos(
            result_select_sql,
            "Municipio",
            "municipio"
        )

        return county_list
