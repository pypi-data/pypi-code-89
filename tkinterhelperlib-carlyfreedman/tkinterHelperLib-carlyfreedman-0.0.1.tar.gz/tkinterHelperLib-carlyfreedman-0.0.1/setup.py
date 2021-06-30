
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tkinterHelperLib-carlyfreedman",
    version="0.0.1",
    author="Carly Freedman",
    author_email="carlyfreedman4@gmail.com",
    description="Helps to make tkinter more user-friendly",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Carly-Freedman/TkinterHelperLib.git",
    project_urls={
        "TkinterLibHelper": "https://github.com/Carly-Freedman/TkinterHelperLib.git",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)