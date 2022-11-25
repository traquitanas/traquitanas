"""
ssss
"""

import errno
import os
import stat

import chardet


def predict_encoding(file_path, n_lines=30):
    """
    Predict Encoding determines the encoding of a given file,
    so that when reading the file (via 'Pandas', for example)
    characters, accents and symbols are spelled correctly.

    # Examples to Use
    file_encoding = predict_encoding('data.csv')
    print(file_encoding)
    df = pd.read_csv('data.csv', encoding=file_encoding)

    :param file_path: Name and path to file
    :param n_lines: Number of lines to read to set encoding. Parameter Optional.
    Default: 30 lines.
    :return: Encoding.
    """

    # Open the file as binary data
    with open(file_path, 'rb') as f:
        # Join binary lines for specified number of lines
        raw_data = b''.join([f.readline() for line in range(n_lines)])
    enc = chardet.detect(raw_data)['encoding']
    return enc


def handle_remove_readonly(func, path, exc):
    """
    dddd

    Example:
    shutil.rmtree(
        input_path,
        ignore_errors=False,
        onerror=handle_remove_readonly
    )

    References:
    https://stackoverflow.com/questions/1213706/what-user-do-python-scripts-run-as-in-windows

    :param func: _description_
    :type func: _type_
    :param path: _description_
    :type path: _type_
    :param exc: _description_
    :type exc: _type_
    """

    excvalue = exc[1]
    if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
        os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 0777
        func(path)
    else:
        raise


if __name__ == '__main__':
    pass
