#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_sqlite3_zlib_adapter
----------------------------------

Tests for `sqlite3_zlib_adapter` module.
"""

import pytest


from sqlite3_zlib_adapter import sqlite3_zlib_adapter


@pytest.fixture
def response():
    """Sample pytest fixture.
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument.
    """
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
