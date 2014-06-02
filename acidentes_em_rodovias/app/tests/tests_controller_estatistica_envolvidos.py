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

from app.controller import estatisticas_envolvidos_controller as ctrl

from _mysql_exceptions import *


class Test_Envolvidos(Controller_Tests):

    """docstring for Test_Envolvidos"""

    def shortDescription(self):
        return "Teste da classe Test_Envolvidos"

    def test_ocorrencias_e_envolvidos(self):
        self.assertIsNotNone(ctrl.ocorrencias_e_envolvidos(None))
