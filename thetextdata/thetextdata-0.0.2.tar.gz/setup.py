#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['thetextdata']

package_data = \
{'': ['*']}

install_requires = \
['spacy==3.0.5',
 'spacy_universal_sentence_encoder==0.4.1',
 'veriservice==0.0.33',
 'pandas==1.1.2',
 'tensorflow_text==2.4.3']

setup(name='thetextdata',
      version='0.0.2',
      description="Let's process some text",
      author='Berk Gokden',
      author_email='berkgokden@gmail.com',
      url='https://github.com/bgokden/text-data',
      packages=packages,
      package_data=package_data,
      install_requires=install_requires,
      python_requires='>=3.7',
     )
