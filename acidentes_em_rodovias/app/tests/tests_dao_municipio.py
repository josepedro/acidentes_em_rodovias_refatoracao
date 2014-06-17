# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#
from app.tests.tests_basic import DAO_Tests
from app.models.dao.municipio_dao import MunicipioDAO


class TestMunicipio(DAO_Tests):

    """docstring for TestMunicipio
    Class that tests the methods municipio_dao
    """

    def test_existing_municipio_dao_instance(self):
        """
        Tests if the returned county is not NULL
        """

        self.municipio = MunicipioDAO()
        self.assertIsNotNone(self.municipio)

    def test_list_municipio(self):
        """
        Tests if the list of counties does not return null, in general and in
        a determined limit.
        """

        self.municipio = MunicipioDAO()
        for i in self.municipio.lista_municipios("DF"):
            self.assertIsNotNone(i)
        for i in self.municipio.lista_municipios("DF", limite=3):
            self.assertIsNotNone(str(i))
            self.assertIsNotNone(i)
