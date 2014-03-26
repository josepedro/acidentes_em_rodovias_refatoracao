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

from django.test import SimpleTestCase
from django.core.urlresolvers import reverse, resolve

from models.dao import *
from models import envolvidos_acidentes, causas_acidentes

from _mysql_exceptions import OperationalError, ProgrammingError

from exception.internal_exceptions import *
from exception.validation_exceptions import *

# Adding upper directories to the Python Path
current_path = os.path.dirname(os.path.abspath('..'))
sys.path.append(current_path)
current_path = os.path.dirname(os.path.abspath('.'))
sys.path.append(current_path)


class TestDAO(SimpleTestCase):

    """docstring for TestDAO"""

    def setUp(self):  # configura ambiente para teste
        x = __import__('models.dao.generico_dao')
        self.dao = x.dao.generico_dao.GenericoDAO()
        # help(x.dao.generico_dao)
        #sys.stderr.write('\n' + str(x) + '\n' )
        # descobre qual metodo será chamado e formata a saída
        func = str(self.id).split('=')[-1][:-2]
        func = func.split('test_')[-1]
        func = func.replace('_', ' ')
        out = '\rTeste de ' + func + ' '
        out = out.ljust(65, '-')
        sys.stderr.write(out)
        self.shortDescription()

    def tearDown(self):
        # informa que o teste foi realizado
        sys.stderr.write('Done\n')

    def shortDescription(self):
        return "Teste da classe GenericoDAO"

    def test_existing_dao_instance(self):
        self.assertIsNotNone(self.dao)

    def test_get_conexao(self):
        self.dao.database = ' '
        self.dao.usuario = ' '
        self.dao.senha = ' '
        self.dao.host = ' '
        # self.assertIsNone(self.dao.get_conexao())
        with self.assertRaises(OperationalError):
            self.dao.get_conexao()

    def test_try_query(self):
        with self.assertRaises(ProgrammingError):
            self.assertIsNone(self.dao.executa_query("show * from jik;"))
        self.assertIsNotNone(self.dao.executa_query("show tables;"))

    def test_transforma_objeto(self):
        # Quando tudo funciona bem
        query = """SELECT tufuf, tufdenominacao FROM uf
                WHERE tufuf = 'DF' ORDER BY tufdenominacao;"""
        # Testa se passa no 'if' e 'else' do for
        ufList = self.dao.transforma_dicionario_em_objetos(
            self.dao.executa_query(query),
            'Uf',
            'uf'
        )
        self.assertEquals(ufList[0].tufuf, 'DF')
        # Testa se a lista nao esta vazia.
        self.assertIsNotNone(self.dao.transforma_dicionario_em_objetos(
            self.dao.executa_query(query),
            'Uf',
            'uf')
        )
        # Testa exception
        with self.assertRaises(ResultadoConsultaNuloError):
            self.assertIsNone(self.dao.transforma_dicionario_em_objetos(
                None,
                'Uf',
                'uf')
            )

    def test_instancia_objetos(self):
        self.assertIsNotNone(causas_acidentes.Acidentes())
        self.assertIsNotNone(str(causas_acidentes.Acidentes()))
        self.assertIsNotNone(causas_acidentes.AcidentesAno())
        self.assertIsNotNone(str(causas_acidentes.AcidentesAno()))
        self.assertIsNotNone(str(causas_acidentes.ProbabilidadeAcidentes()))
        self.assertIsNotNone(str(causas_acidentes.MediaDesvioAcidentes()))
        self.assertIsNotNone(str(envolvidos_acidentes.EnvolvidosAcidente()))
        self.assertIsNotNone(str(ResultadoConsultaNuloError("Test")))
        self.assertIsNotNone(str(DataInvalidaError("Test")))
        self.assertIsNotNone(str(ParametroInseguroClienteError("Test")))
