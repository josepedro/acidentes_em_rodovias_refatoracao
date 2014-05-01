#!/usr/bin/env python
# coding: utf-8

"""Acidentes em Rodovias

 Universidade de Brasilia - FGA
 Técnicas de Programação, 1/2014

Parser responsable to return to HTML inquiry about region.
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

from app.models.dao.uf_dao import *
from app.models.dao.municipalities_dao import *
from app.models.dao.ocorrencia_basica_dao import *

from app.exception.validation_exceptions import *
from app.exception.internal_exceptions import *

from app.util.validacao_util import *

# Logging config
logging.basicConfig()
## logger object
logger = logging.getLogger(__name__)


def consulta_por_regiao(request):
    """ Return the render from page with query by region.
    @param request context request from view
    @return HTML page with query by region.
    """

    try:
        ## object DAO from UF
        uf_dao = UfDAO()
        ## list of UFs
        uf_list = uf_dao.lista_ufs()
    except (MySQLdb.Error, ResultadoConsultaNuloError) as e:
        logger.error(str(e))
        erro = "Ocorreu um erro no sistema, tente novamente mais tarde!"
        return render_to_response(
            "index.html", {
                'erro': erro
            }, context_instance=RequestContext(request)
        )

    return render_to_response(
        "regiao.html", {
            'uf_list': uf_list
        }, context_instance=RequestContext(request)
    )


def consulta_municipios_na_regiao(request):
    """ Return the render from page with query by municipalities in region.
    @param request context request from view
    @return HTML page with query by municipalities in region.
    """

    try:
        ## Id from UF requested
        uf_id = request.GET['uf_id']
    except MultiValueDictKeyError as e:
        logger.error(str(e))
        erro = "Preencha corretamente o formulário!"
        return render_to_response(
            "index.html", {
                'erro': erro
            }, context_instance=RequestContext(request)
        )

    try:
        valida_caracteres(uf_id)
    except ParametroInseguroClienteError as e:
        logger.error(str(e))
        erro = "Preencha corretamente o formulário!"
        return render_to_response(
            "index.html", {
                'erro': erro
            }, context_instance=RequestContext(request)
        )

    try:
        ## object DAO from municipalities
        municipalities_dao = MunicipioDAO()
        ## list of municipalities
        municipalities_list = municipalities_dao.lista_municipios(uf_id)
    except (MySQLdb.Error, ResultadoConsultaNuloError) as e:
        logger.error(str(e))
        erro = "Ocorreu um erro no sistema, tente novamente mais tarde!"
        return render_to_response(
            "index.html", {
                'erro': erro
            }, context_instance=RequestContext(request)
        )

    return render_to_response(
        "municipio.html", {
            'municipio_list': municipalities_list
        }, context_instance=RequestContext(request)
    )


def consulta_ocorrencias_por_municipio(request):
    """ Return the render from page with query by occurrences in the region.
    @param request context request from view
    @return HTML page with query by occurrences in the region.
    """

    try:
        ## Municipalitie Id
        municipalities_id = int(request.GET['municipio_id'])
    except (ValueError, MultiValueDictKeyError) as e:
        logger.error(str(e))
        erro = "Preencha corretamente o formulário!"
        return render_to_response(
            "index.html", {
                'erro': erro
            }, context_instance=RequestContext(request)
        )

    try:
        ## Occurrences DAO
        occurrences_dao = OcorrenciaBasicaDAO()
        ## List of occurrences
        occurrences_list = occurrences_dao.lista_ocorrencias_por_regiao(
            municipalities_id,
            1000
        )
    except (MySQLdb.Error, ResultadoConsultaNuloError) as e:
        logger.error(str(e))
        erro = "Ocorreu um erro no sistema, tente novamente mais tarde!"
        return render_to_response(
            "index.html", {
                'erro': erro
            }, context_instance=RequestContext(request)
        )

    if (len(occurrences_list) == 0):
        erro = "A consulta não retornou resultados!"
        return render_to_response(
            "index.html", {
                'erro': erro
            }, context_instance=RequestContext(request)
        )

    municipalities = occurrences_list[0].tmudenominacao
    uf = occurrences_list[0].tmuuf

    return render_to_response(
        "resultado.html", {
            'ocorrencia_list': occurrences_list,
            'tipo_consulta': 'regiao',
            'municipio': municipalities,
            'uf': uf
        }, context_instance=RequestContext(request)
    )
