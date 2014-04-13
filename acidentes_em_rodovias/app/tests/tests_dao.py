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

    """docstring for TestDAO
        Class that tests the methods from generico_dao
    """

    def setUp(self):  # configura ambiente para teste
        """
        Configures the ambient for test.

        @brief Local variables:
            x -
                Receives the import from models.dao.generico_dao.
            func - 
                Gets the name of the test function and fixes it for the output.
            out -
                Writes the name of the test function that is being proccessed.
        """
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
        """
        Informs that the test was executed.
        """
        # informa que o teste foi realizado
        sys.stderr.write('Done\n')

    def shortDescription(self):
        """
        Gives a description of the class being tested.
        """
        return "Teste da classe GenericoDAO"

    def test_existing_dao_instance(self):
        """
        Tests to see if the class is correctly instanced.
        """
        self.assertIsNotNone(self.dao)

    def test_get_conexao(self):
        """
        Tests the connection. 
        Expects an error in case the method has at least on of it's parameters not set.
        """
        self.dao.database = ' '
        self.dao.usuario = ' '
        self.dao.senha = ' '
        self.dao.host = ' '
        # self.assertIsNone(self.dao.get_conexao())
        with self.assertRaises(OperationalError):
            self.dao.get_conexao()

    def test_try_query(self):
        """
        Tests the execution of a query.
        Expects an error in case the table selected does not exist.
        """
        with self.assertRaises(ProgrammingError):
            self.assertIsNone(self.dao.executa_query("show * from jik;"))
        self.assertIsNotNone(self.dao.executa_query("show tables;"))

    def test_transforma_objeto(self):
        """
        Tests the transformation of the query results to a model object.
        If the query is correctl selected, tests it goes through the IF and ELSE of the FOR loop.
        After it tests if the list isn't empty and end with the exception in case it fails to transform the query. 
        """
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
        """
        Tests that the objects were correctly instanced.
        """
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
