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

from app.tests.tests_basic import DAO_Tests
from django.core.urlresolvers import reverse, resolve

from app.models.dao.br_acidentes_dao import BRAcidentesDAO
from app.models import br_acidentes

from _mysql_exceptions import OperationalError, ProgrammingError

from app.exception.internal_exceptions import *


class Test_BR_Acidentes(DAO_Tests):
    """
    Docstring for Test_BR_Acidentes
    Class that tests the methods from br_acidentes_dao
    """

    def test_br_acidentes(self):
        """
        Tests to see if the statistics were correctly instanced.
        """

        self.estatistica = BRAcidentesDAO()
        self.assertIsNotNone(self.estatistica)

    def test_acidentes_br_geral(self):
        """
        Tests to see if the query results return not NULL
        """

        self.estatistica = BRAcidentesDAO()
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
                receives a list of br's.
        """

        self.estatistica = BRAcidentesDAO()
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
