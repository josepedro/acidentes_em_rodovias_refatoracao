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


class TestMunicipio(SimpleTestCase):

    """docstring for TestMunicipio
    Class that tests the methods municipio_dao
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
        self.municipio = municipio_dao.MunicipioDAO()
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
        return "Teste da classe MunicipioDAO"

    def test_existing_municipio_dao_instance(self):
        """
        Tests if the returned county is not NULL
        """
        self.assertIsNotNone(self.municipio)

    def test_list_municipio(self):
        """
        Tests if the list of counties does not return null, in general and in a determined limit.
        """
        for i in self.municipio.lista_municipios("DF"):
            self.assertIsNotNone(i)
        for i in self.municipio.lista_municipios("DF", limite=3):
            self.assertIsNotNone(str(i))
            self.assertIsNotNone(i)
