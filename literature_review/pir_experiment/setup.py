from setuptools import setup, find_packages

setup(
    name="pir-experiment",
    version='0.1',
    packages=find_packages(include=['src', \
                    'src.experiments', \
                    'src.primitives', \
                    'src.utils']),
    author="bt3gl",
    install_requires=['python-dotenv'],
    entry_points={
        'console_scripts': ['pir=src.main:run']
    },
)
