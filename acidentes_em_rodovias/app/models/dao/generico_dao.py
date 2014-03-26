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

# Adding upper directories to the Python Path
current_path = os.path.dirname(os.path.abspath('..'))
sys.path.append(current_path)
current_path = os.path.dirname(os.path.abspath('.'))
sys.path.append(current_path)

import myconfiguration
import MySQLdb
import importlib
import logging

import pandas.io.sql as psql

from exception.internal_exceptions import *

# Logging config
logging.basicConfig()
logger = logging.getLogger(__name__)


class GenericoDAO:

    """Classe pai de todas as DAO's"""

    def __init__(self):
        self.usuario = myconfiguration.DB_USER
        self.database = myconfiguration.DB
        self.senha = myconfiguration.DB_PASS
        self.host = myconfiguration.HOST
        self.conexao = self.get_conexao()

    def get_conexao(self):
        conexao = MySQLdb.connect(
            self.host,
            self.usuario,
            self.senha,
            self.database
        )
        return conexao

    def executa_query(self, query, get_data_frame=False):
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
        modulo_classe = importlib.import_module("models." + modulo)
        class_ = getattr(
            modulo_classe,
            classe
        )
        lista_objetos = []

        try:
            chaves = dados.keys()
        except AttributeError, e:
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
