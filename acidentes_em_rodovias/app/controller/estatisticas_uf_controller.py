#!/usr/bin/env python
# coding: utf-8

"""Acidentes em Rodovias

 Universidade de Brasilia - FGA
 Técnicas de Programação, 1/2014

Parser responsable to return to HTML the the abbreviation (UF)
of the states from Brazil.
"""

import sys
import os
import inspect
import MySQLdb
import logging

from django.utils.datastructures import MultiValueDictKeyError
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response

from exception.validation_exceptions import *
from exception.internal_exceptions import *

from models.dao.uf_acidentes_dao import *

from datetime import datetime

# Adding upper directories to the Python Path
from app import *

""" Logging config """
logging.basicConfig()
logger = logging.getLogger(__name__)


def acidentes_uf(request):
    """ Return the render with the accidents by states. """

    try:
        data = datetime.now()
        uf_dao = UFAcidentesDAO()
        uf_acidentes_geral = uf_dao.acidentes_uf_geral()
        uf_acidentes_ano = uf_dao.acidentes_uf_ano()

    except (MySQLdb.Error, ResultadoConsultaNuloError) as e:
        logger.error(str(e))
        erro = "Ocorreu um erro no sistema, tente novamente mais tarde!"
        return render_to_response(
            "index.html", {
                'erro': erro
            }, context_instance=RequestContext(request)
        )

    return render_to_response(
        "uf_acidentes.html", {
            'ano': range(2007, data.year + 1),
            'uf_acidentes_ano': uf_acidentes_ano,
            'uf_acidentes_geral': uf_acidentes_geral[:10],
            'uf_acidentes_geral_mapa': uf_acidentes_geral
        }, context_instance=RequestContext(request)
    )
