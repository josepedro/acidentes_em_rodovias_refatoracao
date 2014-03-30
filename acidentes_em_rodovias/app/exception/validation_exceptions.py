#!/usr/bin/env python
# coding: utf-8

"""Acidentes em Rodovias - validation exceptions

 Universidade de Brasilia - FGA
 Técnicas de Programação, 1/2014

This module contains control classes of exception for validation
"""

from exceptions import Exception


class DataInvalidaError(Exception):

    """docstring for InvalidDateError"""

    def __init__(self, message):
        """ Initialize module """
        Exception.__init__(self)
        self.message = message

    def __str__(self):
        """ How module shold be printed """
        return self.message


class ParametroInseguroClienteError(Exception):

    """docstring for ParametroInseguroClienteError"""

    def __init__(self, message):
        """ Initialize module """
        Exception.__init__(self)
        self.message = message

    def __str__(self):
        """ How module shold be printed """
        return self.message
