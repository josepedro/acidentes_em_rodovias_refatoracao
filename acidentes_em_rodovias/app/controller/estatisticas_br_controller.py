#!/usr/bin/env python
# coding: utf-8

"""Acidentes em Rodovias

 Universidade de Brasilia - FGA
 Técnicas de Programação, 1/2014

Parser responsable to return to HTML inquiry about statistics.
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

from models.dao.br_acidentes_dao import *

from datetime import datetime

# Adding upper directories to the Python Path
current_path = os.path.dirname(os.path.abspath('..'))
sys.path.append(current_path)
current_path = os.path.dirname(os.path.abspath('.'))
sys.path.append(current_path)

# Logging config
logging.basicConfig()
logger = logging.getLogger(__name__)


def acidentes_br(request):
    try:
        data = datetime.now()
        br_dao = BRAcidentesDAO()
        br_acidentes_geral = br_dao.acidentes_br_geral()
        acidentes_ano = br_dao.acidentes_br_ano()

    except (MySQLdb.Error, ResultadoConsultaNuloError) as e:
        logger.error(str(e))
        erro = "Ocorreu um erro no sistema, tente novamente mais tarde!"
        return render_to_response(
            "index.html", {
                'erro': erro
            }, context_instance=RequestContext(request)
        )

    return render_to_response(
        "br_acidentes.html", {
            'ano': range(2007, data.year + 1),
            'br_acidentes_geral': br_acidentes_geral,
            'acidentes_ano': acidentes_ano
        }, context_instance=RequestContext(request)
    )
