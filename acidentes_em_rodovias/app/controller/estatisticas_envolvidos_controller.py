#!/usr/bin/env python
# coding: utf-8

"""Acidentes em Rodovias

 Universidade de Brasilia - FGA
 Técnicas de Programação, 1/2014

Parser responsable to return to HTML inquiry about statistics
involved in the accident.
"""

import sys
import os
import inspect
import MySQLdb
import logging

# Adding upper directories to the Python Path
#from app import *
from app.util.estatisticas_util import *
from app.exception.internal_exceptions import *
from app.models.dao.envolvidos_acidentes_dao import *
from app.models.dao.pessoas_acidentes_dao import *

from django.utils.datastructures import MultiValueDictKeyError
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response

from datetime import datetime

# Logging config
logging.basicConfig()
logger = logging.getLogger(__name__)


def ocorrencias_e_envolvidos(request):
    """ Return the render with the statistics from
    involved in the accident. """

    envolvidosDAO = EnvolvidosAcidentesDAO()
    lista_envolvidos = envolvidosDAO.envolvidos_acidentes()
    medias, desvio = envolvidosDAO.media_desvio_envolvidos()
    anos = []

    for acidente in lista_envolvidos:
        anos.append(acidente.ano)

    ano_media_list = zip(anos, medias)

    return render_to_response(
        "ocorrencias-e-envolvidos.html", {
            'lista_envolvidos': lista_envolvidos,
            'ano_media_list': ano_media_list,
            'desvio': desvio
        }, context_instance=RequestContext(request)
    )


def acidentes_sexo(request):
    """ Return the render with the statistics from
    involved in the accident by gender. """
    try:
        pessoas_dao = PessoasAcidentesDAO()
        homens_ano = pessoas_dao.acidentes_por_sexo_e_ano('M')
        mulheres_ano = pessoas_dao.acidentes_por_sexo_e_ano('F')
        homens_geral = pessoas_dao.acidentes_por_sexo_geral('M')
        mulheres_geral = pessoas_dao.acidentes_por_sexo_geral('F')
        homens_geral, mulheres_geral = media_sexo(homens_geral, mulheres_geral)

    except (MySQLdb.Error, ResultadoConsultaNuloError) as e:
        logger.error(str(e))
        erro = "Ocorreu um erro no sistema, tente novamente mais tarde!"
        return render_to_response(
            "index.html", {
                'erro': erro
            }, context_instance=RequestContext(request)
        )

    return render_to_response(
        "acidentes_sexo.html", {
            'homens_geral': homens_geral,
            'mulheres_geral': mulheres_geral,
            'homens_ano': homens_ano,
            'mulheres_ano': mulheres_ano
        }, context_instance=RequestContext(request)
    )
