import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple-default-backpropagation-ann-package",
    version="1.0.0",
    author="Adrianna Pater",
    author_email="andairka@wp.pl",
    description="A small and simple backpropagation neutral network which predicts titanic Survived.",
    url="https://github.com/andairka/Simple-default-Backpropagation-ANN",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)