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

from models.dao import *

from _mysql_exceptions import OperationalError, ProgrammingError

from exception.internal_exceptions import *

# Adding upper directories to the Python Path
current_path = os.path.dirname(os.path.abspath('..'))
sys.path.append(current_path)
current_path = os.path.dirname(os.path.abspath('.'))
sys.path.append(current_path)


class TestMunicipio(SimpleTestCase):

    """docstring for TestMunicipio"""

    def setUp(self):
        self.municipio = municipio_dao.MunicipioDAO()
        func = str(self.id).split('=')[-1][:-2]
        func = func.split('test_')[-1]
        func = func.replace('_', ' ')
        out = '\rTeste de ' + func + ' '
        out = out.ljust(65, '-')
        sys.stderr.write(out)
        self.shortDescription()

    def tearDown(self):
        sys.stderr.write('Done\n')

    def shortDescription(self):
        return "Teste da classe MunicipioDAO"

    def test_existing_municipio_dao_instance(self):
        self.assertIsNotNone(self.municipio)

    def test_list_municipio(self):
        for i in self.municipio.lista_municipios("DF"):
            self.assertIsNotNone(i)
        for i in self.municipio.lista_municipios("DF", limite=3):
            self.assertIsNotNone(str(i))
            self.assertIsNotNone(i)
