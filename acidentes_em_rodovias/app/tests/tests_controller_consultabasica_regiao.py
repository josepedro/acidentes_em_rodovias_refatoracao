# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#

from sys import stderr

from app.tests.tests_basic import Controller_Tests
from django.template import RequestContext, TemplateDoesNotExist, Context
from django.utils.datastructures import MultiValueDictKeyError

from app.controller import consultabasica_regiao_controller as ctrl


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

    def test_response_consulta_municipio(self):
        response = self.client.get('/acidentes_rodovias/consulta/municipio')
        self.assertEquals(response.status_code, 200)
