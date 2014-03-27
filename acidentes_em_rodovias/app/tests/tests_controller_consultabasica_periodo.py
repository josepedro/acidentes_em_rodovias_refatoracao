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
from django.template import RequestContext, TemplateDoesNotExist, Context
from django.utils.datastructures import MultiValueDictKeyError

from controller import consultabasica_periodo_controller as ctrl

from _mysql_exceptions import *

from nose import with_setup

from mock import MagicMock, patch, Mock

# Adding upper directories to the Python Path
current_path = os.path.dirname(os.path.abspath('..'))
sys.path.append(current_path)
current_path = os.path.dirname(os.path.abspath('.'))
sys.path.append(current_path)


class Test_Periodo(SimpleTestCase):

    """docstring for Test_Periodo"""

    def setUp(self):
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
        return "Teste da classe Test_Periodo"

    def test_consulta_por_periodo(self):
        self.assertIsNotNone(ctrl.consulta_por_periodo(None))

    def test_consulta_ocorrencias_por_periodo(self):
        with self.assertRaises(AttributeError):
            self.assertIsNotNone(ctrl.consulta_ocorrencias_por_periodo(None))
