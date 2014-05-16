# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#

from app.tests.tests_basic import Index_Tests
from django.template import RequestContext, TemplateDoesNotExist

from app.exception.validation_exceptions import *

from app.controller import index_controller as ctrl

from _mysql_exceptions import *


class TestControllerIndex(Index_Tests):

    """docstring for TestControllerIndex"""

    def test_render_to_response(self):
        self.assertIsNotNone(ctrl.render_to_response(
            "index.html", context_instance=RequestContext(None)))
        with self.assertRaises(TemplateDoesNotExist):
            ctrl.render_to_response(
                "nao_existo",
                context_instance=RequestContext(None)
            )

    def test_index(self):
        self.assertIsNotNone(ctrl.index(None))
