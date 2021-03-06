import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyourls3",
    version="1.0.1",
    author="Thomas Pain",
    author_email="pyourls3@tdpain.net",
    description="The official Python 3 API wrapper for YOURLS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.tdpain.net/projects/pyourls3",
    packages=["pyourls3"],
    classifiers=[
        "Programming Language :: Python :: 3",
	"Programming Language :: Python :: 3.5",
	"Programming Language :: Python :: 3.6",
	"Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires=["requests",
                      "certifi>=2017.4.17",
                      "chardet<3.1.0,>=3.0.2",
                      "idna<2.9,>=2.5",
                      "urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1"]
)
