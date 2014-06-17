#!/usr/bin/env python
# coding: utf-8

"""Acidentes em Rodovias

 Universidade de Brasilia - FGA
 Técnicas de Programação, 1/2014

Parser responsable to return to HTML the index page.
"""
from django.template import RequestContext
from django.shortcuts import render_to_response


def index(request):
    """ Return the render from the index page. """

    return render_to_response(
        "index.html",
        context_instance=RequestContext(request)
    )
