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

from app.models.dao import br_acidentes_dao as dao
from app.models import br_acidentes

from _mysql_exceptions import OperationalError, ProgrammingError

from exception.internal_exceptions import *


class Test_BR_Acidentes(SimpleTestCase):
    """
    Docstring for Test_BR_Acidentes
    Class that tests the methods from br_acidentes_dao
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
        self.estatistica = dao.BRAcidentesDAO()
        func = str(self.id).split('=')[-1][:-2]
        func = func.split('test_')[-1]
        func = func.replace('_', ' ')
        out = '\rTeste de ' + func + ' '
        out = out.ljust(65, '-')
        sys.stderr.write(out)
        ##Gives a short description of what class is the test being executed.
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
        return "Teste da classe BRAcidentesDAO"

    def test_br_acidentes(self):
        """
        Tests to see if the statistics were correctly instanced.
        """
        self.assertIsNotNone(self.estatistica)

    def test_acidentes_br_geral(self):
        """
        Tests to see if the query results return not NULL
        """
        self.assertIsNotNone(self.estatistica.acidentes_br_geral())

    def test_acidentes_br_ano(self):
        """
        Tests if a year is on the list of years.

        @brief Local variables:
            br_acidentes_ano_list -
                Receives a list of number of accidents per year.
            anos -
                receives a list of years.
            brs -
                
        """
        br_acidentes_ano_list = self.estatistica.acidentes_br_ano()

        anos = br_acidentes_ano_list[0].ano_list
        self.assertEquals([
            2007,
            2008,
            2009,
            2010,
            2011,
            2012,
            2013
        ], anos)

        brs = [i.br for i in br_acidentes_ano_list]
        self.assertIn('40', brs)
