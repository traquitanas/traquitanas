"""
Convert dataframe to sql script

Michel Metran
março.2023
"""


from datetime import datetime

from sqlalchemy import create_engine


def convert_dataframe_to_sql(dataframe, output_file, dataset_name):
    """
    Convert a dataframe into a .sql file, with instructions for
    creating a table and inserting data

    :param dataframe: Dataframe to be converted
    :type dataframe: dataframe
    :param output_file: _description_Path to output file
    :type output_file: Posix Path
    :param dataset_name: Database table name
    :type dataset_name: string
    """
    # Create Engine with SQL Alchemy (used by pandas)
    engine = create_engine('sqlite://', echo=False)

    # Sendo data to temporary SQLite3
    dataframe.to_sql(
        name=dataset_name, index=True, con=engine, if_exists='replace'
    )

    # Para cada
    with open(output_file, 'w', encoding='utf-8') as f:
        #
        data_agora = datetime.today().strftime('%Y.%m.%d %H:%M:%S')

        f.write(
            '/****** Query para criação e inserção de registros no DB ******/\n'
        )
        f.write('/*\n')
        f.write(f'São {len(dataframe)} registros\n')
        f.write(f'Obtidos na tabela "{dataset_name}"\n')
        f.write('\n')
        f.write(f'Query feita por Michel Metran em {data_agora},\n')
        f.write('*/\n')
        f.write('\r\n')

        with engine.connect() as conn:
            for line in conn.connection.iterdump():
                f.write(f'{line}\n')
                print(line)

        # Close Connection
        conn.close()
        return 0


if __name__ == '__main__':
    import seaborn as sns
    from paths import output_path_sql

    # Create Dataframe
    dataset = 'iris'
    df = sns.load_dataset(dataset)

    # Convert do SQL File
    convert_dataframe_to_sql(
        df,
        output_file=output_path_sql / f'sql - {dataset}.sql',
        dataset_name=dataset,
    )
