# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#
from app.tests.tests_basic import Controller_Tests

from app import myconfiguration


class TestControllerEstatisticaTipo(Controller_Tests):

    """docstring for TestControllerEstatisticaTipo"""

    def shortDescription(self):
        return "Teste da classe TestControllerEstatisticaTipo"

    def tearDown(self):
        myconfiguration.DB_PASS = self.db_password

    def test_response_causas_acidentes(self):
        """ Test for response """
        response = self.client.get(
            '/acidentes_rodovias/estatisticas/tipos-acidentes'
        )
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tipos_acidentes.html')

    def test_view_object_returned(self):
        """ Test object returned from view """
        response = self.client.get(
            '/acidentes_rodovias/estatisticas/tipos-acidentes'
        )
        self.assertIsNotNone(response.context[-1]['tipos_acidentes_list'])
        self.assertIsNotNone(response.context[-1]['tipos_acidentes_ano_list'])
        self.assertIsNotNone(
            response.context[-1]['probabilidade_tipos_acidentes_list']
        )
        self.assertIsNotNone(response.context[-1]['anos'])
        self.assertIsNotNone(
            response.context[-1]['tipos']
        )
        self.assertIsNotNone(
            response.context[-1]['media_desvio_tipos_acidentes_list'])

    def test_database_connection(self):
        """ Test for database connection """
        myconfiguration.DB_PASS = ''

        response = self.client.get(
            '/acidentes_rodovias/estatisticas/tipos-acidentes'
        )
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertEquals(
            response.context[-1]['erro'],
            "Ocorreu um erro no sistema, tente novamente mais tarde!"
        )
