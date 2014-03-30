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

from models.dao.ocorrencia_basica_dao import *

from exception.validation_exceptions import *
from exception.internal_exceptions import *

from util.validacao_util import *

# Adding upper directories to the Python Path
current_path = os.path.dirname(os.path.abspath('..'))
sys.path.append(current_path)
current_path = os.path.dirname(os.path.abspath('.'))
sys.path.append(current_path)

# Logging config
logging.basicConfig()
logger = logging.getLogger(__name__)


def consulta_por_periodo(request):
    """ Return the render of page with inquiry in time. """

    return render_to_response(
        "periodo.html",
        context_instance=RequestContext(request)
    )


def consulta_ocorrencias_por_periodo(request):
    """ Return the render of page with occurrences inquiry in time. """

    try:
        data_inicio = str(request.GET['data_inicio'])
        data_fim = str(request.GET['data_fim'])
    except (MultiValueDictKeyError) as e:
        logger.error(str(e))
        erro = "Preencha corretamente o formulário!"
        return render_to_response(
            "index.html", {
                'erro': erro
            }, context_instance=RequestContext(request)
        )

    try:
        valida_data(data_inicio)
        valida_data(data_fim)
    except DataInvalidaError as e:
        logger.error(str(e))
        erro = "Preencha corretamente o formulário!"
        return render_to_response(
            "index.html", {
                'erro': erro
            }, context_instance=RequestContext(request)
        )

    try:
        ocorrencia_dao = OcorrenciaBasicaDAO()
        ocorrencia_list = ocorrencia_dao.lista_ocorrencias_por_periodo(
            data_inicio, data_fim, 1000)
    except (MySQLdb.Error, ResultadoConsultaNuloError) as e:
        logger.error(str(e))
        erro = "Ocorreu um erro no sistema, tente novamente mais tarde!"
        return render_to_response(
            "index.html", {
                'erro': erro
            }, context_instance=RequestContext(request)
        )

    return render_to_response(
        "resultado.html", {
            'ocorrencia_list': ocorrencia_list,
            'tipo_consulta': 'periodo',
            'data_inicio': data_inicio,
            'data_fim': data_fim
        }, context_instance=RequestContext(request)
    )
