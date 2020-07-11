from setuptools import setup, find_packages

setup(
    name="NBTBrowser",
    version="0.0.1",
    author="Nicholas Stonecipher",
    author_email="nickster258@users.noreply.github.com",
    packages=find_packages(),
    install_requires=[
        'nbtlib~=1.7.0',
        'tabulate~=0.8.7'
    ]
)
