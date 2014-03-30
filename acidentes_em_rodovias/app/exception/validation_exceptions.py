#!/usr/bin/env python
# coding: utf-8

"""Acidentes em Rodovias - validation exceptions

 Universidade de Brasilia - FGA
 Técnicas de Programação, 1/2014

This module contains control classes of exception for validation
"""

from exceptions import Exception


class DataInvalidaError(Exception):

    """ Exception to occurs when a date is not well formatted """

    def __init__(self, message):
        """ Initialize module """
        Exception.__init__(self)
        self.message = message

    def __str__(self):
        """ How module shold be printed """
        return self.message


class ParametroInseguroClienteError(Exception):

    """ Exception to occurs when an odd character is inserted by
    user or by Data Bank """

    def __init__(self, message):
        """ Initialize module """
        Exception.__init__(self)
        self.message = message

    def __str__(self):
        """ How module shold be printed """
        return self.message
