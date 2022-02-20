# Traquitanas

[![Publish Python distributions to PyPI](https://github.com/traquitanas/traquitanas/actions/workflows/publish-to-pypi.yml/badge.svg)](https://github.com/traquitanas/traquitanas/actions/workflows/publish-to-pypi.yml)
<br>
[![Publish Python distributions to TestPyPI](https://github.com/traquitanas/traquitanas/actions/workflows/publish-to-test-pypi.yml/badge.svg)](https://github.com/traquitanas/traquitanas/actions/workflows/publish-to-test-pypi.yml)

<br>

Traquitanas, badulaques, secos e molhados.<br>
Por aqui tem de tudo. Tudo junto e misturado!

Todas as coisas que uso no dia a dia... em um só pacote.<br>
Quem sabe um dia encaixoto tudo, separando os temas em pacotes distintos...

<br>

-----

### Install

```bash
pip3 install traquitanas --upgrade
```

<br>

----

### Geoprocessamento

#### Conversão

Funções para converter coordenadas e formatos.

```python
from traquitanas import geo

geo.converts.dms2dd('23°06’12,48”S')
geo.converts.dms2dd_infoaguas('22 13 52')
geo.converts.df2geojson(df, lat='latitude', long='longitude', remove_coords_properties=True)
```

<br>

#### *Layers*




----

### Net





