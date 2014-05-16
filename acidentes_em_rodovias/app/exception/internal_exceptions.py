#!/usr/bin/env python
# coding: utf-8

"""Acidentes em Rodovias - internal exceptions

 Universidade de Brasilia - FGA
 Técnicas de Programação, 1/2014

This module contains control classes of exception for internal validations
"""

from app.exception.validation_exceptions import DataInvalidaError


class ResultadoConsultaNuloError(DataInvalidaError):

    """ Exception to occurs when a inquiry returns null """
