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

from app.models.dao import pessoas_acidentes_dao as dao
from app.models import pessoas_acidentes

from _mysql_exceptions import OperationalError, ProgrammingError

from exception.internal_exceptions import *


class Test_Estatistica_Pessoa(SimpleTestCase):

    """docstring for Test_Estatistica_Pessoa
    Class that tests the methods from pessoas_acidentes_dao
    """

    def setUp(self):
        """
        Configures the ambient for test.

        @brief Local variables:
            func -
                Gets the name of the test function and fixes it for the output.
            out -
                Writes the name of the test function that is being proccessed.
        """
        self.estatistica = dao.PessoasAcidentesDAO()
        func = str(self.id).split('=')[-1][:-2]
        func = func.split('test_')[-1]
        func = func.replace('_', ' ')
        out = '\rTeste de ' + func + ' '
        out = out.ljust(65, '-')
        sys.stderr.write(out)
        self.shortDescription()

    def tearDown(self):
        """
        Informs that the test was executed.
        """
        sys.stderr.write('Done\n')

    def shortDescription(self):
        """
        Gives a description of the class being tested.
        """
        return "Teste da classe EstatisticasPessoasDAO"

    def test_acidentes_por_sexo(self):
        """
        Test for acidentes_por_sexo to check if the statistic is instantiated.
        """
        self.assertIsNotNone(self.estatistica)

    def test_instancia_estatistica_pessoa(self):
        """
        Test for instancia_estatistica_pessoa to check if the possible
        exceptions are being treated correctly.
        """
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
