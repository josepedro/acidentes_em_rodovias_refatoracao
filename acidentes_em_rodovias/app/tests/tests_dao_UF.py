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



class TestUF(SimpleTestCase):

    """docstring for TestUF
    Class that tests the methods from uf_dao
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
        self.uf = uf_dao.UfDAO()
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
        return "Teste da classe GenericoDAO"

    def test_existing_uf_dao_instance(self):
        """
        Test to see if the return of the method is correctly instantiated.
        """
        self.assertIsNotNone(self.uf)

    def test_list_uf(self):
        """
        Test if the list of UF is correctly filled, given a defined and an undefined limit.
        """
        for i in self.uf.lista_ufs():
            self.assertIsNotNone(i)
        for i in self.uf.lista_ufs(limite=3):
            self.assertIsNotNone(str(i))
            self.assertIsNotNone(i)
