Installation and Configuration
==============================

Prerequisites
-------------

* Django 2.x, 3.x, or 4.x
* Python 3
* GeoDjango
* PostGIS 2.x
* (Recommended for k-means clustering) k-means PostgreSQL extension: https://github.com/umitanuki/kmeans-postgresql

k-means PostGIS Extension
-------------------------

**Installing the k-means PostgreSQL Extension (Optional, Required for k-means Clustering)**

1. Download and unzip the k-means PostgreSQL extension from https://github.com/umitanuki/kmeans-postgresql on your server.
2. Ensure the development packages for your PostgreSQL server are installed (e.g., `sudo apt-get install libpq-dev postgresql-server-dev-10`).

3. Within the unzipped k-means directory, execute the following commands (example for Ubuntu):

   .. code-block:: bash

      make
      sudo make install
      psql -f /usr/share/postgresql/14/extension/kmeans.sql -d YOUR_GEODJANGO_DATABASE

   Execute the above commands as a PostgreSQL superuser, such as the user 'postgres'. This grants access to the k-means functions necessary for pin-based clustering.

For openSUSE, the `psql` command would be:

.. code-block:: bash

   psql -f /usr/share/postgresql15/extension/kmeans.sql -d YOUR_GEODJANGO_DATABASE

The version number (e.g., *14* or *15*) corresponds to the version of PostgreSQL you are using.

Django Configuration
--------------------

**Installing djangoMapCluster with Your Django Installation**

1. Install djangoMapCluster using pip or by manually unzipping the folder into your project directory:

   .. code-block:: bash

      pip install djangoMapCluster

2. Add 'djangoMapCluster' to your `INSTALLED_APPS` in `settings.py`.

3. Configure the necessary settings in `settings.py`:

   .. code-block:: python

     DJANGOMAPCLUSTER_GEODJANGO_MODEL = "yourapp.models.your_geodjango_model"
     DJANGOMAPCLUSTER_COORDINATES_COLUMN = "your_geometric_column"

4. Update `urls.py` to include djangoMapCluster's URLs:

   .. code-block:: python

      path('djangoMapCluster/', include('djangoMapCluster.urls')),