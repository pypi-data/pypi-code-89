#!/usr/bin/env python
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()
    requirements = [req.replace('==', '>=') for req in requirements]

# normal setuptool inputs
setuptools.setup(
    name='pollination-direct-sun-hours',                                     # will be used for package name
    author='ladybug-tools',                                                 # the owner account for this package - required if pushed to Pollination
    author_email='info@ladybug.tools',
    packages=setuptools.find_namespace_packages(                            # required - that's how pollination find the package
        include=['pollination.*'], exclude=['tests', '.github']
    ),
    install_requires=requirements,
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    url='https://github.com/pollination/direct-sun-hours',                   # will be translated to home
    project_urls={
        'icon': 'https://raw.githubusercontent.com/ladybug-tools/artwork/master/icons_components/honeybee/png/directsun.png',
        'docker': 'https://hub.docker.com/r/ladybugtools/honeybee-radiance'
    },
    description='Direct sun hours recipe for Pollination.',                  # will be used as package description
    long_description=long_description,                                      # will be translated to ReadMe content on Pollination
    long_description_content_type="text/markdown",
    maintainer='mostapha, ladybug-tools',                                   # Package maintainers. For multiple maintainers use comma
    maintainer_email='mostapha@ladybug.tools, info@ladybug.tools',
    keywords='honeybee, radiance, ladybug-tools, daylight, direct-sun-hours',  # will be used as keywords
    license='PolyForm Shield License 1.0.0, https://polyformproject.org/wp-content/uploads/2020/06/PolyForm-Shield-1.0.0.txt',  # the license link should be separated by a comma
    zip_safe=False
)
