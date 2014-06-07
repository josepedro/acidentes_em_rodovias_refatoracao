# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#

import sys
import os
import inspect

from app.tests.tests_basic import Controller_Tests
from django.template import RequestContext, TemplateDoesNotExist, Context
from django.utils.datastructures import MultiValueDictKeyError

from app.controller import consultabasica_periodo_controller as ctrl
from app.controller.consultabasica_periodo_controller import *

from _mysql_exceptions import *

from nose import with_setup

from app.exception.validation_exceptions import *

from app import myconfiguration


class Test_Periodo(Controller_Tests):

    """docstring for Test_Periodo"""

    def shortDescription(self):
        return "Teste da classe Test_Periodo"

    def tearDown(self):
        myconfiguration.DB_PASS = self.db_password

    def test_consulta_por_periodo(self):
        self.assertIsNotNone(ctrl.consulta_por_periodo(None))

    def test_consulta_ocorrencias_por_periodo(self):
        with self.assertRaises(AttributeError):
            self.assertIsNotNone(ctrl.consulta_ocorrencias_por_periodo(None))

    def test_response_consulta_por_periodo(self):
        response = self.client.get('/acidentes_rodovias/periodo')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'periodo.html')

    def test_response_ocorrencias_por_periodo(self):
        response = self.client.get(
            '/acidentes_rodovias/consulta/periodo?data_inicio=01%2F01%2F2008&data_fim=02%2F01%2F2009'
        )
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'resultado.html')
        self.assertEquals(response.context[-1]['start_date'], '01/01/2008')
        self.assertEquals(response.context[-1]['end_date'], '02/01/2009')

    def test_response_invalid_period(self):
        response = self.client.get(
            '/acidentes_rodovias/consulta/periodo?data_inicio=01%2F01%2F2008&data_fim='
        )
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertEquals(response.context[-1]['erro'],
                          "Preencha corretamente o formulário!"
                          )

        response = self.client.get(
            '/acidentes_rodovias/consulta/periodo?data_inicio=&data_fim=01%2F01%2F2009'
        )
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertEquals(response.context[-1]['erro'],
                          "Preencha corretamente o formulário!"
                          )

        response = self.client.get(
            '/acidentes_rodovias/consulta/periodo?data_inicio=&data_fim=invalido'
        )
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertEquals(response.context[-1]['erro'],
                          "Preencha corretamente o formulário!"
                          )

    def test_database_conection(self):
        myconfiguration.DB_PASS = ""

        response = self.client.get(
            '/acidentes_rodovias/consulta/periodo?data_inicio=01%2F01%2F2008&data_fim=02%2F01%2F2009'
        )
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertEquals(response.context[-1]['erro'],
                          "Ocorreu um erro no sistema, tente novamente mais tarde!"
                          )
