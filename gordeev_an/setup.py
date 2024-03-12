from setuptools import setup, find_packages

setup(
    name='calculator',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'tk'
    ],
    entry_points={
        "console_scripts": [
            "calculator-start = calculator.calc:main",
        ],
    }
)
