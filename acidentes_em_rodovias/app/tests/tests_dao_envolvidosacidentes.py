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

from app.models.dao import *

from _mysql_exceptions import OperationalError, ProgrammingError

from exception.internal_exceptions import *

from datetime import datetime


class TestEnvolvidosAcidentes(SimpleTestCase):

    """docstring for TestUF
    Class that tests the methods from envolvidos_acidentes_dao
    """

    def setUp(self):  # configura ambiente para teste
        """
        Configures the ambient for test.

        @brief Local variables:
            func - 
                Gets the name of the test function and fixes it for the output.
            out -
                Writes the name of the test function that is being proccessed.
        """
        self.dao = envolvidos_acidentes_dao.EnvolvidosAcidentesDAO()
        # descobre qual método será chamado e formata a saída
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
        # informa que o teste foi realizado
        sys.stderr.write('Done\n')

    def shortDescription(self):
        """
        Gives a description of the class being tested.
        """
        return "Teste da classe TestEnvolvidosAcidentesDAO"

    def test_envolvidos_acidentes(self):
        """
        Tests to see if the method envolvidos_acidentes is correctly instantiated.

        @brief Local variables
            envolvidos_acidentes_list -
                Receives a list with the number involved in accidents.

            diffyears -
                Calculates the difference between years.
        """
        envolvidos_acidentes_list = self.dao.envolvidos_acidentes()

        self.assertIsNotNone(envolvidos_acidentes_list)

        diffyears = datetime.now().year - 2007

        self.assertEquals(len(envolvidos_acidentes_list), diffyears + 1)

    def test_media_desvio_envolvidos(self):
        """
        Tests to see if the method media_desvio_envolvidos is correctly instantiated.

        @brief Local variables
            desvio -
                Receives a list with the number of involved in accidents.
        """
        lista_medias, desvio = self.dao.media_desvio_envolvidos()

        self.assertIsNotNone(lista_medias)
        self.assertIsNotNone(desvio)
