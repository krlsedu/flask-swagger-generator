import setuptools
from version import get_version

VERSION = get_version()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('requirements.txt', encoding="utf-8") as f:
    required = f.read().splitlines()

setuptools.setup(
    name="flask-swagger-init",
    version=VERSION,
    license="MIT",
    author="Carlos Eduardo",
    description="A library for generating and publishing Swagger specifications for Flask applications.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/krlsedu/flask-swagger-generator.git",
    packages=setuptools.find_packages(exclude=['tests', 'tests.*']),
    keywords=['Flask', 'swagger', 'swagger generator', 'OpenAPI'],
    classifiers=[
        "Intended Audience :: Developers",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Programming Language :: Python :: 3.15',
        "Topic :: Software Development",
    ],
    install_requires=required,
    python_requires='>=3.11',
    include_package_data=True,
)
