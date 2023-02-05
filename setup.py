from setuptools import setup, find_packages

setup(
    name='shakkala',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'tensorflow==2.9.3',
        'h5py==3.8.0',
        'nltk==3.6.6',
        'numpy==1.24.1',
        'click==8.1.3'
    ],
)
