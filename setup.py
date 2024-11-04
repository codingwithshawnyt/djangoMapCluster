from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", "r") as file_handle:
    detailed_description = file_handle.read()

required_packages = [
    'psycopg2',
    'djangorestframework',
    'jsonschema',
]

setup(
    name="djangoMapCluster",
    version='2.5.0',
    description='DjangoMapCluster enables server-side clustering of map markers specifically designed for GeoDjango applications',
    long_description=detailed_description,
    long_description_content_type="text/markdown",
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='django, cluster, kmeans, grid, server-side clustering',
    author='Shawn Ray',
    author_email='shawnray5699@gmail.com',
    url='https://github.com/codingwithshawnyt/djangoMapCluster',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
    install_requires=required_packages,
)