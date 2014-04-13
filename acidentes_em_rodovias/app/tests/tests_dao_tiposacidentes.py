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


class TestTiposAcidentes(SimpleTestCase):

    """docstring for TestTiposAcidentes
    Class that tests the methods from tipos_acidentes_dao
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
        self.dao = tipos_acidentes_dao.TiposAcidentesDAO()
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
        return "Teste da classe TestTiposAcidentesDAO"

    def test_tipos_acidentes(self):
        """
        Gives a description of the class being tested.
        """
        tipos_acidentes_list = self.dao.tipos_acidentes()

        self.assertAlmostEquals(len(tipos_acidentes_list), 10, delta=10)

        descricao_tipos_acidentes = []
        for acidente in tipos_acidentes_list:
            descricao_tipos_acidentes.append(acidente.tipos)

        self.assertIn("Tombamento", descricao_tipos_acidentes)

    def test_tipos_acidentes_ano(self):
        """
        Test if the method tipos_acidentes_ano is correctly instantiated.

        @brief Local variables
            tipos_acidentes_list -
                List of number of accidents and it's types.
            anos -
                List with years.
            descricao_tipos_acidentes_ano -
                List with a better description of each accident per year.
        """
        tipos_acidentes_ano_list = self.dao.tipos_acidentes_ano()

        anos = tipos_acidentes_ano_list[0].ano_list
        self.assertEquals([
            2007,
            2008,
            2009,
            2010,
            2011,
            2012,
            2013
        ], anos)

        descricao_tipos_acidentes_ano = []
        for acidente in tipos_acidentes_ano_list:
            descricao_tipos_acidentes_ano.append(acidente.tipo)

        self.assertIn("Tombamento", descricao_tipos_acidentes_ano)

    def test_probabilidade_tipos_acidentes(self):
        """
        Test if the method probabilidade_tipos_acidentes is correctly calculating the probability.

        @brief Local variables
            probabilidade_tipos_list -
                List with probability of accidents per type.
        """
        probabilidade_tipos_list = self.dao.probabilidade_tipos_acidentes()

        for prob_tipos in probabilidade_tipos_list:
            for probabilidade in prob_tipos.probabilidade_por_limite_list:
                self.assertTrue(probabilidade >= 0 and probabilidade <= 100)

    def test_media_desvio_tipos_acidentes(self):
        """
        Test if the method media_desvio_tipos_acidentes is calculationg the average and the standar deviation correctly.
        @brief Local variables
            media_desvio_list -
                List of standard deviation's averages.
        """
        media_desvio_list = self.dao.media_desvio_tipos_acidentes()

        for media_desvio_tipos_acidentes in media_desvio_list:
            self.assertTrue(media_desvio_tipos_acidentes.media > 0)
            self.assertTrue(media_desvio_tipos_acidentes.desvio > 0)
