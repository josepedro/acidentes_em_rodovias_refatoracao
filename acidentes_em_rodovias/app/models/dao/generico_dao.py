# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#

"""@package Envolvidos Acidentes DAO
Data Access Object (DAO) para causa de acidentes nas BRs.

This module contains the class declaration that accesses
data in the database and exports them to the controller
"""

import sys
import os
import inspect

import app.myconfiguration as myconfiguration
import MySQLdb
import importlib
import logging

import pandas.io.sql as psql

from app.exception.internal_exceptions import *

# Logging config
logging.basicConfig()
""" Logger object """
logger = logging.getLogger(__name__)


class GenericoDAO:

    """Creates Database connection, executes queries and transform queries
    results in objects
    """

    def __init__(self):
        """ Constructor method.
        Set the values to get a valid connection
        """

        # Database's username
        self.usuario = myconfiguration.DB_USER
        # Database's schema name
        self.database = myconfiguration.DB
        # Database's password
        self.senha = myconfiguration.DB_PASS
        # Database's host
        self.host = myconfiguration.HOST
        # Receives a connection with the Database
        self.conexao = self.get_conexao()

    def get_conexao(self):
        """ Starts and returns a connection with the Database
        @return A MySQL connection object
        """

        conexao = MySQLdb.connect(
            self.host,
            self.usuario,
            self.senha,
            self.database
        )
        return conexao

    def executa_query(self, query, get_data_frame=False):
        """ Executes a SQL query.

            @brief Local variable:

                dados - 
                    Receives the query result

            @param query A SQL instruction
            @param get_data_frame   Determines the format of the query results.
                Sets False as default
            @return Query with the result
        """

        dados = None

        if (get_data_frame is False):
            dados = psql.frame_query(
                query,
                con=self.conexao
            ).to_dict()
        else:
            dados = psql.frame_query(
                query,
                con=self.conexao
            )

        if (dados is None):
            raise ResultadoConsultaNuloError(
                "A biblioteca pandas não está instalada, " +
                "ou nenhum dado foi passado a esse método"
            )
        else:
            return dados

    def transforma_dicionario_em_objetos(self, dados, classe, modulo):
        """ Transforms the query results in a model object

        @brief Local variables:

            modulo_classe -
                Receives the module inserted into sys.modules

            lista_objetos -
                A list of the objects that will be returned

            chaves -
                Receives the keys of the query dictionary

            instancia -
                Instance of a determined object

            @param dados Databank fields.
            @param classe Determines the Class of the model object.
            @param modulo Indicates the name of the module that the class is.
            @return List os objects build by query results
        """
        modulo_classe = importlib.import_module("app.models." + modulo)
        class_ = getattr(
            modulo_classe,
            classe
        )
        lista_objetos = []

        try:
            chaves = dados.keys()
        except AttributeError as e:
            raise ResultadoConsultaNuloError(
                "A biblioteca pandas não está instalada," +
                "ou nenhum dado foi passado a esse método"
            )

        for i in range(0, len(dados[chaves[0]])):
            instancia = class_()
            for chave in chaves:
                if (isinstance(dados[chave][i], basestring)):
                    setattr(instancia, chave, dados[chave][
                            i].decode('iso-8859-1').encode('utf8'))
                else:
                    setattr(instancia, chave, dados[chave][i])
            lista_objetos.append(instancia)

        return lista_objetos
