#!/usr/bin/env python
# coding: utf-8

"""Acidentes em Rodovias

 Universidade de Brasilia - FGA
 Técnicas de Programação, 1/2014

Calc some statistics methods.
"""

import os


def gaussian_distribution(eixo_vertical, eixo_horizontal):
    """ Calculate the gaussian_distribution """
    value_standard = 0.5
    prev_path = os.path.dirname(os.path.abspath(__file__))
    arquivo_csv = open(
        prev_path +
        "/../resources/tabela-normal-reduzida.csv",
        "rb")
    tabela = []
    for linha in arquivo_csv:
        line = [float(i.strip()) for i in linha.split(';')]
        tabela.append(line)
    try:
        probabilities = tabela[eixo_vertical][eixo_horizontal]
    except TypeError:
        probabilities = value_standard

    return probabilities


def distribuicao_normal(x_point, media, desvio):
    """ Calc Normal distribution (Gaussian) """
    try:
        normalization = 100
        adjust_vertical = 10
        value_standard = 0.5
        z_point = (x_point - media) / float(abs(desvio))
        z_point = abs(int(z_point * normalization) / normalization)
        eixo_vertical = int(z_point * adjust_vertical)
        eixo_horizontal = int(
            z_point * normalization) - adjust_vertical * eixo_vertical
        try:
            probabilities = gaussian_distribution(
                eixo_vertical, eixo_horizontal)
        except IndexError:
            probabilities = value_standard
    except TypeError:
        probabilities = value_standard
    return probabilities


def calculate_total_mean(lista):
    """ Calculate the mean total """
    total_mean = 0
    array_initial = 0
    for i in range(array_initial, len(lista)):
        total_mean = total_mean + lista[i]
    total_mean = total_mean / len(lista)
    return total_mean


def desvio_padrao(lista):
    """ Calc standard deviation """
    elevation_to_2 = 2
    square_root = 0.5
    array_initial = 0
    devition_for_none = -1
    try:
        total_mean = calculate_total_mean(lista)
        for i in range(array_initial, len(lista)):
            desvio = (i - total_mean) ** elevation_to_2
        deviation = (desvio / len(lista)) ** (square_root)
    except TypeError:
        deviation = devition_for_none
    return deviation


def media_sexo(homens, mulheres):
    """ Calc mean about men and women """
    porcent_division = 100
    paramter_none = -1
    try:
        total = int(homens[0].quantidade) + int(mulheres[0].quantidade)
        for homem in homens:
            homem.quantidade = float(
                homem.quantidade) / float(total) * porcent_division
        for mulher in mulheres:
            mulher.quantidade = float(
                mulher.quantidade) / float(total) * porcent_division
        return homens[0], mulheres[0]
    except TypeError:
        return paramter_none
