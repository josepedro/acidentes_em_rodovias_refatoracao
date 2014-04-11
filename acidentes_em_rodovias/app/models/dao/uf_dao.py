# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#

"""@package UF DAO
Data Access Object (DAO) for Brazilian states.

This module contains the class declaration that accesses
data of Brazilian states in the database and exports them
to the controller
"""

from .generico_dao import GenericoDAO


class UfDAO(GenericoDAO):

    """Queries Brazilian states
    """

    def lista_ufs(self, limite=0):
        """ Queries Brazilian states

            @brief Local variable:

                query - 
                    SQL instruction to query brazilian states

            @param limite   Limits the query result. Default 0.
            @return List of Brazilian states
        """

        if(limite != 0):
            limite = 'LIMIT %s' % limite
        else:
            limite = ''
        query = """SELECT tufuf, tufdenominacao
                FROM uf ORDER BY tufdenominacao %s;""" % limite

        return self.transforma_dicionario_em_objetos(
            self.executa_query(query),
            "Uf",
            "uf"
        )
