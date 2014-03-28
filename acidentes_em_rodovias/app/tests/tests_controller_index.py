# -*- coding: utf-8 -*-
#
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#

import sys
import os
import inspect

from django.test import SimpleTestCase
from django.template import RequestContext, TemplateDoesNotExist

from exception.validation_exceptions import *

from controller import index_controller as ctrl

from _mysql_exceptions import *

# Adding upper directories to the Python Path
current_path = os.path.dirname(os.path.abspath('..'))
sys.path.append(current_path)
current_path = os.path.dirname(os.path.abspath('.'))
sys.path.append(current_path)


class TestControllerIndex(SimpleTestCase):

    """docstring for TestControllerIndex"""

    def setUp(self):
        func = str(self.id).split('=')[-1][:-2]
        func = func.split('test_')[-1]
        func = func.replace('_', ' ')
        out = '\rTeste de ' + func + ' '
        out = out.ljust(65, '-')
        sys.stderr.write(out)
        self.shortDescription()

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
