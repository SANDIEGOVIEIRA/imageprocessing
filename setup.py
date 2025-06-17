from setuptools import setup, find_packages

setup(
    name='imageprocessing',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Pillow'
    ],
    author='Seu Nome',
    author_email='seuemail@example.com',
    description='Um pacote simples de processamento de imagens com Pillow',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/seunome/imageprocessing',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
