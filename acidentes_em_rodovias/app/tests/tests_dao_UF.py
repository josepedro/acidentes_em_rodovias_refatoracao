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

from app.models.dao.uf_dao import UfDAO

from _mysql_exceptions import OperationalError, ProgrammingError

from app.exception.internal_exceptions import *


class TestUF(DAO_Tests):

    """docstring for TestUF
    Class that tests the methods from uf_dao
    """

    def test_existing_uf_dao_instance(self):
        """
        Test to see if the return of the method is correctly instantiated.
        """

        self.uf = UfDAO()
        self.assertIsNotNone(self.uf)

    def test_list_uf(self):
        """
        Test if the list of UF is correctly filled, given a defined and an
        undefined limit.
        """

        self.uf = UfDAO()
        for i in self.uf.lista_ufs():
            self.assertIsNotNone(i)
        for i in self.uf.lista_ufs(limite=3):
            self.assertIsNotNone(str(i))
            self.assertIsNotNone(i)
