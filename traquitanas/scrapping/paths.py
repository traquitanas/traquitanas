"""
Pastas Projeto
"""


from pathlib import Path

project_path = Path(__file__).parents[2]

# Scrapy
scrapy_path = project_path / 'scrapy'
scrapy_path.mkdir(exist_ok=True)

driver_path = scrapy_path / 'driver'
driver_path.mkdir(exist_ok=True)

logs_path = scrapy_path / 'logs'
logs_path.mkdir(exist_ok=True)

adds_path = scrapy_path / 'adds'
adds_path.mkdir(exist_ok=True)


if __name__ == '__main__':
    print(project_path)
