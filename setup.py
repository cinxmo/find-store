from setuptools import setup

setup(
    name='find_store',
    version='0.1.0',
    author='Cindy Mo',
    author_email='cinxmo@gmail.com',
    packages=['find_store'],
    entry_points={
        'console_scripts': [
            'find_store = find_store.__main__:main'
        ]
    },
    description='Command Line Application for Finding Nearest Store',
)

