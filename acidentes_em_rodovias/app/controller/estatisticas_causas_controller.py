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

from app.exception.validation_exceptions import *
from app.exception.internal_exceptions import *

from app.models.dao.causas_acidentes_dao import *

from datetime import datetime

# Logging config
logging.basicConfig()
## logger object
logger = logging.getLogger(__name__)


def causas_acidentes(request):
    """ Return the render of the page with statistics of causes of accidents.
    @param request context request from view
    @return HTML page with statistics of causes of accidents.
    """

    try:
        ## DAO object of causes
        causas_dao = CausasAcidentesDAO()
        ## List of causes
        causas_list = causas_dao.causas_acidentes()
        ## List of years by causes
        causas_ano_list = causas_dao.causas_acidentes_ano()
        ## List of statistics by causes
        probabilidade_causas_list = causas_dao.probabilidade_causas_acidentes()
        ## List of means
        media_desvio_list = causas_dao.media_desvio_causas_acidentes()

        # clean the list causes
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
