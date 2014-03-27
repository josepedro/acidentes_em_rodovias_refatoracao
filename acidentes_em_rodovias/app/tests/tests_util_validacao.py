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
from django.template import RequestContext, TemplateDoesNotExist

from exception.validation_exceptions import *

from util import validacao_util

from _mysql_exceptions import *

# Adding upper directories to the Python Path
current_path = os.path.dirname(os.path.abspath('..'))
sys.path.append(current_path)
current_path = os.path.dirname(os.path.abspath('.'))
sys.path.append(current_path)


class Test_Valida(SimpleTestCase):

    """docstring for Test_Valida"""

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
        return "Teste da classe Test_Valida"

    def test_valida_data(self):
        self.assertFalse(validacao_util.valida_data(
            "10/10/2013"
        ))
        with self.assertRaises(DataInvalidaError):
            self.assertFalse(validacao_util.valida_data(
                "20 de março de 2013"
            ))

    def test_valida_caracteres(self):
        with self.assertRaises(ParametroInseguroClienteError):
            self.assertIsNone(validacao_util.valida_caracteres(None))
        with self.assertRaises(ParametroInseguroClienteError):
            self.assertFalse(validacao_util.valida_caracteres("./$%^&"))
