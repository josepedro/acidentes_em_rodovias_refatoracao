# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#

from app.tests.tests_basic import Controller_Tests

from app.controller import estatisticas_causas_controller as ctrl

from app import myconfiguration


class TestCausa(Controller_Tests):

    """docstring for TestCausa"""

    def shortDescription(self):
        return "Teste da classe TestCausa"

    def tearDown(self):
        myconfiguration.DB_PASS = self.db_password

    def test_causas_acidentes(self):
        self.assertIsNotNone(ctrl.causas_acidentes(None))

    def test_response_causas_acidentes(self):
        response = self.client.get(
            '/acidentes_rodovias/estatisticas/causas-acidentes'
        )
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'causas_acidentes.html')

    def test_view_return_objects(self):
        response = self.client.get(
            '/acidentes_rodovias/estatisticas/causas-acidentes'
        )
        self.assertIsNotNone(response.context[-1]['causas_acidentes_list'])
        self.assertIsNotNone(response.context[-1]['causas_acidentes_list'])
        self.assertIsNotNone(response.context[-1]['causas_acidentes_ano_list'])
        self.assertIsNotNone(response.context[-1]['anos'])
        self.assertIsNotNone(
            response.context[-1]['probabilidade_causas_acidentes_list']
        )
        self.assertIsNotNone(response.context[-1]['causas'])
        self.assertIsNotNone(
            response.context[-1]['media_desvio_causas_acidentes_list']
        )

    def test_database_connection(self):
        myconfiguration.DB_PASS = ''

        response = self.client.get(
            '/acidentes_rodovias/estatisticas/causas-acidentes')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertEquals(
            response.context[-1]['erro'],
            "Ocorreu um erro no sistema, tente novamente mais tarde!"
        )
