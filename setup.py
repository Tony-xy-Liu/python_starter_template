import os, sys
from pathlib import Path
import setuptools

USER = "hallamlab" # github id
HERE = Path(os.path.realpath(__file__)).parent
NAME = os.listdir(HERE.joinpath("src"))[0].lower()
ENTRY_POINTS =  [
    f'{NAME} = {NAME}.cli:main',
    # f'shrt = {NAME}.cli:main', # feel free to abbreviate the command
]
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open(HERE.joinpath(f"src/{NAME}/version.txt")) as f:
    VERSION = f.read()

if __name__ == "__main__":
    setuptools.setup(
        name=NAME,
        version=VERSION,
        author="author 1, author 2",
        author_email="your@email.com",
        description="a starter package for a python based tool",
        long_description=long_description,
        long_description_content_type="text/markdown",
        license_files = ('LICENSE',),
        url=f"https://github.com/{USER}/{NAME}",
        project_urls={
            "Bug Tracker": f"https://github.com/{USER}/{NAME}/issues",
        },
        classifiers=[
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
        ],
        package_dir={"": "src"},
        packages=setuptools.find_packages(where="src"),
        package_data={
            "":[ # "" is all packages
                "version.txt",
            ],
            # examples
            # "package-name": ["*.txt"],
            # "test_package": ["res/*.txt"],
        },
        entry_points={
            'console_scripts': ENTRY_POINTS,
        },
        python_requires=">=3.11",
        install_requires=[
            "packaging >=21.0",
        ]
    )