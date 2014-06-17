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


class TestEstatisticaBR(Controller_Tests):

    def tearDown(self):
        myconfiguration.DB_PASS = self.db_password

    def test_response_estatistica_br(self):
        response = self.client.get('/acidentes_rodovias/estatisticas/br')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'br_acidentes.html')

    def test_database_connection(self):
        myconfiguration.DB_PASS = ''

        response = self.client.get('/acidentes_rodovias/estatisticas/br')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertEquals(
            response.context[-1]['erro'],
            "Ocorreu um erro no sistema, tente novamente mais tarde!"
        )
