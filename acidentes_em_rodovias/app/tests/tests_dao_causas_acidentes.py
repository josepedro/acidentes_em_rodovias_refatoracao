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


class TestCausasAcidentes(SimpleTestCase):

    """docstring for TestUF
    Tests for the class causa_acidente_dao.
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
        self.dao = causas_acidentes_dao.CausasAcidentesDAO()
        func = str(self.id).split('=')[-1][:-2]
        func = func.split('test_')[-1]
        func = func.replace('_', ' ')
        out = '\rTeste de ' + func + ' '
        out = out.ljust(65, '-')
        sys.stderr.write(out)
        ##Gives a short description of the class being tested.
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
        return "Teste da classe TestCausasAcidentesDAO"

    def test_causas_acidentes(self):
        """
        Tests if method causas_acidentes is correctly instanced.

        @brief Local variables
            causas_acidentes_list -
                Receives a list with the causes of accidents.
            descricao_causas_acidentes -
                Receives a list with a better description to the cause of the accident.
        """
        causas_acidentes_list = self.dao.causas_acidentes()

        descricao_causas_acidentes = []
        for acidente in causas_acidentes_list:
            descricao_causas_acidentes.append(acidente.causa)

        self.assertIn("Outras", descricao_causas_acidentes)

    def test_causas_acidentes_ano(self):
        """
        Tests if method causas_acidentes_ano is correctly instanced.

        @brief Local variables
            causas_acidentes_list -
                Receives a list containing the causes of accidents and their number per year.
            anos -
                Receives a list of years to be tested.
            descricao_causas_acidentes_ano -
                Receives a list with a better description to the cause of the accidents per year.
        """
        causas_acidentes_ano_list = self.dao.causas_acidentes_ano()

        anos = causas_acidentes_ano_list[0].ano_list
        self.assertEquals([
            2007,
            2008,
            2009,
            2010,
            2011,
            2012,
            2013
        ], anos)

        descricao_causas_acidentes_ano = []
        for acidente in causas_acidentes_ano_list:
            descricao_causas_acidentes_ano.append(acidente.causa)

        self.assertIn("Outras", descricao_causas_acidentes_ano)

    def test_probabilidade_causas_acidentes(self):
        """
        Tests if method probabilidade_causas_acidentes is correctly calculationg the probability.

        @brief Local variable
            probabilidade_causas_list -
                Receives a list with the accidents causes.
        """
        probabilidade_causas_list = self.dao.probabilidade_causas_acidentes()

        for causa in probabilidade_causas_list:
            for probabilidade in causa.probabilidade_por_limite_list:
                self.assertTrue(probabilidade >= 0 and probabilidade <= 100)

    def test_media_desvio_causas_acidentes(self):
        """
        Tests if method media_desvio_causas_acidentes is correctly calculationg the standard deviation.

        @brief Local variable
            media_desvio_list -
                Receives a list with the media and standard deviation of causes.
        """
        media_desvio_list = self.dao.media_desvio_causas_acidentes()

        for media_desvio_causas_acidentes in media_desvio_list:
            self.assertTrue(media_desvio_causas_acidentes.media > 0)
            self.assertTrue(media_desvio_causas_acidentes.desvio > 0)
