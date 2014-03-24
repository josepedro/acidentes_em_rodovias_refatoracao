# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#

import MySQLdb
import logging
import sys
import os
import inspect

# Add upper directories
current_dir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())
))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from django.utils.datastructures import MultiValueDictKeyError
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response

from exception.validation_exceptions import *
from exception.internal_exceptions import *

from models.dao.br_accidents_dao import *

from datetime import datetime

# Config logging messages
logging.basicConfig()
logger = logging.getLogger(__name__)


def accidents_br(request):
    try:
        date = datetime.now()
        br_dao = BRAccidentsDAO()
        general_accidents = br_dao.general_accidents()
        accidents_year = br_dao.general_accidents_year()

    except (MySQLdb.Error, ResultadoConsultaNuloError), e:
        logger.error(str(e))
        error = "Ocorreu um erro no sistema, tente novamente mais tarde!"
        return render_to_response("index.html", {
            'error': error
        }, context_instance=RequestContext(request))

    return render_to_response("br_acidentes.html", {
        'year': range(2007, date.year + 1),
        'general_accidents': general_accidents,
        'accidents_year': accidents_year
    }, context_instance=RequestContext(request))
