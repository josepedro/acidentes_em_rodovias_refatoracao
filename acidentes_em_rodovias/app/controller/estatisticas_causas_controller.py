#!/usr/bin/env python
# coding: utf-8

"""Acidentes em Rodovias

 Universidade de Brasilia - FGA
 Técnicas de Programação, 1/2014

Parser responsable to return to HTML inquiry about statistics of
causes of accidents.
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

from models.dao.causas_acidentes_dao import *

from datetime import datetime

# Adding upper directories to the Python Path
current_path = os.path.dirname(os.path.abspath('..'))
sys.path.append(current_path)
current_path = os.path.dirname(os.path.abspath('.'))
sys.path.append(current_path)

# Logging config
logging.basicConfig()
logger = logging.getLogger(__name__)


def causas_acidentes(request):
    """ Return the render of the page with statistics of
causes of accidents.. """
    try:
        causas_dao = CausasAcidentesDAO()
        causas_list = causas_dao.causas_acidentes()
        causas_ano_list = causas_dao.causas_acidentes_ano()
        probabilidade_causas_list = causas_dao.probabilidade_causas_acidentes()
        media_desvio_list = causas_dao.media_desvio_causas_acidentes()

        causas_list = []
        for acidente in probabilidade_causas_list:
            causas_list.append(acidente.causa)
    except (MySQLdb.Error, ResultadoConsultaNuloError) as e:
        logger.error(str(e))
        erro = "Ocorreu um erro no sistema, tente novamente mais tarde!"
        return render_to_response(
            "index.html", {
                'erro': erro
            }, context_instance=RequestContext(request)
        )

    return render_to_response(
        "causas_acidentes.html", {
            'causas_acidentes_list': causas_list,
            'causas_acidentes_ano_list': causas_ano_list,
            'anos': causas_ano_list[0].ano_list,
            'probabilidade_causas_acidentes_list': probabilidade_causas_list,
            'causas': causas_list,
            'media_desvio_causas_acidentes_list': media_desvio_list,
        }, context_instance=RequestContext(request)
    )
