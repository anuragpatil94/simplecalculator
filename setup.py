from setuptools import setup, find_packages

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Education",
    "Operating System :: Microsoft :: Windows :: Windows 10",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
]

setup(
    name="anurag-simplecalculator",
    version="0.0.1",
    description="A very basic calculator",
    long_description=open("README.md").read() + "\n\n" + open("CHANGELOG.md").read(),
    url="",
    author="Anurag Patil",
    author_email="",
    license="MIT",
    classifiers=classifiers,
    keywords=["calculator", "educative", "example"],
    packages=find_packages(),
    install_requires=[""],
)