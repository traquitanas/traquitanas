import random
import requests


def dms2dd(coord):
    """
    Convert geographic coordinates in
    format degrees, minutes and seconds (23°06’12,48”S)
    in decimal degrees

    :param coord: string 23°06’12,48”S
    :return: float -23.10346666666667
    """
    # Splitar coordenada
    graus = float(coord.split('°')[0])
    minutos = float((coord.split('°')[1]).split('’')[0])
    segundos = float((((coord.split('°')[1]).split('’')[1]).split('”')[0]).replace(',', '.'))
    direction = (((coord.split('°')[1]).split('’')[1]).split('”')[1])

    # Calcular
    coord_dm = graus + (minutos / 60) + (segundos / 3600)

    # Converter parâmetro textual
    if direction in ('S', 's', 'O', 'o'):
        return coord_dm * -1
    else:
        return coord_dm


def df2geojson(df, lat='latitude', long='longitude', remove_coords_properties=True):
    """
    Convert um dataframe, com colunas de latitude e longitude, em um objeto geojson
    https://notebook.community/gnestor/jupyter-renderers/notebooks/nteract/pandas-to-geojson
    :param df:
    :param lat: Nome da coluna no dataframe que tem os dados de latitude
    :param long: Nome da coluna no dataframe que tem os dados de longitude
    :param remove_coords_properties:
    :return:
    """

    # Create a new python dict to contain our geojson data, using geojson format
    geojson = {'type': 'FeatureCollection', 'features': []}

    # Loop through each row in the dataframe and convert each row to geojson format
    for _, row in df.iterrows():
        # Create a feature template to fill in
        feature = {
            'type': 'Feature',
            'properties': {},
            'geometry': {
                'type': 'Point',
                'coordinates': [],
            }
        }

        # Fill in the coordinates
        feature['geometry']['coordinates'] = [row[long], row[lat]]

        # for each column, get the value and add it as a new feature property
        properties = list(df.columns)
        if remove_coords_properties:
            properties.remove(lat)
            properties.remove(long)

        for prop in properties:
            feature['properties'][prop] = row[prop]

        # Add this feature (aka, converted dataframe row) to the list of features inside our dict
        geojson['features'].append(feature)

    return geojson


if __name__ == '__main__':
    print(dms2dd('23°06’12,48”S'))
