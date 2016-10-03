# -*- coding: utf-8 -*-
from flask import Blueprint

main = Blueprint('maun', __name__)

from . import views, errors

