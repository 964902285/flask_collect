"""
@File    : errors.py
@Time    : 2021/4/23 16:14
@Author  : shroud.xu
@Description: 一个 ctrl c + v 工程师
@Email   : shroud.xu@cygia.com
@Software: PyCharm
"""
from flask import render_template
from . import main


@main.app_errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
