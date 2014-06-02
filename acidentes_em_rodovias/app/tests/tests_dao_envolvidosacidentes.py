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

from app.tests.tests_basic import DAO_Tests
from django.core.urlresolvers import reverse, resolve

from app.models.dao.envolvidos_acidentes_dao import EnvolvidosAcidentesDAO

from _mysql_exceptions import OperationalError, ProgrammingError

from app.exception.internal_exceptions import *

from datetime import datetime


class TestEnvolvidosAcidentes(DAO_Tests):

    """docstring for TestUF
    Class that tests the methods from envolvidos_acidentes_dao
    """

    def test_envolvidos_acidentes(self):
        """
        Tests to see if the method envolvidos_acidentes is correctly
        instantiated.

        @brief Local variables
            envolvidos_acidentes_list -
                Receives a list with the number involved in accidents.

            diffyears -
                Calculates the difference between years.
        """

        self.dao = EnvolvidosAcidentesDAO()
        envolvidos_acidentes_list = self.dao.envolvidos_acidentes()

        self.assertIsNotNone(envolvidos_acidentes_list)

        diffyears = datetime.now().year - 2007

        self.assertEquals(len(envolvidos_acidentes_list), diffyears)

    def test_media_desvio_envolvidos(self):
        """
        Tests to see if the method media_desvio_envolvidos is correctly
        instantiated.

        @brief Local variables
            desvio -
                Receives a list with the number of involved in accidents.
        """

        self.dao = EnvolvidosAcidentesDAO()
        lista_medias, desvio = self.dao.media_desvio_envolvidos()

        self.assertIsNotNone(lista_medias)
        self.assertIsNotNone(desvio)
