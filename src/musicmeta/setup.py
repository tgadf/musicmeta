from distutils.core import setup
import setuptools

setup(
  name = 'mp3id',
  py_modules = ['mp3id', 'musicID'],
  version = '0.0.1',
  description = 'A Python Wrapper For Mp3 Tag IO',
  long_description = open('README.md').read(),
  author = 'Thomas Gadfort',
  author_email = 'tgadfort@gmail.com',
  license = "MIT",
  url = 'https://github.com/tgadf/mp3id',
  keywords = ['metadata', 'mp3'],
  classifiers = [
    'Development Status :: 3',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities'
  ],
  install_requires=['mutagen>=1.42.0'],
  dependency_links=['git+ssh://git@github.com/tgadf/mp3id.git#egg=mp3id-0.0.1', 'git+ssh://git@github.com/tgadf/utils.git#egg=utils-0.0.1']
)
 
