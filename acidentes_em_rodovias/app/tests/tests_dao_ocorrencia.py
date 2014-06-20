# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#
from app.tests.tests_basic import DAO_Tests
from app.dao.ocorrencia_basica_dao import OcorrenciaBasicaDAO


class TestOcorrencia(DAO_Tests):

    """docstring for TestOcorrencia
    Class that tests the methods from ocorrencia_basica_dao
    """

    def test_existing_ocorrencia_dao_instance(self):
        """
        Tests to see if the occurrence was correctly instantiated
        """

        self.ocorrencia = OcorrenciaBasicaDAO()
        self.assertIsNotNone(self.ocorrencia)

    def test_ocorrencia_por_regiao(self):
        """
        Tests is the number of occurrences were instantiated, for a defined
        and an undefined limit.
        Also verifies if the return for the occurrences are in the same state.

        @brief Local variables
            oco -
                A list of occurences on a region.
        """

        self.ocorrencia = OcorrenciaBasicaDAO()
        _brasilia = 97012
        oco = self.ocorrencia.lista_ocorrencias_por_regiao(_brasilia)
        self.assertIsNotNone(oco)
        oco = self.ocorrencia.lista_ocorrencias_por_regiao(_brasilia, limite=3)
        self.assertIsNotNone(oco)
        self.assertLess(len(oco), 4)

        # verifica se todos os retornos estão no DF
        for i in oco:
            self.assertIsNotNone(str(i))
            self.assertEqual(i.tmuuf, 'DF')

    def test_ocorrencia_por_periodo(self):
        """
        Tests is the number of occurrences were instantiated in a determined
        period, for a defined and an undefined limit.
        Also verifies if the return for the occurrences are in the same year.

        @brief Local variables
            oco -
                A list of occurences on a period.
        """

        self.ocorrencia = OcorrenciaBasicaDAO()
        oco = self.ocorrencia.lista_ocorrencias_por_periodo(
            '06/01/06',
            '06/12/06'
        )
        self.assertIsNotNone(oco)
        oco = self.ocorrencia.lista_ocorrencias_por_periodo(
            '06/01/06', '06/12/06', limite=3)
        self.assertIsNotNone(oco)
        self.assertLess(len(oco), 4)

        # verifica se as ocorrencias aconteceram em 2006
        for i in oco:
            self.assertEqual(2006, i.ocodataocorrencia.year)
