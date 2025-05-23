import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="coloraiz",
    version="1.0.2",
    author="Morty",
    author_email="me@mortysmith.org",
    description="Simple way to add color to your terminal text output",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/",
    project_urls={
        "Bug Tracker": "https://github.com/",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        "colorama",
        "requests"
    ]
)
