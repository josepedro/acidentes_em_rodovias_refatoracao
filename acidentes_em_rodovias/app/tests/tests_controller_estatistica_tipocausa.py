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
from django.template import RequestContext, TemplateDoesNotExist

from app.controller import estatisticas_causas_controller as ctrl

from _mysql_exceptions import *

class TestTipoCausa(Controller_Tests):

    """docstring for TestTipoCausa"""

    def shortDescription(self):
        return "Teste da classe TestTipoCausa"

    def test_causas_acidentes(self):
        self.assertIsNotNone(ctrl.causas_acidentes(None))
