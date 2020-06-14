from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = [
"batemaneq>=0.2.2",
"Pint>=0.12",
"importlib_resources; python_version<'3.7'",
]

setup(
    name ='decaychain',
    version ='0.6.7',
    description='Module to radioactively decay radioactive elements using the ICRP-107 and Bateman Equation',
#   package_dir={''},
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering",
        "Topic :: Education ",
        ],
    packages=find_packages(),
    author="Kenneth McKee",
    author_email="kenneth.mckee@protonmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Rolleroo/decaychain",
    python_requires='>=3.6',
    install_requires=requirements,
include_package_data = True,
package_data = {
'' : ['*.NDX'],
}
)