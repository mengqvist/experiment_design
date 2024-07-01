from setuptools import setup, find_packages

setup(
    name='expdesign',
    version='0.1.0',
    author='Martin Engqvist',
    author_email='martin.engqdist@gmail.com',
    description='A package for generating experiment designs',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mengqvist/experiment-design',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        'numpy',
        'scipy',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
