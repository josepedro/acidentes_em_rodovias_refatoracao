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

from controller import consultabasica_regiao_controller as ctrl

from _mysql_exceptions import *

from nose import with_setup

from mock import MagicMock, patch, Mock

# Adding upper directories to the Python Path
current_path = os.path.dirname(os.path.abspath('..'))
sys.path.append(current_path)
current_path = os.path.dirname(os.path.abspath('.'))
sys.path.append(current_path)


class Test_Regiao(SimpleTestCase):

    """docstring for Test_Regiao"""

    def setUp(self):
        self.request = Context()
        self.request.GET = dict()
        self.request.GET['uf_id'] = 'DF'
        self.request.GET['municipio_id'] = 'Brasilia'
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
        return "Teste da classe Test_Regiao"

    def test_consulta_por_regiao(self):
        ctrl.consulta_por_regiao(None)

    def test_consulta_municipios_na_regiao(self):
        ctrl.consulta_municipios_na_regiao(self.request)

    def test_consulta_ocorrencias_por_municipio(self):
        ctrl.consulta_ocorrencias_por_municipio(self.request)
