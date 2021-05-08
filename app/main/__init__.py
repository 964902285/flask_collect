"""
@File    : __init__.py
@Time    : 2021/4/23 16:14
@Author  : shroud.xu
@Description: 一个 ctrl c + v 工程师
@Email   : shroud.xu@cygia.com
@Software: PyCharm
"""
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
