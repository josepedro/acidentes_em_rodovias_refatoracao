# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#
from app.tests.tests_basic import Controller_Tests
from app.controller import estatisticas_envolvidos_controller as ctrl
from app import myconfiguration


class Test_Envolvidos(Controller_Tests):

    """docstring for Test_Envolvidos"""

    def tearDown(self):
        myconfiguration.DB_PASS = self.db_password

    def test_ocorrencias_e_envolvidos(self):
        self.assertIsNotNone(ctrl.ocorrencias_e_envolvidos(None))

    def test_database_connection(self):
        myconfiguration.DB_PASS = ''

        response = self.client.get(
            '/acidentes_rodovias/estatisticas/acidentes-sexo')
        self.assertTemplateUsed(response, 'index.html')
        self.assertEquals(
            response.context[-1]['erro'],
            "Ocorreu um erro no sistema, tente novamente mais tarde!"
        )
