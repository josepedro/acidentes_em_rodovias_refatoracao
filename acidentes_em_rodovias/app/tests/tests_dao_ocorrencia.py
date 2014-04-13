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

from django.test import SimpleTestCase
from django.core.urlresolvers import reverse, resolve

from app.models.dao import *

from _mysql_exceptions import OperationalError, ProgrammingError

from exception.internal_exceptions import *


class TestOcorrencia(SimpleTestCase):

    """docstring for TestOcorrencia
    Class that tests the methods from ocorrencia_basica_dao
    """

    def setUp(self):
        """
        Configures the ambient for test.

        @brief Local variables:
            func - 
                Gets the name of the test function and fixes it for the output.
            out -
                Writes the name of the test function that is being proccessed.
        """
        self.ocorrencia = ocorrencia_basica_dao.OcorrenciaBasicaDAO()
        func = str(self.id).split('=')[-1][:-2]
        func = func.split('test_')[-1]
        func = func.replace('_', ' ')
        out = '\rTeste de ' + func + ' '
        out = out.ljust(65, '-')
        sys.stderr.write(out)
        self.shortDescription()

    def tearDown(self):
        """
        Informs that the test was executed.
        """
        sys.stderr.write('Done\n')

    def shortDescription(self):
        """
        Gives a description of the class being tested.
        """
        return "Teste da classe OcorrenciaBasica"

    def test_existing_ocorrencia_dao_instance(self):
        """
        Tests to see if the occurrence was correctly instantiated
        """
        self.assertIsNotNone(self.ocorrencia)

    def test_ocorrencia_por_regiao(self):
        """
        Tests is the number of occurrences were instantiated, for a defined and an undefined limit.
        Also verifies if the return for the occurrences are in the same state.

        @brief Local variables
            oco -
                A list of occurences on a region.
        """
        # 97012 = Brasilia
        oco = self.ocorrencia.lista_ocorrencias_por_regiao(97012)
        self.assertIsNotNone(oco)
        oco = self.ocorrencia.lista_ocorrencias_por_regiao(97012, limite=3)
        self.assertIsNotNone(oco)
        self.assertLess(len(oco), 4)

        # verifica se todos os retornos estão no DF
        for i in oco:
            self.assertIsNotNone(str(i))
            self.assertEqual(i.tmuuf, 'DF')

    def test_ocorrencia_por_periodo(self):
        """
        Tests is the number of occurrences were instantiated in a determined period, for a defined and an undefined limit.
        Also verifies if the return for the occurrences are in the same year.

        @brief Local variables
            oco -
                A list of occurences on a period.
        """
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
