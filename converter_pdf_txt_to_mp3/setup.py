from setuptools import setup, find_packages

setup(
    name='converter_pdf_txt_to_mp3',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'PyPDF2',
        'pyttsx3',
        'gtts'
    ],
    entry_points={
        'console_scripts': [
            'converter_pdf_txt_to_mp3=converter_pdf_txt_to_mp3.converter:convert_file_to_mp3',
        ],
    },
    author='clenio',
    author_email='mouraaf@gmail.com',
    description='Um pacote para converter documentos PDF e TXT em arquivos MP3',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/clenio77/NTT-DATA/pdf_txt_to_mp3',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
