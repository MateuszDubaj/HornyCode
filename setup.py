from setuptools import setup, find_packages

setup(
    name='HornyCode',
    version='0.1.1',
    packages=find_packages(),
    description='Run Python in horny furry language.',
    author='MateuszDubaj',
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'hornyrun = hornycode.cli:main',
            'hornycompile = hornycode.compiler:main',
            'dehornify = hornycode.convert:main'
        ],
    },
)

