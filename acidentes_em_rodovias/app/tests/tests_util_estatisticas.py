# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#
from app.tests.tests_basic import Util_Estatisticas
from app.util import estatisticas_util


class Test_Estatisticas(Util_Estatisticas):

    """Test the validate of inputs"""

    def test_estatisticas_open_tables_values_gaussian(self):
        self.assertIsNotNone(
            estatisticas_util.open_table_values_gaussian_distribution(
                None, None))
        self.assertEquals(
            estatisticas_util.open_table_values_gaussian_distribution(
                None, None), 0.5)

    def test_estatisticas_distribuicao_normal(self):
        self.assertIsNotNone(
            estatisticas_util.distribuicao_normal(None, None, None))
        self.assertIsNotNone(
            estatisticas_util.distribuicao_normal(100, 50, 0.5))
        self.assertEquals(
            estatisticas_util.distribuicao_normal(100, 50, 0.5), 0.5)

    def test_total_mean(self):
        f = []
        for i in range(30):
            f.append(10)
        self.assertIsNotNone(estatisticas_util.calculate_total_mean(f))
        self.assertEquals(10, estatisticas_util.calculate_total_mean(f))

    def test_estatisticas_desvio_padrao(self):
        f = []
        for i in range(30):
            f.append(0)
        self.assertIsNotNone(estatisticas_util.desvio_padrao(None))
        self.assertIsNotNone(estatisticas_util.desvio_padrao(f))
        self.assertEquals(
            5.291502622129181, estatisticas_util.desvio_padrao(f))

    def test_estatisticas_media_sexo(self):
        self.assertIsNotNone(estatisticas_util.media_sexo(None, None))
