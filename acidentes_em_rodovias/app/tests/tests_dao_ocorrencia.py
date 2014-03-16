# -*- coding: utf-8 -*- 
import sys, os, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from django.test import SimpleTestCase
from django.core.urlresolvers import reverse, resolve
from models.dao import generico_dao,uf_dao,ocorrencia_basica_dao,municipio_dao
from _mysql_exceptions import OperationalError, ProgrammingError
from exception.internal_exceptions import *



class TestOcorrencia(SimpleTestCase):
	"""docstring for TestOcorrencia"""
	def setUp(self):    #configura ambiente para teste
		self.ocorrencia = ocorrencia_basica_dao.OcorrenciaBasicaDAO()
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
		sys.stderr.write('Done\n')

	def shortDescription(self):
		return "Teste da classe OcorrenciaBasica"

	def test_existing_ocorrencia_dao_instance(self):
		self.assertIsNotNone(self.ocorrencia)

	def test_ocorrencia_por_regiao(self):
		# 97012 = Brasilia
		oco =  self.ocorrencia.lista_ocorrencias_por_regiao(97012)
		self.assertIsNotNone(oco)   #verifica se não retorna nulo
		oco =  self.ocorrencia.lista_ocorrencias_por_regiao(97012,limite=3)
		self.assertIsNotNone(oco)   #verifica se não retorna nulo
		self.assertLess(len(oco),4) #verifica se retorna no maximo 3 ocorrencias
		for i in oco:               #verifica se todos os retornos estão no DF
			self.assertIsNotNone(str(i))
			self.assertEqual(i.tmuuf, 'DF')


	def test_ocorrencia_por_periodo(self):
		oco =  self.ocorrencia.lista_ocorrencias_por_periodo('06/01/06','06/12/06')
		self.assertIsNotNone(oco)   #verifica se não retorna nulo
		oco =  self.ocorrencia.lista_ocorrencias_por_periodo('06/01/06','06/12/06',limite=3)
		self.assertIsNotNone(oco)   #verifica se não retorna nulo
		self.assertLess(len(oco),4) #verifica se retorna no maximo 3 ocorrencias
		for i in oco:               #verifica se as ocorrencias aconteceram em 2006
			self.assertEqual(2006, i.ocodataocorrencia.year)
			
