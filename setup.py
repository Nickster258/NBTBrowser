from setuptools import setup

setup(
    name="nbtbrowser",
    version="1.1",
    author="Nicholas Stonecipher",
    author_email="nickster258@users.noreply.github.com",
    packages=['nbtbrowser'],
    install_requires=[
        'nbtlib~=1.7.0',
        'tabulate~=0.8.7'
    ],
    entry_points={
        'console_scripts': [
            'nbtbrowser=nbtbrowser.__main__:main'
        ]
    }
)
