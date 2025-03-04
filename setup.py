import pathlib
import setuptools

setuptools.setup(
    name="sarif_filter",
    version="1.0.4",
    author="Tim Honisett",
    author_email="tim.honisett@hotmail.co.uk",
    description="Filters out SARIF file results from CodeQL query by ID",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/timh1975/sarif_filter",
    project_urls={
        "Source": "https://github.com/timh1975/sarif_filter",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
    ],
    python_requires=">=3.0",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "sarif_filter=sarif_filter.__main__:main",
        ]
    },
    include_package_data=True,
)
