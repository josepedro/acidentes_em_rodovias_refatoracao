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

from app.tests.tests_basic import Util_Estatisticas
from django.template import RequestContext, TemplateDoesNotExist

from app.util import estatisticas_util

from _mysql_exceptions import *


class Test_Estatisticas(Util_Estatisticas):

    """Test the validate of inputs"""

    def test_estatisticas(self):
        testando = "testando"
        self.assertIsNotNone(testando)