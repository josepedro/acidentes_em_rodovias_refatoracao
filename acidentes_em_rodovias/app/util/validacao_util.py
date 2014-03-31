#!/usr/bin/env python
# coding: utf-8

"""Acidentes em Rodovias

@file validacao_util.py
 Universidade de Brasilia - FGA
 Técnicas de Programação, 1/2014

Calc some statistics methods.
"""

import sys
import os
import inspect
""" Variable to store the corrent path. """
_current_dir = os.path.dirname(
    os.path.abspath(inspect.getfile(inspect.currentframe())))

""" Variable to store the parent path. """
_parent_dir = os.path.dirname(_current_dir)
sys.path.append(_parent_dir)

from re import search
from exception.validation_exceptions import *
from exception.internal_exceptions import *


def valida_data(data):
    """
    Validate date. If a no valid data be received, an exception will
    be risen.
    @param data Date to be validate.
    """

    if (search('^[0-3]\rd/[01]\rd/\rd{4}$', data) is None
            or int(data[0:2]) >= 32
            or int(data[3:5]) >= 13):
        raise DataInvalidaError("Data invalida inserida: " + data)


def valida_caracteres(palavra):
    """
    Validate a sequence of characters. If a no valid character is found,
    an exception will be risen.
    @param palavra Word to be validate if all characters
    are valid.
    """

    if search('^[\rw\rs]+$', str(palavra) is None):
        raise ParametroInseguroClienteError(
            "Parametro invalido inserido: " +
            palavra)
    if palavra is None:
        raise ParametroInseguroClienteError(
            "Parametro invalido inserido: enviado NONE")
