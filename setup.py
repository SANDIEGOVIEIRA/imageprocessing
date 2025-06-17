from setuptools import setup, find_packages

setup(
    name='imageprocessing-sv',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Pillow'
    ],
    author='Sandiego Vieira',
    author_email='sandiegovieira@outlook.com',
    description='Um pacote simples de processamento de imagens com Pillow',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/SANDIEGOVIEIRA/imageprocessing',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
