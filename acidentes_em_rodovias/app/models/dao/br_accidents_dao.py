# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#

from generico_dao import GenericoDAO

from models.br_accidents import *

import sys
import os
import inspect

# Add upper directories
current_path = os.path.dirname(os.path.abspath('..'))
sys.path.append(current_path)
current_path = os.path.dirname(os.path.abspath('.'))
sys.path.append(current_path)


class BRAccidentsDAO(GenericoDAO):

    """BR Accidents Data Access"""

    def general_accidents(self):
        general_accidents_sql = """SELECT bre.br,
            SUM(bre.quantidade_ocorrencias)
            AS quantidade_ocorrencias
            FROM estatisticas_br bre
            GROUP BY bre.br
            ORDER BY bre.quantidade_ocorrencias DESC
            LIMIT 10;"""

        return self.transforma_dicionario_em_objetos(
            self.executa_query(general_accidents_sql),
            'BRAccidents',
            'br_accidents')

    def general_accidents_year(self):
        general_accidents_year_sql = """SELECT bre.br,
                bre.quantidade_ocorrencias, bre.ano
            FROM estatisticas_br bre
            GROUP BY bre.ano, bre.br
            ORDER BY bre.br, bre.ano;"""

        general_accidents_year = self.executa_query(general_accidents_year)

        br_accidents_year = []
        last_br = ''
        for (br, number_occurrences, year) in zip(
            general_accidents_year['br'].values(),
            general_accidents_year['quantidade_ocorrencias'].values(),
            general_accidents_year['ano'].values()
        ):

            br = br.decode('iso-8859-1').encode('utf8')

            if (last_br != br):
                brs_accidents_year = BRAccidentsYear()
                br_accidents_year.append(brs_accidents_year)
                brs_accidents_year.br = br
                last_br = br
            brs_accidents_year.year_list.append(year)
            brs_accidents_year.number_occurrences_list.append(
                number_occurrences
            )

        return br_accidents_year
