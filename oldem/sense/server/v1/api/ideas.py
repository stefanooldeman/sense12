# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class Ideas(Resource):

    def post(self):
        print(g.json)
        return {'created_at': 'something', 'link': 'something', 'uuid': 'something'}, 201, None
