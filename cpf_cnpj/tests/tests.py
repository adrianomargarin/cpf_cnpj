# -*- coding:utf-8 -*-

from unittest import TestCase

from cpf_cnpj import Cpf, Cnpj

class CnpjTest(TestCase):

    def setUp(self):
        self.cnpj_valid_with_formatting = Cnpj('65.025.861/0001-70')
        self.cnpj_valid_without_formatting = Cnpj('65025861000170')
        self.cnpj_invalid_with_formatting = Cnpj('61.882.613/0001-95')
        self.cnpj_invalid_without_formatting = Cnpj('61882613000195')
        self.cnpj_invalid_amount_with_formatting = Cnpj('61.882.613/0001-9')
        self.cnpj_invalid_amount_without_formatting = Cnpj('6188261300019')

    def test_calculating_first_digit(self):
        self.assertEqual(
            self.cnpj_valid_without_formatting.calculating_first_digit(), '7')

    def test_calculating_second_digit(self):
        self.assertEqual(
            self.cnpj_valid_without_formatting.calculating_second_digit(), '0')

    def test_cnpj_valid_without_formatting(self):
        self.assertTrue(self.cnpj_valid_without_formatting.validate())

    def test_cnpj_valid_with_formatting(self):
        self.assertTrue(self.cnpj_valid_with_formatting.validate())

    def test_cnpj_invalid_without_formatting(self):
        self.assertFalse(self.cnpj_invalid_without_formatting.validate())

    def test_cnpj_invalid_with_formatting(self):
        self.assertFalse(self.cnpj_invalid_with_formatting.validate())

    def test_cnpj_invalid_amount_without_formatting(self):
        self.assertFalse(self.cnpj_invalid_amount_without_formatting.validate())

    def test_cnpj_invalid_amount_with_formatting(self):
        self.assertFalse(self.cnpj_invalid_amount_with_formatting.validate())

    def test_cnpj_valid_format(self):
        self.assertEqual(self.cnpj_valid_without_formatting.format(),
            '65.025.861/0001-70')

    def test_cnpj_invalid_format(self):
        self.assertNotEqual(self.cnpj_valid_with_formatting.format(),
            '65025861000170')

class CpfTest(TestCase):

    def setUp(self):
        self.cpf_with_formatting = Cpf('010.787.400-89')
        self.cpf_without_formatting = Cpf('01078740089')

    def test_cpf_with_formatting_validate_suze_return_true(self):
        self.assertTrue(self.cpf_with_formatting.validate_size())

    def test_cpf_without_formatting_validate_suze_return_true(self):
        self.assertTrue(self.cpf_without_formatting.validate_size())

    def test_cpf_validate_size_return_false(self):
        cpf = Cpf('1234567891')
        self.assertFalse(cpf.validate_size())

    def test_cpf_format_return_true(self):
        self.assertEqual(self.cpf_without_formatting.format(), '010.787.400-89')

    def test_cpf_format_return_false(self):
        self.assertNotEqual(self.cpf_without_formatting.format(), '01078740089')

    def test_cpf_cleaning_return_true(self):
        self.assertEqual(self.cpf_with_formatting.cleaning(), '01078740089')

    def test_cpf_cleaning_return_false(self):
        self.assertNotEqual(self.cpf_with_formatting.cleaning(),
            '010787400-89')

    def test_cpf_with_formatting_validate_return_true(self):
        self.assertTrue(self.cpf_with_formatting.validate())

    def test_cpf_with_formatting_validate_return_false(self):
        cpf = Cpf('010.787.400-8')
        self.assertFalse(cpf.validate())

    def test_cpf_without_formatting_validate_return_false(self):
        cpf = Cpf('0107874008')
        self.assertFalse(cpf.validate())

    def test_cpf_without_formatting_validate_return_true(self):
        self.assertTrue(self.cpf_without_formatting.validate())