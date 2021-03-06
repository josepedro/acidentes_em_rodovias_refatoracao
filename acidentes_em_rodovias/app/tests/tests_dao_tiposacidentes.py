# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#
from app.tests.tests_basic import DAO_Tests
from app.dao.tipos_acidentes_dao import TiposAcidentesDAO


class TestTiposAcidentes(DAO_Tests):

    """docstring for TestTiposAcidentes
    Class that tests the methods from tipos_acidentes_dao
    """

    def test_tipos_acidentes(self):
        """
        Gives a description of the class being tested.
        """

        self.dao = TiposAcidentesDAO()
        tipos_acidentes_list = self.dao.tipos_acidentes()

        self.assertAlmostEquals(len(tipos_acidentes_list), 10, delta=10)

        descricao_tipos_acidentes = []
        for acidente in tipos_acidentes_list:
            descricao_tipos_acidentes.append(acidente.tipo)

        self.assertIn("Tombamento", descricao_tipos_acidentes)

    def test_tipos_acidentes_ano(self):
        """
        Test if the method tipos_acidentes_ano is correctly instantiated.

        @brief Local variables
            tipos_acidentes_list -
                List of number of accidents and it's types.
            anos -
                List with years.
            descricao_tipos_acidentes_ano -
                List with a better description of each accident per year.
        """

        self.dao = TiposAcidentesDAO()
        tipos_acidentes_ano_list = self.dao.tipos_acidentes_ano()

        anos = tipos_acidentes_ano_list[0].ano_list
        self.assertEquals([
            2007,
            2008,
            2009,
            2010,
            2011,
            2012,
            2013
        ], anos)

        descricao_tipos_acidentes_ano = []
        for acidente in tipos_acidentes_ano_list:
            descricao_tipos_acidentes_ano.append(acidente.tipo)

        self.assertIn("Tombamento", descricao_tipos_acidentes_ano)

    def test_probabilidade_tipos_acidentes(self):
        """
        Test if the method probabilidade_tipos_acidentes is correctly
        calculating the probability.

        @brief Local variables
            probabilidade_tipos_list -
                List with probability of accidents per type.
        """

        self.dao = TiposAcidentesDAO()
        probabilidade_tipos_list = self.dao.probabilidade_tipos_acidentes()

        for prob_tipos in probabilidade_tipos_list:
            for probabilidade in prob_tipos.probabilidade_por_limite_list:
                self.assertTrue(probabilidade >= 0 and probabilidade <= 100)

    def test_media_desvio_tipos_acidentes(self):
        """
        Test if the method media_desvio_tipos_acidentes is calculationg the
        average and the standar deviation correctly.
        @brief Local variables
            media_desvio_list -
                List of standard deviation's averages.
        """

        self.dao = TiposAcidentesDAO()
        media_desvio_list = self.dao.media_desvio_tipos_acidentes()

        for media_desvio_tipos_acidentes in media_desvio_list:
            self.assertTrue(media_desvio_tipos_acidentes.media > 0)
            self.assertTrue(media_desvio_tipos_acidentes.desvio > 0)
