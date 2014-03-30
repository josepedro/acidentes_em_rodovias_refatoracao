#!/usr/bin/env python
# coding: utf-8

"""Acidentes em Rodovias - internal exceptions

 Universidade de Brasilia - FGA
 Técnicas de Programação, 1/2014

This module contains control classes of exception for internal validations
"""

from exceptions import Exception


class ResultadoConsultaNuloError(Exception):

    """ Exception to occurs when a inquiry returns null """

    def __init__(self, message):
        """ Initialize module """
        Exception.__init__(self)
        self.message = message

    def __str__(self):
        """ How module shold be printed """
        return self.message
