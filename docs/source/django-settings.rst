Django Settings for djangoMapCluster
====================================

Configuration Parameters
------------------------

The following table outlines the available settings for djangoMapCluster, detailing their data types, examples, and whether they are mandatory or optional.

+---------------------------------------+------------+--------------------------------------------------+---------------------------+
| Setting                               | Type       | Example                                          | Required                  |
+=======================================+============+==================================================+===========================+
| DJANGOMAPCLUSTER_GEODJANGO_MODEL      | string     | 'app_name.ModelName'                             | Required                  |
+---------------------------------------+------------+--------------------------------------------------+---------------------------+
| DJANGOMAPCLUSTER_COORDINATES_COLUMN   | string     | 'coordinates'                                    | Required                  |
+---------------------------------------+------------+--------------------------------------------------+---------------------------+
| DJANGOMAPCLUSTER_COORDINATES_COLUMN_SRID | integer | 3857                                             | Optional                  |
+---------------------------------------+------------+--------------------------------------------------+---------------------------+
| DJANGOMAPCLUSTER_FILTERS              | string[]   | ['db_column_1', 'db_column_2']                   | Optional                  |
+---------------------------------------+------------+--------------------------------------------------+---------------------------+
| DJANGOMAPCLUSTER_PINCOLUMN            | string     | 'db_column'                                      | Optional                  |
+---------------------------------------+------------+--------------------------------------------------+---------------------------+
| DJANGOMAPCLUSTER_GIS_MODEL_SERIALIZER | string     | 'myapp.api.serializers.DatasetRetrieveSerializer'| Optional                  |
+---------------------------------------+------------+--------------------------------------------------+---------------------------+

Detailed Descriptions
---------------------

**DJANGOMAPCLUSTER_GEODJANGO_MODEL**
    Specifies the Django model that djangoMapCluster will query.

**DJANGOMAPCLUSTER_COORDINATES_COLUMN**
    Defines the GIS column of the model specified in DJANGOMAPCLUSTER_GEODJANGO_MODEL.

**DJANGOMAPCLUSTER_COORDINATES_COLUMN_SRID** *(optional)*
    djangoMapCluster attempts to automatically determine the SRID of your database column. If unsuccessful, *4326* will be used as a default.

**DJANGOMAPCLUSTER_FILTERS**
    Restricts the columns that can be used as filters within queries.

**DJANGOMAPCLUSTER_PINCOLUMN**
    Allows for the specification of a database column to vary markers for pins with a count of one.

    Example configuration:

    .. code-block:: python

        DJANGOMAPCLUSTER_PINCOLUMN = 'style'

    This setting works in conjunction with the following configuration of djangoMapClusterClient:

    .. code-block:: javascript

        const settings = {
            singlePinImages : {
                'stone': '/static/djangoMapCluster/pin_stone.png',
                'flower': '/static/djangoMapCluster/pin_flower.png'
            }
        };

        const djangoMapClusterClient = new djangoMapClusterOpenLayers(map, apiUrl, markerFolderPath, settings);

    If the `style` column of the dataset equals `stone`, `/static/djangoMapCluster/pin_stone.png` will be used as the marker image.

**DJANGOMAPCLUSTER_GIS_MODEL_SERIALIZER**
    Defines the Django REST Framework serializer used for retrieving datasets with `djangoMapClusterClient.getMapContents`.
    This serializer is also utilized for data received by `djangoMapClusterClient.onFinalClick`.

**Example Configuration with All Entries**:

.. code-block:: python

    DJANGOMAPCLUSTER_GEODJANGO_MODEL = 'anymap.Gardens'
    DJANGOMAPCLUSTER_COORDINATES_COLUMN = 'coordinates'
    DJANGOMAPCLUSTER_COORDINATES_COLUMN_SRID = 3857
    DJANGOMAPCLUSTER_FILTERS = ['rating', 'free_entrance', 'last_renewal', 'style']
    DJANGOMAPCLUSTER_PINCOLUMN = 'style'