# Traquitanas

[![Publish Python distributions to PyPI](https://github.com/traquitanas/traquitanas/actions/workflows/publish-to-pypi.yml/badge.svg)](https://github.com/traquitanas/traquitanas/actions/workflows/publish-to-pypi.yml)
<br>
[![Publish Python distributions to TestPyPI](https://github.com/traquitanas/traquitanas/actions/workflows/publish-to-test-pypi.yml/badge.svg)](https://github.com/traquitanas/traquitanas/actions/workflows/publish-to-test-pypi.yml)

<br>

Traquitanas, badulaques, secos e molhados.<br>
Por aqui tem de tudo. Tudo junto e misturado!

Todas as coisas que uso no dia a dia... em um só pacote.<br>
Quem sabe um dia encaixoto tudo, separando os temas em pacotes distintos...

O pacote também tem a função de aprender a empacotar as coisas.

<br>

-----

### Install

```bash
pip3 install traquitanas --upgrade
```

<br>

----

### Conversão Coordenadas

```python
from traquitanas import geo

geo.converts.dms2dd('23°06’12,48”S')
geo.converts.dms2dd_infoaguas('22 13 52')
geo.converts.df2geojson(df, lat='latitude', long='longitude', remove_coords_properties=True)
```

<br>

----

### *Utils*

```python
from traquitanas import utils

utils.predict_encoding()
```

<br>

----

### Net

```python
from traquitanas import net

driver = net.scraping.create_driver(download_path)
```

<br>

----

## Google Colab

Para testes rápidos sobre o funcionamento do pacote, elaborei um [Google Colab](https://colab.research.google.com/drive/1WfiEeO4jeeiLPiCknGWfvHI-O3b5NbjE?usp=sharing).
