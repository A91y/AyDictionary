import setuptools

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()
with open("LICENSE", "r", encoding="utf8") as fl:
    LICENSE = fl.read()

setuptools.setup(
    name="AyDictionary",
    version="0.0.1",
    author="A91y",
    author_email="ayush.agr254@gmail.com",
    description="A dictionary module for Python (Modification of PyDictionary)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/A91y/AyDictionary",
    project_urls={
        "Bug Tracker": "https://github.com/A91y/AyDictionary/issues",
        "Repository": "https://github.com/A91y/AyDictionary"
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    install_requires=[
        'bs4',
        'click',
        'requests'
    ],
    python_requires=">=3.6",
    license=LICENSE
)
