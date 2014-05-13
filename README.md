CPF e CNPJ
==========

Validador de CPF e CNPJ.

**Install**


``` python

  pip install cpf_cnpj
```

**Usage**

``` python

  from cpf_cnpj import Cpf, Cnpj
  
  cpf = Cpf('85725262502')

  cpf.format()
  '857.252.625-02'
  
  cpf.cleaning()
  '85725262502'
  
  cpf.validate()
  True
  
  cnpj = Cnpj('97373439000100')

  cnpj.format()
  '97.373.439/0001-00'
  
  cnpj.cleaning()
  '97373439000100'
  
  cnpj.validate()
  True
```
