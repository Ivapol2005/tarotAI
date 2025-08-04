from setuptools import setup, find_packages

setup(
    name='tarotAI',
    version='0.1.0',
    description='A simple Tarot card reading Python module',
    author='Твоє імʼя',
    author_email='твій.email@example.com',
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=[
        # ad here requirements if need
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
