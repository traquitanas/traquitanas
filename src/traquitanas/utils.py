import chardet


def predict_encoding(file_path, n_lines=30):
    """
    Predict Encoding determines the encoding of a given file, so that when reading the file (via 'Pandas', for example)
    characters, accents and symbols are spelled correctly.

    # Examples to Use
    file_encoding = predict_encoding('data.csv')
    print(file_encoding)
    df = pd.read_csv('data.csv', encoding=file_encoding)

    :param file_path: Name and path to file
    :param n_lines: Number of lines to read to set encoding. Parameter Optional. Default: 30 lines.
    :return: Encoding.

    """

    # Open the file as binary data
    with open(file_path, 'rb') as f:
        # Join binary lines for specified number of lines
        raw_data = b''.join([f.readline() for line in range(n_lines)])
    return chardet.detect(raw_data)['encoding']
