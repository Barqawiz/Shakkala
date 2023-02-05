from setuptools import setup, find_packages

setup(
    name='Shakkala',
    version='0.8',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['Shakkala', 'helper'],
    package_data={'': ['dictionary/*', 'model/*']},
    description="Deep learning for Arabic text Vocalization - التشكيل الالي للنصوص العربية",
    long_description="The Shakkala project presents a recurrent neural network for Arabic text vocalization that automatically forms Arabic characters (تشكيل الحروف) to enhance text-to-speech systems.",
    install_requires=[
        'tensorflow==2.9.3',
        'h5py==3.8.0',
        'nltk==3.6.6',
        'numpy==1.24.1',
        'click==8.1.3'
    ],
)
