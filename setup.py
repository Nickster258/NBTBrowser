from setuptools import setup

setup(
    name="nbtbrowser",
    version="0.0.1",
    author="Nicholas Stonecipher",
    author_email="nickster258@users.noreply.github.com",
    py_modules=['nbtbrowser'],
    install_requires=[
        'Click',
        'nbtlib~=1.7.0',
        'tabulate~=0.8.7'
    ],
    entry_points='''
        [console_scripts]
        nbtbrowser=nbtbrowser:main
    '''
)
