# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#

from sys import stderr

from django.test import Client
from app.tests.tests_basic import Controller_Tests
from django.template import Context


from app.controller import consultabasica_regiao_controller as ctrl

from app import myconfiguration


class Test_Regiao(Controller_Tests):

    """docstring for Test_Regiao"""

    def setUp(self):
        self.my_type = '[Controller]'
        self.request = Context()
        self.request.GET = dict()
        self.request.GET['uf_id'] = 'DF'
        self.request.GET['municipio_id'] = '0'
        stderr.write(self.__str__())
        self.shortDescription()
        self.client = Client()
        self.db_password = myconfiguration.DB_PASS

    def tearDown(self):
        myconfiguration.DB_PASS = self.db_password

    def test_consulta_por_regiao(self):
        ctrl.consulta_por_regiao(None)

    def test_consulta_municipios_na_regiao(self):
        ctrl.consulta_municipios_na_regiao(self.request)

    def test_consulta_ocorrencias_por_municipio(self):
        ctrl.consulta_ocorrencias_por_municipio(self.request)

    def test_response_regiao(self):
        response = self.client.get('/acidentes_rodovias/regiao')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'regiao.html')

    def test_response_municipios_regiao(self):
        response = self.client.get('/acidentes_rodovias/municipios-regiao')
        self.assertEquals(response.status_code, 200)

        response = self.client.get(
            '/acidentes_rodovias/municipios-regiao?uf_id=AC'
        )
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'municipio.html')

    def test_municipios_regiao_invalid_param(self):
        response = self.client.get(
            '/acidentes_rodovias/municipios-regiao?uf_id='
        )
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

        response = self.client.get(
            "/acidentes_rodovias/municipios-regiao?uf_id=';a"
        )
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_response_consulta_municipio(self):
        response = self.client.get('/acidentes_rodovias/consulta/municipio')
        self.assertEquals(response.status_code, 200)

        response = self.client.get(
            '/acidentes_rodovias/consulta/municipio?municipio_id=6432'
        )
        self.assertEquals(response.status_code, 200)

    def test_database_conection(self):
        myconfiguration.DB_PASS = ""
        response = self.client.get(
            '/acidentes_rodovias/consulta/municipio?municipio_id=6432'
        )
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertEquals(
            response.context[-1]['erro'],
            "Ocorreu um erro no sistema, tente novamente mais tarde!"
        )

        response = self.client.get(
            '/acidentes_rodovias/municipios-regiao?uf_id=AC'
        )
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertEquals(
            response.context[-1]['erro'],
            "Ocorreu um erro no sistema, tente novamente mais tarde!"
        )

        response = self.client.get('/acidentes_rodovias/regiao')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertEquals(
            response.context[-1]['erro'],
            "Ocorreu um erro no sistema, tente novamente mais tarde!"
        )
