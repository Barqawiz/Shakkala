from setuptools import setup, find_packages

with open("PIP_README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='shakkala',
    version='1.7',
    author='Ahmad Albarqawi',
    packages=find_packages(),
    include_package_data=True,
    url='https://ahmadai.com/shakkala/',
    data_files=[('dictionary', ['shakkala/dictionary/input_vocab_to_int.pickle',
                                'shakkala/dictionary/output_int_to_vocab.pickle']),
                ('model', ['shakkala/model/middle_model.h5',
                           'shakkala/model/second_model6.h5',
                           'shakkala/model/simple_model.h5'])],
    description="Deep learning for Arabic text Vocalization - التشكيل الالي للنصوص العربية",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[        'tensorflow==2.9.3',        'h5py==3.8.0',        'nltk==3.6.6',        'numpy==1.24.1',        'click==8.1.3'    ],
)
