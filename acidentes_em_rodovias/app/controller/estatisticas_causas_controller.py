#!/usr/bin/env python
# coding: utf-8

"""Acidentes em Rodovias

 Universidade de Brasilia - FGA
 Técnicas de Programação, 1/2014

Parser responsable to return to HTML inquiry about statistics of
causes of accidents.
"""
import MySQLdb
import logging

from django.template import RequestContext
from django.shortcuts import render_to_response

from app.exception.internal_exceptions import ResultadoConsultaNuloError

from app.dao.causas_acidentes_dao import CausasAcidentesDAO

# Logging config
logging.basicConfig()
# logger object
logger = logging.getLogger(__name__)


def causas_acidentes(request):
    """ Return the render of the page with statistics of causes of accidents.
    @param request context request from view
    @return HTML page with statistics of causes of accidents.
    """

    try:
        # DAO object of causes
        causes_dao = CausasAcidentesDAO()
        # List of causes
        causes_list = causes_dao.causas_acidentes()
        # List of years by causes
        causes_year_list = causes_dao.causas_acidentes_ano()
        # List of statistics by causes
        probability_causes_list = causes_dao.probabilidade_causas_acidentes()
        # List of means
        average_deviation_list = causes_dao.media_desvio_causas_acidentes()

    except (MySQLdb.Error, ResultadoConsultaNuloError):
        # logger.error(str(e))
        erro = "Ocorreu um erro no sistema, tente novamente mais tarde!"
        response = render_to_response(
            "index.html", {
                'erro': erro
            }, context_instance=RequestContext(request)
        )

        return response

    response = render_to_response(
        "causas_acidentes.html", {
            'causas_acidentes_list': causes_list,
            'causas_acidentes_ano_list': causes_year_list,
            'anos': causes_year_list[0].ano_list,
            'probabilidade_causas_acidentes_list': probability_causes_list,
            'causas': causes_list,
            'media_desvio_causas_acidentes_list': average_deviation_list,
        }, context_instance=RequestContext(request)
    )

    return response
