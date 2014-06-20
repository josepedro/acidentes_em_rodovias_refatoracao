#!/usr/bin/env python
# coding: utf-8

"""Acidentes em Rodovias

 Universidade de Brasilia - FGA
 Técnicas de Programação, 1/2014

Parser responsable to return to HTML inquiry about statistics
involved in the accident.
"""
import MySQLdb
import logging

from app.util.estatisticas_util import media_sexo
from app.exception.internal_exceptions import ResultadoConsultaNuloError

from app.dao.envolvidos_acidentes_dao import EnvolvidosAcidentesDAO
from app.dao.pessoas_acidentes_dao import PessoasAcidentesDAO

from django.template import RequestContext
from django.shortcuts import render_to_response

# Logging config
logging.basicConfig()
logger = logging.getLogger(__name__)


def ocorrencias_e_envolvidos(request):
    """ Return the render with the statistics from
    involved in the accident. """

    involved_dao = EnvolvidosAcidentesDAO()
    involved_list = involved_dao.envolvidos_acidentes()
    medias, desvio = involved_dao.media_desvio_envolvidos()
    years = get_years_list(involved_list)

    year_average_list = zip(years, medias)

    response = render_to_response(
        "ocorrencias-e-envolvidos.html", {
            'lista_envolvidos': involved_list,
            'ano_media_list': year_average_list,
            'desvio': desvio
        }, context_instance=RequestContext(request)
    )

    return response


def get_years_list(involved_list):
    years = []

    for accident in involved_list:
        years.append(accident.ano)

    return years


def acidentes_sexo(request):
    """ Return the render with the statistics from
    involved in the accident by gender. """
    try:
        people_dao = PessoasAcidentesDAO()
        men_year = people_dao.acidentes_por_sexo_e_ano('M')
        women_year = people_dao.acidentes_por_sexo_e_ano('F')
        men_general = people_dao.acidentes_por_sexo_geral('M')
        women_general = people_dao.acidentes_por_sexo_geral('F')
        men_general, women_general = media_sexo(men_general, women_general)

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
        "acidentes_sexo.html", {
            'homens_geral': men_general,
            'mulheres_geral': women_general,
            'homens_ano': men_year,
            'mulheres_ano': women_year
        }, context_instance=RequestContext(request)
    )

    return response
