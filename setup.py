# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
        name = "cpf_cnpj",
        version = '0.1.0',
        description = "Validador de CPF e CNPJ para Python",
        license = "MIT",
        author = "Adriano Margarin",
        author_email = "adriano.margarin@gmail.com",
        url = "https://github.com/amargarin/cpf_cnpj",
        packages = find_packages(exclude = ['tests']),
        keywords = "python cpf cnpj validador",
        zip_safe = True
    )
