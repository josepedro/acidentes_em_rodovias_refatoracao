#!/usr/bin/env python
# coding: utf-8

"""Acidentes em Rodovias

 Universidade de Brasilia - FGA
 Técnicas de Programação, 1/2014

Parser responsable to return to HTML the index page.
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

# Adding upper directories to the Python Path
from app import *


def index(request):
    """ Return the render from the index page. """

    return render_to_response(
        "index.html",
        context_instance=RequestContext(request)
    )
