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


class TestOcorrencia(SimpleTestCase):

    """docstring for TestOcorrencia"""

    def setUp(self):
        self.ocorrencia = ocorrencia_basica_dao.OcorrenciaBasicaDAO()
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
        return "Teste da classe OcorrenciaBasica"

    def test_existing_ocorrencia_dao_instance(self):
        self.assertIsNotNone(self.ocorrencia)

    def test_ocorrencia_por_regiao(self):
        # 97012 = Brasilia
        oco = self.ocorrencia.lista_ocorrencias_por_regiao(97012)
        self.assertIsNotNone(oco)
        oco = self.ocorrencia.lista_ocorrencias_por_regiao(97012, limite=3)
        self.assertIsNotNone(oco)
        self.assertLess(len(oco), 4)

        # verifica se todos os retornos estão no DF
        for i in oco:
            self.assertIsNotNone(str(i))
            self.assertEqual(i.tmuuf, 'DF')

    def test_ocorrencia_por_periodo(self):
        oco = self.ocorrencia.lista_ocorrencias_por_periodo(
            '06/01/06',
            '06/12/06'
        )
        self.assertIsNotNone(oco)
        oco = self.ocorrencia.lista_ocorrencias_por_periodo(
            '06/01/06', '06/12/06', limite=3)
        self.assertIsNotNone(oco)
        self.assertLess(len(oco), 4)

        # verifica se as ocorrencias aconteceram em 2006
        for i in oco:
            self.assertEqual(2006, i.ocodataocorrencia.year)
