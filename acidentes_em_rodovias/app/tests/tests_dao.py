# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#
from app.tests.tests_basic import DAO_Tests

from _mysql_exceptions import OperationalError, ProgrammingError

from app.models import envolvidos_acidentes, causas_acidentes
from app.dao.generico_dao import GenericoDAO

from app.exception.internal_exceptions import ResultadoConsultaNuloError
from app.exception.internal_exceptions import DataInvalidaError
from app.exception.validation_exceptions import ParametroInseguroClienteError


class TestDAO(DAO_Tests):

    """docstring for TestDAO
        Class that tests the methods from generico_dao
    """

    def test_existing_dao_instance(self):
        """
        Tests to see if the class is correctly instanced.
        """

        self.dao = GenericoDAO()

        self.assertIsNotNone(self.dao)

    def test_get_conexao(self):
        """
        Tests the connection.
        Expects an error in case the method has at least one of it's
        parameters not set.
        """

        self.dao = GenericoDAO()

        # Field to insert database
        self.dao.database = ' '
        # Field to insert user
        self.dao.usuario = ' '
        # Field to insert password
        self.dao.senha = ' '
        # Field to insert host
        self.dao.host = ' '
        # self.assertIsNone(self.dao.get_conexao())
        with self.assertRaises(OperationalError):
            self.dao.get_conexao()

    def test_try_query(self):
        """
        Tests the execution of a query.
        Expects an error in case the table selected does not exist.
        """

        self.dao = GenericoDAO()

        with self.assertRaises(ProgrammingError):
            self.assertIsNone(self.dao.executa_query("show * from jik;"))
        self.assertIsNotNone(self.dao.executa_query("show tables;"))

    def test_transforma_objeto(self):
        """
        Tests the transformation of the query results to a model object.
        If the query is correctly selected, tests that it goes through the IF
        and ELSE of the FOR loop.
        After, it tests if the list isn't empty and raises an exception in
        case it fails to transform the query.

        @brief Local variable
            query -
                SQL instruction that queries the UFs and their names.
            ufList -
                Receives the query results after they become model objects.
        """

        self.dao = GenericoDAO()
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
        self.dao = GenericoDAO()

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
