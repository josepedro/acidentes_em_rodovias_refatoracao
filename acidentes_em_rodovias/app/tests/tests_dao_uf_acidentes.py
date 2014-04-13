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

from app.models.dao import uf_acidentes_dao as dao
from app.models import uf_acidentes

from _mysql_exceptions import OperationalError, ProgrammingError

from exception.internal_exceptions import *


class Test_UF_Acidentes(SimpleTestCase):
    """docstring for TestUFAcidentes
    Class that tests the methods from uf_acidentes_dao
    """

    def setUp(self):  # configura ambiente para teste
        """
        Configures the ambient for test.

        @brief Local variables:
            func - 
                Gets the name of the test function and fixes it for the output.
            out -
                Writes the name of the test function that is being proccessed.
        """    
        self.estatistica = dao.UFAcidentesDAO()
        # descobre qual metodo será chamado e formata a saída
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
        # informa que o teste foi realizado
        sys.stderr.write('Done\n')

    def shortDescription(self):
        """
        Gives a description of the class being tested.
        """
        return "Teste da classe UFAcidentesDAO"

    def test_uf_acidentes(self):
        """
        Test that verifies if the statistics are correctly instantiated, not leaving NULL
        """
        self.assertIsNotNone(self.estatistica)

    def test_acidentes_uf_geral(self):
        """
        Test if the statistics in accidents in all UFs are correctly instantiated, not returnning NULL
        """
        self.assertIsNotNone(self.estatistica.acidentes_uf_geral())

    def test_acidentes_uf_ano(self):
        """
        Test the number of accidents per year.

        @brief Local variables
            uf_acidentes_ano_list -
                List of number of accidents per year.

            anos -
                List of years.

            ufs -
                A Selected UF to check the number of accidents.
        """
        uf_acidentes_ano_list = self.estatistica.acidentes_uf_ano()

        anos = uf_acidentes_ano_list[0].ano_list
        self.assertEquals([
            2007,
            2008,
            2009,
            2010,
            2011,
            2012,
            2013
        ], anos)

        ufs = [i.uf for i in uf_acidentes_ano_list]
        self.assertIn('Pernambuco', ufs)
