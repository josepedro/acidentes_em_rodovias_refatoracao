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

from models.dao import pessoas_acidentes_dao as dao
from models import pessoas_acidentes

from _mysql_exceptions import OperationalError, ProgrammingError

from exception.internal_exceptions import *

# Adding upper directories to the Python Path
current_path = os.path.dirname(os.path.abspath('..'))
sys.path.append(current_path)
current_path = os.path.dirname(os.path.abspath('.'))
sys.path.append(current_path)


class Test_Estatistica_Pessoa(SimpleTestCase):

    """docstring for Test_Estatistica_Pessoa
    """

    def setUp(self):
        self.estatistica = dao.PessoasAcidentesDAO()
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
        return "Teste da classe EstatisticasPessoasDAO"

    def test_acidentes_por_sexo(self):
        self.assertIsNotNone(self.estatistica)

    def test_instancia_estatistica_pessoa(self):
        with self.assertRaises(NameError):
            self.assertIsNotNone(
                estatistica_pessoas.EstatisticaPessoas()
            )
        with self.assertRaises(NameError):
            self.assertIsNotNone(str(
                estatistica_pessoas.EstatisticaPessoas()
            ))
        with self.assertRaises(NameError):
            self.assertIsNotNone(str(
                estatistica_pessoas.PessoasAcidentesGeral()
            ))
