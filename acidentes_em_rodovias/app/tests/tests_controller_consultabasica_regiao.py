# -*- coding: utf-8 -*- 
import sys, os, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from django.test import SimpleTestCase
from django.template import RequestContext, TemplateDoesNotExist, Context
from controller import consultabasica_regiao_controller as ctrl
from _mysql_exceptions import *
from nose import with_setup
from mock import MagicMock,patch,Mock
from django.utils.datastructures import MultiValueDictKeyError

class Test_Regiao(SimpleTestCase):
	"""docstring for Test_Regiao"""
	def setUp(self):    #configura ambiente para teste
		self.request     = Context()
		self.request.GET = dict()
		self.request.GET['uf_id'] = 'DF'
		self.request.GET['municipio_id'] = 'Brasilia'
		#descobre qual metodo será chamado e formata a saída
		func = str(self.id).split('=')[-1][:-2]
		func = func.split('test_')[-1]
		func = func.replace('_',' ')
		out = '\rTeste de ' + func + ' '
		out = out.ljust(65,'-')
		sys.stderr.write(out)
		self.shortDescription()

	def tearDown(self):
		# informa que o teste foi realizado
		#print 'Done'                                
		sys.stderr.write('Done\n')
	
	def shortDescription(self):
		return "Teste da classe Test_Regiao"

	def test_consulta_por_regiao(self):
		ctrl.consulta_por_regiao(None)

	def test_consulta_municipios_na_regiao(self):
		ctrl.consulta_municipios_na_regiao(self.request)
	
	def test_consulta_ocorrencias_por_municipio(self):
		ctrl.consulta_ocorrencias_por_municipio(self.request)
