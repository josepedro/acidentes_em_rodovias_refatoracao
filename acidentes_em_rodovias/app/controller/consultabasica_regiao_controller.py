#!/usr/bin/env python
# coding: utf-8

"""Acidentes em Rodovias

 Universidade de Brasilia - FGA
 Técnicas de Programação, 1/2014

Parser responsable to return to HTML inquiry about region.
"""
import MySQLdb
import logging

from django.utils.datastructures import MultiValueDictKeyError
from django.template import RequestContext
from django.shortcuts import render_to_response

from app.dao.uf_dao import UfDAO
from app.dao.municipio_dao import MunicipioDAO
from app.dao.ocorrencia_basica_dao import OcorrenciaBasicaDAO

from app.exception.validation_exceptions import ParametroInseguroClienteError
from app.exception.internal_exceptions import ResultadoConsultaNuloError

from app.util.validacao_util import valida_caracteres

# Logging config
logging.basicConfig()
# logger object
logger = logging.getLogger(__name__)

_MAX_ITEMS = 1000


def consulta_por_regiao(request):
    """ Return the render from page with query by region.
    @param request context request from view
    @return HTML page with query by region.
    """

    try:
        # object DAO from UF
        uf_dao = UfDAO()
        # list of UFs
        uf_list = uf_dao.lista_ufs()
    except (MySQLdb.Error, ResultadoConsultaNuloError):
        # logger.error(str(e))
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
        # Id from UF requested
        uf_id = request.GET['uf_id']
    except MultiValueDictKeyError:
        # logger.error(str(e))
        erro = "Preencha corretamente o formulário!"
        return render_to_response(
            "index.html", {
                'erro': erro
            }, context_instance=RequestContext(request)
        )

    try:
        valida_caracteres(uf_id)
    except ParametroInseguroClienteError:
        # logger.error(str(e))
        erro = "Preencha corretamente o formulário!"
        return render_to_response(
            "index.html", {
                'erro': erro
            }, context_instance=RequestContext(request)
        )

    try:
        # object DAO from municipalities
        municipalities_dao = MunicipioDAO()
        # list of municipalities
        municipalities_list = municipalities_dao.lista_municipios(uf_id)
    except (MySQLdb.Error, ResultadoConsultaNuloError):
        # logger.error(str(e))
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
        # Municipalitie Id
        municipalities_id = int(request.GET['municipio_id'])
    except (ValueError, MultiValueDictKeyError):
        # logger.error(str(e))
        erro = "Preencha corretamente o formulário!"
        return render_to_response(
            "index.html", {
                'erro': erro
            }, context_instance=RequestContext(request)
        )

    try:
        # Occurrences DAO
        occurrences_dao = OcorrenciaBasicaDAO()
        # List of occurrences
        occurrences_list = occurrences_dao.lista_ocorrencias_por_regiao(
            municipalities_id,
            _MAX_ITEMS
        )
    except (MySQLdb.Error, ResultadoConsultaNuloError):
        # logger.error(str(e))
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
