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

from models.dao import br_acidentes_dao as dao
from models import br_acidentes

from _mysql_exceptions import OperationalError, ProgrammingError

from exception.internal_exceptions import *

# Adding upper directories to the Python Path
current_path = os.path.dirname(os.path.abspath('..'))
sys.path.append(current_path)
current_path = os.path.dirname(os.path.abspath('.'))
sys.path.append(current_path)


class Test_BR_Acidentes(SimpleTestCase):

    def setUp(self):
        self.estatistica = dao.BRAcidentesDAO()
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
        return "Teste da classe BRAcidentesDAO"

    def test_br_acidentes(self):
        self.assertIsNotNone(self.estatistica)

    def test_acidentes_br_geral(self):
        self.assertIsNotNone(self.estatistica.acidentes_br_geral())

    def test_acidentes_br_ano(self):
        br_acidentes_ano_list = self.estatistica.acidentes_br_ano()

        anos = br_acidentes_ano_list[0].ano_list
        self.assertEquals([
            2007,
            2008,
            2009,
            2010,
            2011,
            2012,
            2013
        ], anos)

        brs = [i.br for i in br_acidentes_ano_list]
        self.assertIn('40', brs)
