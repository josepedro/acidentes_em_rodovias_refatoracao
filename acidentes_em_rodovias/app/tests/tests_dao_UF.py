# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#
from app.tests.tests_basic import DAO_Tests
from app.dao.uf_dao import UfDAO


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
