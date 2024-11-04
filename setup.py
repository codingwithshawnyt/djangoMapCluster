from setuptools import setup, find_packages

# Open the README.md file and read its contents to use as the extended description
with open("README.md", "r") as file_handle:
    detailed_description = file_handle.read()

# List of packages that are required for this project
required_packages = [
    'psycopg2',
    'djangorestframework',
    'jsonschema',
]

# Configuration for setup function
setup(
    name="djangoMapCluster",  # Name of the package
    version='2.5.0',  # Version of the package
    description='DjangoMapCluster enables server-side clustering of map markers specifically designed for GeoDjango applications',  # Short description of the package
    long_description=detailed_description,  # Long description read from README.md
    long_description_content_type="text/markdown",  # Type of the long description content
    license='The MIT License',  # License type
    platforms=['OS Independent'],  # Platform compatibility
    keywords='django, cluster, kmeans, grid, server-side clustering',  # Keywords for the package
    author='Shawn Ray',  # Author of the package
    author_email='shawnray5699@gmail.com',  # Email of the author
    url='https://github.com/codingwithshawnyt/djangoMapCluster',  # URL to the project's repository
    packages=find_packages(),  # Automatically find all packages in the project
    classifiers=[  # Classifiers to categorize the project
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Minimum version requirement of Python
    include_package_data=True,  # Include all data files specified in MANIFEST.in
    install_requires=required_packages,  # List of packages that need to be installed along with this package
)
