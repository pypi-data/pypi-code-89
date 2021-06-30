import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name= "pipmaker",

     version="0.1",

     scripts=["pipmaker=0.2.py"],

     author="Dante Annetta",

     author_email="dannetta@lasalleflorida.edu.ar",

     description="A simple way to upload your python modules into PyPi!",

     long_description=long_description,

     long_description_content_type="text/markdown",

     url="https://github.com/DanteAnnetta/pipmaker",

     packages=setuptools.find_packages(),

     classifiers=[

         "Programming Language :: Python :: 3",

         "License :: OSI Approved :: MIT License",

         "Operating System :: OS Independent",

     ],

)