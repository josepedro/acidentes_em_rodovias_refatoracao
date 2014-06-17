#!/usr/bin/env python
# coding: utf-8

"""Acidentes em Rodovias

 Universidade de Brasilia - FGA
 Técnicas de Programação, 1/2014

Parser responsable to return to HTML inquiry about kinds of accidents.
"""
import MySQLdb
import logging

from django.template import RequestContext
from django.shortcuts import render_to_response

from app.exception.internal_exceptions import ResultadoConsultaNuloError
from app.models.dao.tipos_acidentes_dao import TiposAcidentesDAO

# Logging config
logging.basicConfig()
logger = logging.getLogger(__name__)


def tipos_acidentes(request):
    """ Return the render with the kinds of accidents. """

    try:
        type_dao = TiposAcidentesDAO()
        types_accidents_list = type_dao.tipos_acidentes()
        types_accidents_year_list = type_dao.tipos_acidentes_ano()
        probability_list = type_dao.probabilidade_tipos_acidentes()
        average_deviation_list = type_dao.media_desvio_tipos_acidentes()

        type_list = get_type_list(probability_list)

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
        "tipos_acidentes.html", {
            'tipos_acidentes_list': types_accidents_list,
            'tipos_acidentes_ano_list': types_accidents_year_list,
            'anos': types_accidents_year_list[0].ano_list,
            'probabilidade_tipos_acidentes_list': probability_list,
            'tipos': type_list,
            'media_desvio_tipos_acidentes_list': average_deviation_list,
        }, context_instance=RequestContext(request)
    )

    return response


def get_type_list(probability_list):
    type_list = []
    for accident in probability_list:
            type_list.append(accident.tipo)

    return type_list
