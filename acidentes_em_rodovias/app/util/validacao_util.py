#!/usr/bin/env python
# coding: utf-8

"""Acidentes em Rodovias

@file validacao_util.py
 Universidade de Brasilia - FGA
 Técnicas de Programação, 1/2014

Calc some statistics methods.
"""
from re import search
from app.exception.validation_exceptions import DataInvalidaError
from app.exception.validation_exceptions import ParametroInseguroClienteError


def valida_data(data):
    """
    Validate date. If a no valid data be received, an exception will
    be risen.
    @param data Date to be validate.
    """

    _max_day = 32
    _max_month = 13

    if data == "":
        raise DataInvalidaError("Data invalida inserida: " + data)

    if (search('^[0-3]\d/[01]\d/\d{4}$', data) is None
            or int(data[0:2]) >= _max_day
            or int(data[3:5]) >= _max_month):
        raise DataInvalidaError("Data invalida inserida: " + data)


def valida_caracteres(palavra):
    """
    Validate a sequence of characters. If a no valid character is found,
    an exception will be risen.
    @param palavra Word to be validate if all characters
    are valid.
    """

    if search('^[\w\s]+$', str(palavra)) is None:
        raise ParametroInseguroClienteError(
            "Parametro invalido inserido: " +
            palavra)
    if palavra is None:
        raise ParametroInseguroClienteError(
            "Parametro invalido inserido: enviado NONE")
