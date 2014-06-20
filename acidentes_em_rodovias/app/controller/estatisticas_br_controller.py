#!/usr/bin/env python
# coding: utf-8

"""Acidentes em Rodovias

 Universidade de Brasilia - FGA
 Técnicas de Programação, 1/2014

Parser responsable to return to HTML inquiry about statistics.
"""
import MySQLdb
import logging

from django.template import RequestContext
from django.shortcuts import render_to_response

from app.exception.internal_exceptions import ResultadoConsultaNuloError
from app.dao.br_acidentes_dao import BRAcidentesDAO

from datetime import datetime

# Logging config
logging.basicConfig()
logger = logging.getLogger(__name__)

_FIRST_YEAR = 2007


def acidentes_br(request):
    """ Return the render from statistics. """

    try:
        data = datetime.now()
        br_dao = BRAcidentesDAO()
        br_overall_accidents = br_dao.acidentes_br_geral()
        accidents_ano = br_dao.acidentes_br_ano()

    except (MySQLdb.Error, ResultadoConsultaNuloError):
        # logger.error(str(e))
        erro = "Ocorreu um erro no sistema, tente novamente mais tarde!"
        return render_to_response(
            "index.html", {
                'erro': erro
            }, context_instance=RequestContext(request)
        )

    response = render_to_response(
        "br_acidentes.html", {
            'ano': range(2007, data.year + 1),
            'br_acidentes_geral': br_overall_accidents,
            'acidentes_ano': accidents_ano
        }, context_instance=RequestContext(request)
    )

    return response
