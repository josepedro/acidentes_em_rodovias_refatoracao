# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#

from django.test import SimpleTestCase, Client
from sys import stderr
from app import myconfiguration
from app.dao.generico_dao import GenericoDAO


class Basic_Tests(SimpleTestCase):

    """Basic test class"""
    name = ''
    my_type = ''

    def getName(self):
        """ Get the name of the test """
        self.name = str(self.id).split('=')[-1][:-2]
        self.name = self.name.split('test_')[-1]
        self.name = self.name.replace('_', ' ')

    def __str__(self):
        self.getName()
        out = '\r[DAO] Teste de ' + self.name + ' '
        out = '\r%s Teste de %s ' % (self.my_type, self.name)
        out = out.ljust(70, '-')
        return out

    def tearDown(self):
        stderr.write(' Done\n')

    def shortDescription(self):
        return "Teste da classe %s" % self.__class__.__name__


class Validate_Tests(Basic_Tests):

    """Basic test class to Validations"""

    def setUp(self):
        self.my_type = '[Validation]'
        stderr.write(self.__str__())
        self.shortDescription()


class Util_Estatisticas(Basic_Tests):

    """Basic test class to Util_Estatisticas"""

    def setUp(self):
        self.my_type = '[Estatisticas]'
        stderr.write(self.__str__())
        self.shortDescription()


class Controller_Tests(Basic_Tests):

    """Basic test class to Controller"""

    def setUp(self):
        self.my_type = '[Controller]'
        stderr.write(self.__str__())
        self.shortDescription()
        self.client = Client()
        self.db_password = myconfiguration.DB_PASS


class DAO_Tests(Basic_Tests):

    """Basic test class to DAO"""

    def setUp(self):
        self.my_type = '[DAO]'
        stderr.write(self.__str__())
        self.shortDescription()
        self.dao = GenericoDAO()


class Index_Tests(Basic_Tests):

    """Basic test class to DAO"""

    def setUp(self):
        self.my_type = '[Index]'
        stderr.write(self.__str__())
        self.shortDescription()
        self.client = Client()
