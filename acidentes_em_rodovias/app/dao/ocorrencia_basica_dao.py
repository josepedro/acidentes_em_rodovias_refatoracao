# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#

from .generico_dao import GenericoDAO


class OcorrenciaBasicaDAO(GenericoDAO):

    """Ocorrência Básica DAO

    Executes and lists queries and transforms queries
    results in objects, by period and region.
    """

    def lista_ocorrencias_por_regiao(self, municipio_id, limite=0):
        """
        Executes and lists query results by region

        @brief Local variable:
            query -
                SQL instruction to query the occurrences per region.
            occurrences_by_region_SQL
                Receives the query execution
            list_of_ocurrences
                Receives the list of occurrences per period.

        @param municipio_id County's ID, returning the counties by each region
        selected.
        @param limite Limits the number of registers in the Database.
        @return Method that transforms the query results in a model object.
        """
        if limite != 0:
            limite = 'LIMIT %s' % limite
        else:
            limite = ''

        query = """SELECT oco.ocoid, oco.ocodataocorrencia,
                oco.ocodataregistro, tta.ttadescricao, lbr.lbrbr,
                tmu.tmudenominacao, tmu.tmuuf, tco.tcodescricao,
                tca.tcadescricao, tmv.tmvdescricao, tvv.tvvdescricao
                FROM ocorrencia oco
                INNER JOIN municipio tmu
                    ON  tmu.tmucodigo =  oco.ocomunicipio
                INNER JOIN tipoComunicacao tco
                    ON tco.tcocodigo = oco.ocotipo
                INNER JOIN localbr lbr
                    ON lbr.lbrid = oco.ocolocal
                INNER JOIN ocorrenciaacidente oac
                    ON oac.oacocoid = oco.ocoid
                INNER JOIN tipoAcidente tta
                    ON tta.ttacodigo = oac.oacttacodigo
                INNER JOIN causaacidente tca
                    ON tca.tcacodigo = oac.oactcacodigo
                INNER JOIN ocorrenciaveiculo ocv
                    ON ocv.ocvid = oco.ocoid
                INNER JOIN veiculo vei
                    ON ocv.ocvveiid = vei.veiid
                INNER JOIN marcadeveiculo tmv
                    ON vei.veitmvcodigo = tmv.tmvcodigo
                INNER JOIN tipoveiculo tvv
                    ON vei.veitvvcodigo = tvv.tvvcodigo
                WHERE oco.ocomunicipio = %s
                %s;""" % (municipio_id, limite)

        occurrences_by_region_sql = self.executa_query(query)
        list_of_ocurrences = self.transforma_dicionario_em_objetos(
            occurrences_by_region_sql,
            "OcorrenciaBasica",
            "ocorrencia_basica"
        )

        return list_of_ocurrences

    def lista_ocorrencias_por_periodo(self, data_inicio, data_fim, limite=0):
        """
        Executes and lists query results by period.

        @brief Local variable:
            query -
                SQL instruction to query the occurrences per period.
            occurrences_by_period_SQL
                Receives the query execution
            list_of_ocurrences
                Receives the list of occurrences per period.

        @param data_inicio Determines the initial date for the query search.
        @param data_fim Determines the final date for the query search.
        @param limite Limits the number of registers in the Database.
        @return List of occurences per period.
        """
        if limite != 0:
            limite = 'LIMIT %s' % limite
        else:
            limite = ''

        if data_inicio != "" and data_fim != "":
            data_inicio = data_inicio + ' 00:00:00'
            data_fim = data_fim + ' 23:59:59'

        query = """SELECT oco.ocoid, oco.ocodataocorrencia,
                tmu.tmudenominacao, tmu.tmuuf, tco.tcodescricao,
                tca.tcadescricao, lbr.lbrbr, tmv.tmvdescricao,
                oco.ocodataregistro, tta.ttadescricao, tvv.tvvdescricao
                FROM ocorrencia oco
                INNER JOIN municipio tmu
                    ON tmu.tmucodigo =  oco.ocomunicipio
                INNER JOIN tipoComunicacao tco
                    ON tco.tcocodigo = oco.ocotipo
                INNER JOIN localbr lbr
                    ON lbr.lbrid = oco.ocolocal
                INNER JOIN ocorrenciaacidente oac
                    ON oac.oacocoid = oco.ocoid
                INNER JOIN tipoAcidente tta
                    ON tta.ttacodigo = oac.oacttacodigo
                INNER JOIN causaacidente tca
                    ON tca.tcacodigo = oac.oactcacodigo
                INNER JOIN ocorrenciaveiculo ocv
                    ON ocv.ocvid = oco.ocoid
                INNER JOIN veiculo vei
                    ON ocv.ocvveiid = vei.veiid
                INNER JOIN marcadeveiculo tmv
                    ON vei.veitmvcodigo = tmv.tmvcodigo
                INNER JOIN tipoveiculo tvv
                    ON vei.veitvvcodigo = tvv.tvvcodigo
                WHERE oco.ocodataocorrencia >=
                    STR_TO_DATE('{0}', '%d/%m/%Y %H:%i:%s')
                AND oco.ocodataocorrencia <=
                    STR_TO_DATE('{1}', '%d/%m/%Y %H:%i:%s')
                {2}
                ;""".format(
            data_inicio,
            data_fim,
            limite
        )

        occurrences_by_period_sql = self.executa_query(query)
        list_of_ocurrences = self.transforma_dicionario_em_objetos(
            occurrences_by_period_sql,
            "OcorrenciaBasica",
            "ocorrencia_basica"
        )

        return list_of_ocurrences
