from setuptools import setup, find_packages

setup(
    name='HornyCode',
    version='0.1.1',
    packages=find_packages(),
    description='OwO, whats this',
    author='MateuszDubaj',
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'hornyrun = hornycode.cli:main',
            'hornydecompile = hornycode.compiler:main',
            'hornycompile = hornycode.convert:main'
        ],
    },
)
