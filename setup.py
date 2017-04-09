from distutils.core import setup
import os

setup(
    name         = 'thermostate',
    version      = '1.0.0',
    author       = 'Neal DeBuhr',
    author_email = 'ndebuhr@protonmail.com',
    license      = 'MIT',
    description  = 'thermostate allows you to solve for unknown parameters in '
    'simple thermodynamic systems, such as those typically analyzed in '
    'undergraduate thermodynamics courses',
    url          = 'https://github.com/ndebuhr/thermo-state-solver',
    packages     = [
        'thermo-state-solver',
    ],
    package_data = {
        'thermo-state-solver': [f for f in os.listdir('thermo-state-solver') if '.' not in f]
    },
    scripts          = ['bin/thermostate'],
    install_requires = [
        'iapws >= 0.0.1',
        'CoolProp >= 0.0.1',
        'scipy >= 0.0.1',
        'numpy >= 0.0.1',
    ]
)
