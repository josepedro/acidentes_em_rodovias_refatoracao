# -*- coding: utf-8 -*- 
import sys, os, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import MySQLdb
from django.utils.datastructures import MultiValueDictKeyError
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response
from exception.validation_exceptions import *
from exception.internal_exceptions import *
from models.dao.tipos_acidentes_dao import *
from datetime import datetime
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)

def tipos_acidentes(request):
	try:
		tipos_acidentes_dao = TiposAcidentesDAO()
		tipos_acidentes_list = tipos_acidentes_dao.tipos_acidentes()
		tipos_acidentes_ano_list = tipos_acidentes_dao.tipos_acidentes_ano()
		probabilidade_tipos_acidentes_list = tipos_acidentes_dao.probabilidade_tipos_acidentes()
		media_desvio_tipos_acidentes_list = tipos_acidentes_dao.media_desvio_tipos_acidentes()
	except (MySQLdb.Error, ResultadoConsultaNuloError), e:
		logger.error(str(e))
		erro = "Ocorreu um erro no sistema, tente novamente mais tarde!"
		return render_to_response("index.html", {'erro' : erro}, context_instance=RequestContext(request))

	return render_to_response("tipos_acidentes.html",{
		'tipos_acidentes_list' : tipos_acidentes_list, 
		'tipos_acidentes_ano_list' : tipos_acidentes_ano_list,
		'anos' : tipos_acidentes_ano_list[0].ano_list,
		'probabilidade_tipos_acidentes_list' : probabilidade_tipos_acidentes_list,
		'tipos' : [i.tipo for i in probabilidade_tipos_acidentes_list], 
		'media_desvio_tipos_acidentes_list' : media_desvio_tipos_acidentes_list,
		}, context_instance=RequestContext(request))	
