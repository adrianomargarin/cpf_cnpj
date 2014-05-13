# -*- coding:utf-8 -*-

import os
from setuptools import setup, find_packages

REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

setup(
    install_requires=REQUIREMENTS,
    name = "cpf_cnpj",
    version = '0.1.3',
    description = "Validador de CPF e CNPJ para Python",
    license = "MIT",
    author = "Adriano Margarin",
    author_email = "adriano.margarin@gmail.com",
    url = "https://github.com/amargarin/cpf_cnpj",
    packages = find_packages(exclude = ['tests']),
    keywords = "python cpf cnpj validador",
    zip_safe = True
)
