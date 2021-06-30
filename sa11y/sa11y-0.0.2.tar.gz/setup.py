# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sa11y']

package_data = \
{'': ['*']}

install_requires = \
['flake8>=3.9.2,<4.0.0', 'pytest>=6.2.4,<7.0.0', 'selenium==3.141.0']

setup_kwargs = {
    'name': 'sa11y',
    'version': '0.0.2',
    'description': 'The Selenium Accessibility Project',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
