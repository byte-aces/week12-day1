#!/usr/bin/env python3

import random
import time

from flask import Blueprint, g, redirect, render_template, request, session, url_for


module = Blueprint('views', __name__, url_prefix="")


# FIXME Dashboard page
@module.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    # TODO Write graphical user interface
    return render_template('dashboard.html')


# FIXME Account page
@module.route('/account', methods=['GET', 'POST'])
def account():
    # TODO Write graphical user interface
    return render_template('account.html')


# Note: for local testing
if __name__ == '__main__':
    module.run(debug=True)
