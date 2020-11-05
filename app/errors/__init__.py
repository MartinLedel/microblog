"""
Create errors Blurprint
"""
from flask import Blueprint

bp = Blueprint('errors', __name__)

from app.errors import handlers  # pylint: disable=wrong-import-position, cyclic-import
