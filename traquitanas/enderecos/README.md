# Gerador Endereço

<br>

Programa para gerar endereços _fakes_ aleatórios, definido apenas o município. Elaborado visando popular um bancos de dados para um projeto realizado em um município específico.

<br>

---

### Como Instalar?

<br>

```bash
pip3 install traquitanas --upgrade
```

<br>

---

### Como usar?

<br>

Inicialmente é necessário gerar um conjunto/lista de CEPs únicos e aleatórios, definindo apenas a unidade da federação e nome do município. Como resultado, são geradas duas listas:

1. A primeira lista contem CEPs;
2. A segunda lista contem bairros.

```python
import random
from traquitanas.enderecos import gerador_endereco

# Gera listas de CEPs e Bairros
list_ceps, list_bairros = gerador_endereco.get_list_ceps_bairros(estado='sp', municipio='piracicaba')

# Resultados
print(list_ceps[0:10])
print(list_bairros[0:10])
```

<br>

Uma vez com essa lista de CEPs aleatórios, é possível obter o logradouro completo por meio da função.

```python
# Escolher CEP aleatório
cep = random.choice(list_ceps)

# Cria um Endereço *fake* aleatório
dict_endereco = gerador_endereco.get_random_complete_address(cep)

# Results
print(dict_endereco)
```

<br>

O resultado será um dicionário com um endereço aleatório, por exemplo:

```json
{
  "bairro": "Nova Piracicaba",
  "cep": "13405-078",
  "cidade": "Piracicaba",
  "endereco_completo": "Praça Noêmia Godoy Leme, 121 - Nova Piracicaba - Piracicaba, SP - CEP: 13405-078",
  "logradouro": "Praça Noêmia Godoy Leme",
  "numero": "121",
  "uf": "SP"
}
```

<br>

Caso tenha interesse, há um [_Google Colab_](https://colab.research.google.com/drive/1WfiEeO4jeeiLPiCknGWfvHI-O3b5NbjE?usp=sharing) para testes.

<br>

---

### _TODO_

1. Ajustar o _output_ usando uma _OrderedDicts_;
