# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#
from app.tests.tests_basic import DAO_Tests
from app.models.dao.uf_acidentes_dao import UFAcidentesDAO


class Test_UF_Acidentes(DAO_Tests):

    """docstring for TestUFAcidentes
    Class that tests the methods from uf_acidentes_dao
    """

    def test_uf_acidentes(self):
        """
        Test that verifies if the statistics are correctly instantiated, not
        leaving NULL
        """

        self.estatistica = UFAcidentesDAO()
        self.assertIsNotNone(self.estatistica)

    def test_acidentes_uf_geral(self):
        """
        Test if the statistics in accidents in all UFs are correctly
        instantiated, not returnning NULL
        """

        self.estatistica = UFAcidentesDAO()
        self.assertIsNotNone(self.estatistica.acidentes_uf_geral())

    def test_acidentes_uf_ano(self):
        """
        Test the number of accidents per year.

        @brief Local variables
            uf_acidentes_ano_list -
                List of number of accidents per year.

            anos -
                List of years.

            ufs -
                A Selected UF to check the number of accidents.
        """

        self.estatistica = UFAcidentesDAO()
        uf_acidentes_ano_list = self.estatistica.acidentes_uf_ano()

        anos = uf_acidentes_ano_list[0].ano_list
        self.assertEquals([
            2007,
            2008,
            2009,
            2010,
            2011,
            2012,
            2013
        ], anos)

        ufs = [i.uf for i in uf_acidentes_ano_list]
        self.assertIn('Pernambuco', ufs)
