#!/usr/bin/env python
# coding: utf-8

"""Acidentes em Rodovias

 Universidade de Brasilia - FGA
 Técnicas de Programação, 1/2014

Parser responsable to return to HTML inquiry in time/period.
"""

import sys
import os
import inspect
import logging
import MySQLdb

from django.utils.datastructures import MultiValueDictKeyError
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response

from app.models.dao.ocorrencia_basica_dao import *

from app.exception.validation_exceptions import *
from app.exception.internal_exceptions import *

from app.util.validacao_util import *

# Logging config
logging.basicConfig()

# Logger object
logger = logging.getLogger(__name__)

_MAX_QUERIES = 1000


def consulta_por_periodo(request):
    """ Return the render of page with inquiry in time.
    @param request context request from view
    @return HTML page with inquiry in time.
    """

    return render_to_response(
        "periodo.html",
        context_instance=RequestContext(request)
    )


def define_dates(request):
    """ Return the strt and end date.
    @param request context request from view.
    @return return the date
    """

    try:
        # string with the initial date
        start_date = str(request.GET['data_inicio'])
        # string with the final date
        end_date = str(request.GET['data_fim'])
    except (MultiValueDictKeyError) as e:
        logger.error(str(e))
        erro = "Preencha corretamente o formulário!"
        return render_to_response(
            "index.html", {
                'erro': erro
            }, context_instance=RequestContext(request)
        )

    return start_data, end_date


def validate_date(start_data, end_date):
    """ Validate two dates
    @param start_data Initial date.
    @param end_data Final date.
    @return True if a valid date.
    """

    try:
        valida_data(start_date)
        valida_data(end_date)
    except DataInvalidaError as e:
        logger.error(str(e))
        erro = "Preencha corretamente o formulário!"
        return render_to_response(
            "index.html", {
                'erro': erro
            }, context_instance=RequestContext(request)
        )
    return True


def build_list_occurences(start_data, end_date):
    """ Creates a list of occurrences
    @param start_data Initial date.
    @param end_data Final date.
    @return List of occurrences
    """

    try:
        # DAO object from basic occurrence
        occurrences_dao = OcorrenciaBasicaDAO()
        # list of occurrences
        occurrences_list = occurrences_dao.lista_ocorrencias_por_periodo(
            start_date, end_date, _MAX_QUERIES)
    except (MySQLdb.Error, ResultadoConsultaNuloError) as e:
        logger.error(str(e))
        erro = "Ocorreu um erro no sistema, tente novamente mais tarde!"
        return render_to_response(
            "index.html", {
                'erro': erro
            }, context_instance=RequestContext(request)
        )
    return occurrences_list


def consulta_ocorrencias_por_periodo(request):
    """ Return the render of page with occurrences inquiry in time.
    @param request context request from view.
    @return If no errors, return the occurrences page, otherwise,
    returns the index page with error message.
    """

    start_data, end_date = define_dates(request)
    assert(True, validate_date(start_data, end_date))
    occurrences_list = build_list_occurences(start_data, end_date)

    render = render_to_response(
        "resultado.html", {
            'ocorrencia_list': occurrences_list,
            'tipo_consulta': 'periodo',
            'start_date': start_date,
            'end_date': end_date
        }, context_instance=RequestContext(request)
    )

    return render
