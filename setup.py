from setuptools import setup, find_namespace_packages, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

requirements = [
    'pycep_correios>=5.0.0',
    'requests>=2.10.1',
]

setup(
    name='traquitanas',  # Nome (não precisa ser o nome do repositório, nem de qualquer pasta...)
    version='1.0.7',
    author='Michel Metran',
    author_email='michelmetran@gmail.com',
    description='Small Defs...',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/open-dsa/gerador_endereco',
    package_dir = {'': 'src'}, # Our packages live under src but src is not a package itself    
    #packages=find_packages(),
    packages=find_packages('src.*', exclude=['*tests*']),
    #include_package_data=False, # https://stackoverflow.com/questions/61274967/why-cant-i-exclude-tests-directory-from-my-python-wheel-using-exclude
    py_modules = ['traquitanas'],
    install_requires=requirements,
    keywords='python, endereço aleatório, address',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: Portuguese',
        'Intended Audience :: Developers',
    ],
)

# package_dir={
#     'scripts': 'random_address',
# },
# include_package_data=True,
# package_data={
#     'myapp': ['data/*.txt'],
# },
# py_modules=['gerador_endereco'],