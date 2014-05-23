# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#

import sys
import os
import inspect

from .generico_dao import GenericoDAO

from app.models.causas_acidentes import *

from app.util.estatisticas_util import *


class TiposAcidentesDAO(GenericoDAO):

    """Tipos de Acidentes DAO
    Executes and lists the accidents by type and per year.
    """

    def tipos_acidentes(self):
        """
        Queries the different types of accidents.

        @brief Local variable:
            query - 
                SQL instruction to query the total number of the different types of accidents.

        @return a list of objects generated by the query.
        """
        query = """SELECT tipo,
                    SUM(quantidade_ocorrencias) AS quantidade_ocorrencias
                FROM estatisticas_tipo
                GROUP BY  tipo
                ORDER BY quantidade_ocorrencias DESC; """

        return self.transforma_dicionario_em_objetos(
            self.executa_query(query),
            "Acidentes",
            "causas_acidentes"
        )

    def tipos_acidentes_ano(self):
        """
        Queries the number of accidents per year.
        @brief Local variables:
            query - 
                SQL instruction to query accidents per year.
            resultado_query - 
                Receives the query results.
            tipos_acidentes_ano_list -
                List of objects that will be returned.
            ultimo_tipo -
                saves the last type of accident that was queried.
            tipo - 
                Receives the type of accident from the query result.

        @return List of objects build by query results
        """
        query = """SELECT tipo, quantidade_ocorrencias, ano
                FROM estatisticas_tipo
                ORDER BY tipo, ano ; """

        resultado_query = self.executa_query(query)

        tipos_acidentes_ano_list = []
        ultimo_tipo = ''

        for (tipo, quantidade_ocorrencias, ano) in zip(
            resultado_query['tipo'].values(),
            resultado_query['quantidade_ocorrencias'].values(),
            resultado_query['ano'].values()
        ):
            tipo = tipo.decode('iso-8859-1').encode('utf8')
            if (ultimo_tipo != tipo):
                tipos_acidentes_ano = AcidentesAno()
                tipos_acidentes_ano_list.append(tipos_acidentes_ano)
                tipos_acidentes_ano.tipo = tipo
                ultimo_tipo = tipo

            tipos_acidentes_ano.ano_list.append(ano)
            tipos_acidentes_ano.quantidade_ocorrencias_list.append(
                quantidade_ocorrencias
            )

        return tipos_acidentes_ano_list

    def probabilidade_tipos_acidentes(self):
        """
        Calculates the probability of future accidents by type.

        @brief Local variables:
            query - 
                SQL instruction to query number of occurrences by type and year.
            data_frame - 
                Receives the query result in a predetermined format.
            medias_list -
                Takes the media of the number of occurrences by type and lists then.
            desvios_padroes_list -
                Lists the standard deviation of the number of occurrences by type.
            probabilidade_tipo_list -
                Lists the probability of a certain type of accident happening again.
            limites - 
                Limits the number of registers in the database.
            probabilidade_tipo - 
                Receives the result of probability per each accident's type.
            probabilidade_tipo.tipo -
                Receives a key to encode from iso-8859-1 to utf8
            inferior -
                Determines the lower limit for the operation
            superior -
                Determines the higher limit for the operation
            distribuicao_normal-
                Calculates the normal distribution of the probability

        @return List of probability by type.
        """
        query = """SELECT tipo, quantidade_ocorrencias, ano
                FROM estatisticas_tipo
                ORDER BY tipo, ano ; """

        data_frame = self.executa_query(query, get_data_frame=True)

        medias_list = data_frame.groupby(
            'tipo'
        )['quantidade_ocorrencias'].mean()
        desvios_padroes_list = data_frame.groupby(
            'tipo'
        )['quantidade_ocorrencias'].std()

        probabilidade_tipo_list = []

        for i in range(0, len(medias_list)):
            probabilidade_tipo = ProbabilidadeAcidentes()
            probabilidade_tipo.tipo = medias_list.keys()[
                i].decode('iso-8859-1').encode('utf8')

            limits_min_one = 0
            limits_max_one = 5000
            limits_min_two = 5001
            limits_max_two = 10000
            limits_min_three = 10001
            limits_max_three = 30000
            limits_min_four = 30001
            limits_max_four = 50000
            limits_min_five = 50001
            limites = [
                (limits_min_one, limits_max_one),
                (limits_min_two, limits_max_two),
                (limits_min_three, limits_max_three),
                (limits_min_four, limits_max_four),
                (limits_min_five, sys.maxsize)]


            normalization_in_percent = 100
            for (inferior, superior) in limites:
                if (medias_list[i] >= inferior and medias_list[i] <= superior):
                    probabilidade_tipo.probabilidade_por_limite_list.append(
                        normalization_in_percent * (
                            distribuicao_normal(
                                inferior,
                                medias_list[i],
                                desvios_padroes_list[i]
                            ) + distribuicao_normal(
                                superior,
                                medias_list[i],
                                desvios_padroes_list[i]
                            )
                        )
                    )
                elif (medias_list[i] >= inferior):
                    probabilidade_tipo.probabilidade_por_limite_list.append(
                        normalization_in_percent * (
                            distribuicao_normal(
                                inferior,
                                medias_list[i],
                                desvios_padroes_list[i]
                            ) - distribuicao_normal(
                                superior,
                                medias_list[i],
                                desvios_padroes_list[i]
                            )
                        )
                    )
                elif (medias_list[i] <= inferior):
                    probabilidade_tipo.probabilidade_por_limite_list.append(
                        normalization_in_percent * (
                            distribuicao_normal(
                                superior,
                                medias_list[i],
                                desvios_padroes_list[i]
                            ) - distribuicao_normal(
                                inferior,
                                medias_list[i],
                                desvios_padroes_list[i]
                            )
                        )
                    )

            probabilidade_tipo_list.append(
                probabilidade_tipo
            )

        return probabilidade_tipo_list

    def media_desvio_tipos_acidentes(self):
        """
        Calculates the average of the accidents types
        @brief Local variables:
            query - 
                SQL instruction to query the statistics per year.
            data_frame - 
                Receives the query result in a predetermined format.
            medias_list- 
                List of averages.
            desvios_padroes_list -
                List of standard deviations. 
            media_desvio_tipos_acidentes_list -
                Lists the average of the standard deviation for the different accidents type.

        @return List of the standard deviation's averages.
        """
        query = """SELECT tipo, quantidade_ocorrencias, ano
                FROM estatisticas_tipo
                ORDER BY tipo, ano ; """

        data_frame = self.executa_query(query, get_data_frame=True)

        medias_list = data_frame.groupby(
            'tipo'
        )['quantidade_ocorrencias'].mean()
        desvios_padroes_list = data_frame.groupby(
            'tipo'
        )['quantidade_ocorrencias'].std()

        media_desvio_tipos_acidentes_list = []

        for i in range(0, len(medias_list)):
            media_desvio_tipos_acidentes = MediaDesvioAcidentes()
            media_desvio_tipos_acidentes.media = medias_list[i]
            media_desvio_tipos_acidentes.desvio = desvios_padroes_list[i]

            media_desvio_tipos_acidentes_list.append(
                media_desvio_tipos_acidentes
            )

        return media_desvio_tipos_acidentes_list
