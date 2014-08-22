try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name' : 'zsenda',
    'version' : '1.0.0',
    'install_requires':['pytest'],
    'py_modules' : ['zsenda']
}

setup(**config)
