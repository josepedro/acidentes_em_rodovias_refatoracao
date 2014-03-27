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


class TestCausasAcidentes(SimpleTestCase):

    """docstring for TestUF"""

    def setUp(self):
        self.dao = causas_acidentes_dao.CausasAcidentesDAO()
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
        return "Teste da classe TestCausasAcidentesDAO"

    def test_causas_acidentes(self):
        causas_acidentes_list = self.dao.causas_acidentes()

        descricao_causas_acidentes = []
        for acidente in causas_acidentes_list:
            descricao_causas_acidentes.append(acidente.causa)

        self.assertIn("Outras", descricao_causas_acidentes)

    def test_causas_acidentes_ano(self):
        causas_acidentes_ano_list = self.dao.causas_acidentes_ano()

        anos = causas_acidentes_ano_list[0].ano_list
        self.assertEquals([
            2007,
            2008,
            2009,
            2010,
            2011,
            2012,
            2013
        ], anos)

        descricao_causas_acidentes_ano = []
        for acidente in causas_acidentes_ano_list:
            descricao_causas_acidentes_ano.append(acidente.causa)

        self.assertIn("Outras", descricao_causas_acidentes_ano)

    def test_probabilidade_causas_acidentes(self):
        probabilidade_causas_list = self.dao.probabilidade_causas_acidentes()

        for causa in probabilidade_causas_list:
            for probabilidade in causa.probabilidade_por_limite_list:
                self.assertTrue(probabilidade >= 0 and probabilidade <= 100)

    def test_media_desvio_causas_acidentes(self):
        media_desvio_list = self.dao.media_desvio_causas_acidentes()

        for media_desvio_causas_acidentes in media_desvio_list:
            self.assertTrue(media_desvio_causas_acidentes.media > 0)
            self.assertTrue(media_desvio_causas_acidentes.desvio > 0)
