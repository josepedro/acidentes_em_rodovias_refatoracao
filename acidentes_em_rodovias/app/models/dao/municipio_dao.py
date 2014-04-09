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

from generico_dao import GenericoDAO


class MunicipioDAO(GenericoDAO):

    """Queries the Brazilian municipalities
    """

    def lista_municipios(self, uf, limite=0):
        """ Queries the Brazilian municipalities

            @brief Local variable:

                query -
                    SQL instruction to query the municipalities of a state

            @param uf Abreviation of the state's name
            @param limite Limits the query. Default 0.

            @return List of Brazilian municipalities
        """
        if(limite != 0):
            limite = 'LIMIT %s' % limite
        else:
            limite = ''

        query = """SELECT DISTINCT tmucodigo, tmudenominacao, tmuuf
                FROM municipio tmu
                INNER JOIN ocorrencia oco ON oco.ocomunicipio = tmu.tmucodigo
                WHERE tmu.tmuuf = '%s'
                ORDER BY tmudenominacao %s; """ % (uf, limite)

        return self.transforma_dicionario_em_objetos(
            self.executa_query(query),
            "Municipio",
            "municipio"
        )
