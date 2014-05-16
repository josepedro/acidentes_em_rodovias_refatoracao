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
        self.request = Context()
        self.request.GET = dict()
        self.request.GET['uf_id'] = 'DF'
        self.request.GET['municipio_id'] = 'Brasilia'
        func = str(self.id).split('=')[-1][:-2]
        func = func.split('test_')[-1]
        func = func.replace('_', ' ')
        out = '\rTeste de ' + func + ' '
        out = out.ljust(65, '-')
        stderr.write(out)
        self.shortDescription()

    def test_consulta_por_regiao(self):
        ctrl.consulta_por_regiao(None)

    def test_consulta_municipios_na_regiao(self):
        ctrl.consulta_municipios_na_regiao(self.request)

    def test_consulta_ocorrencias_por_municipio(self):
        ctrl.consulta_ocorrencias_por_municipio(self.request)
