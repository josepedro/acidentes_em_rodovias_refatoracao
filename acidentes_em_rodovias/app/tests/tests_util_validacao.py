# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#
from app.tests.tests_basic import Validate_Tests

from app.exception.validation_exceptions import DataInvalidaError
from app.exception.validation_exceptions import ParametroInseguroClienteError

from app.util import validacao_util


class Test_Valida(Validate_Tests):

    """Test the validate of inputs"""

    def test_valida_data(self):
        self.assertFalse(validacao_util.valida_data(
            "10/10/2013"
        ))
        with self.assertRaises(DataInvalidaError):
            self.assertFalse(validacao_util.valida_data(
                "20 de março de 2013"
            ))
        with self.assertRaises(DataInvalidaError):
            self.assertFalse(validacao_util.valida_data(
                ""
            ))

    def test_valida_caracteres(self):
        with self.assertRaises(ParametroInseguroClienteError):
            self.assertIsNone(validacao_util.valida_caracteres(None))
        with self.assertRaises(ParametroInseguroClienteError):
            self.assertFalse(validacao_util.valida_caracteres("./$%^&"))
