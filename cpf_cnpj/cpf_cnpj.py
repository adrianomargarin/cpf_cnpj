# -*- coding:utf-8 -*-

class Cnpj(object):

    def __init__(self, cnpj):
        """
        Class to interact with cnpj brazilian numbers
        """
        self.cnpj = cnpj

    def calculating_digit(self, result):
        result = result % 11
        if result < 2:
            digit = 0
        else:
            digit = 11 - result
        return str(digit)

    def calculating_first_digit(self):
        one_validation_list = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4 , 3, 2]
        result = 0
        pos = 0
        for number in self.cnpj:
            try:
                one_validation_list[pos]
            except IndexError:
                break
            result += int(number) * int(one_validation_list[pos])
            pos += 1
        return self.calculating_digit(result)

    def calculating_second_digit(self):
        two_validation_list = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        result = 0
        pos = 0
        for number in self.cnpj:
            try:
                two_validation_list[pos]
            except IndexError:
                break
            result += int(number) * int(two_validation_list[pos])
            pos += 1
        return self.calculating_digit(result)

    def validate(self):
        """
        Method to validate brazilian cnpjs
        """
        self.cnpj = self.cleaning()

        if len(self.cnpj) != 14:
            return False

        checkers = self.cnpj[-2:]

        digit_one = self.calculating_first_digit()
        digit_two = self.calculating_second_digit()

        return bool(checkers == digit_one + digit_two)

    def cleaning(self):
        return self.cnpj.replace('-', '').replace('.', '').replace('/', '')

    def format(self):
        """
        Method to format cnpj numbers.
        """
        return '%s.%s.%s/%s-%s' % (self.cnpj[0:2], self.cnpj[2:5],
            self.cnpj[5:8], self.cnpj[8:12], self.cnpj[12:14])

class Cpf(object):

    def __init__(self, cpf):
        self.cpf = cpf

    def validate_size(self):
        cpf = self.cleaning()
        if len(cpf) > 11 or len(cpf) < 11:
            return False
        return True

    def validate(self):
        if self.validate_size():
            digit_1 = 0
            digit_2 = 0
            i = 0
            cpf = self.cleaning()
            while i < 10:
                digit_1 = ((digit_1 + (int(cpf[i]) * (11-i-1))) % 11
                    if i < 9 else digit_1)
                digit_2 = (digit_2 + (int(cpf[i]) * (11-i))) % 11
                i += 1
            return ((int(cpf[9]) == (11 - digit_1 if digit_1 > 1 else 0)) and
                    (int(cpf[10]) == (11 - digit_2 if digit_2 > 1 else 0)))
        return False

    def cleaning(self):
        return self.cpf.replace('.', '').replace('-', '')

    def format(self):
        return '%s.%s.%s-%s' % (
            self.cpf[0:3], self.cpf[3:6], self.cpf[6:9], self.cpf[9:11])