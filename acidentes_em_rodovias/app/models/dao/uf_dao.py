# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#

from generico_dao import GenericoDAO


class UfDAO(GenericoDAO):

    """UF DAO"""

    def lista_ufs(self, limite=0):
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
