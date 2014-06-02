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

from app.tests.tests_basic import Controller_Tests
from django.template import RequestContext, TemplateDoesNotExist, Context
from django.utils.datastructures import MultiValueDictKeyError

from app.controller import consultabasica_periodo_controller as ctrl

from _mysql_exceptions import *

from nose import with_setup

from mock import MagicMock, patch, Mock


class Test_Periodo(Controller_Tests):

    """docstring for Test_Periodo"""

    def shortDescription(self):
        return "Teste da classe Test_Periodo"

    def test_consulta_por_periodo(self):
        self.assertIsNotNone(ctrl.consulta_por_periodo(None))

    def test_consulta_ocorrencias_por_periodo(self):
        with self.assertRaises(AttributeError):
            self.assertIsNotNone(ctrl.consulta_ocorrencias_por_periodo(None))
