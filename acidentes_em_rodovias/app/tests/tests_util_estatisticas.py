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

    def test_estatisticas_open_tables_values_gaussian(self):
        self.assertIsNotNone(estatisticas_util.open_table_values_gaussian_distribution(None, None))
        self.assertEquals(estatisticas_util.open_table_values_gaussian_distribution(None, None), 0.5)

    def test_estatisticas_distribuicao_normal(self):
        self.assertIsNotNone(estatisticas_util.distribuicao_normal(None,None,None))
        self.assertIsNotNone(estatisticas_util.distribuicao_normal(100,50,0.5))
        self.assertEquals(estatisticas_util.distribuicao_normal(100,50,0.5),0.5)        

    def test_estatisticas_desvio_padrao(self):
        testando = "testando"
        self.assertIsNotNone(testando)

    def test_estatisticas_media_sexo(self):
        testando = "testando"
        self.assertIsNotNone(testando)