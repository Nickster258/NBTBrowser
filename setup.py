from setuptools import setup, find_packages

setup(
    name="NBTBrowser",
    version="0.0.1",
    author="Nicholas Stonecipher",
    author_email="nickster258@users.noreply.github.com",
    packages=find_packages(),
    py_modules=['nbtbrowser'],
    entry_points='''
        [console_scripts]
        nbtbrowser=nbtbrowser:main
    ''',
    install_requires=[
        'Click',
        'nbtlib~=1.7.0',
        'tabulate~=0.8.7'
    ]
)
