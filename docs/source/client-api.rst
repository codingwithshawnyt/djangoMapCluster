djangoMapCluster Client API
===========================

Instantiation
-------------

The djangoMapClusterClient class is tailored to your specific map framework.

.. code-block:: javascript

    let djangoMapClusterOpenLayers = new djangoMapClusterOpenLayers(map, apiUrl, markerFolderPath, settings);
    let djangoMapClusterLeaflet = new djangoMapClusterLeaflet(map, apiUrl, markerFolderPath, settings);
    let djangoMapClusterGoogle = new djangoMapClusterGoogle(apiKey, map, apiUrl, markerFolderPath, settings);


Parameters
^^^^^^^^^^

map
    An instantiated map object. Supports :code:`ol.Map`, :code:`L.map`, or :code:`google.maps.Map`.

apiUrl
    The URL of your Django project where djangoMapCluster is installed. 
    Example: :code:`http://localhost:8080/djangoMapCluster/api`.

apiKey *(Google Maps only)*
    Your Google Maps API key.

markerFolderPath
    Path to the images djangoMapCluster uses to represent clusters on the map.
    Example: :code:`/static/djangoMapCluster/`.

settings (optional)
    Configuration object for the djangoMapCluster client.


Settings
--------

Available settings:

+---------------------+------------+--------------------------------------------------+----------------------------+
| Setting             | Type       | Possible Values, Example                         | Default                    |
+=====================+============+==================================================+============================+
| srid                | string     | :code:`EPSG:4326`, :code:`EPSG:3857`             | :code:`EPSG:4326`          |
+---------------------+------------+--------------------------------------------------+----------------------------+
| kmeansGridSize      | integer    |                                                  | 150                        |
+---------------------+------------+--------------------------------------------------+----------------------------+
| gridGridSize        | integer    |                                                  | 64                         |
+---------------------+------------+--------------------------------------------------+----------------------------+
| clusterMethod       | string     | :code:`kmeans`, :code:`grid`                     | :code:`kmeans`             |
+---------------------+------------+--------------------------------------------------+----------------------------+
| geometryType        | string     | :code:`viewport`, :code:`area`                   | :code:`viewport`           |
+---------------------+------------+--------------------------------------------------+----------------------------+
| area                | geoJSON    |                                                  | null                       |
+---------------------+------------+--------------------------------------------------+----------------------------+
| iconType            | string     | :code:`exact`, :code:`rounded`                   | :code:`rounded`            |
+---------------------+------------+--------------------------------------------------+----------------------------+
| onFinalClick        | function   |                                                  |                            |
+---------------------+------------+--------------------------------------------------+----------------------------+
| singlePinImages     | object     | .. code-block:: javascript                       | {}                         |
|                     |            |                                                  |                            |
|                     |            |   {                                              |                            |
|                     |            |    'stone': '/static/djangoMapCluster/pin_stone.png',  |                            |
|                     |            |    'flower': '/static/djangoMapCluster/pin_flower.png' |                            |
|                     |            |   }                                              |                            |
+---------------------+------------+--------------------------------------------------+----------------------------+
| markerImageSizes    | object     |                                                  | .. code-block:: javascript |
|                     |            |                                                  |                            |
|                     |            |                                                  |   {                        |
|                     |            |                                                  |        1: [24, 39],        |
|                     |            |                                                  |        5: [30, 30],        |
|                     |            |                                                  |       10: [30, 30],        |
|                     |            |                                                  |       50: [40, 40],        |
|                     |            |                                                  |      100: [40, 40],        |
|                     |            |                                                  |     1000: [50, 50],        |
|                     |            |                                                  |    10000: [60, 60]         |
|                     |            |                                                  |   }                        |
+---------------------+------------+--------------------------------------------------+----------------------------+
| gridFillColors      | object     |                                                  |                            |
+---------------------+------------+--------------------------------------------------+----------------------------+
| gridStrokeColors    | object     |                                                  |                            |
+---------------------+------------+--------------------------------------------------+----------------------------+
| onGotClusters       | function   |                                                  |                            |
+---------------------+------------+--------------------------------------------------+----------------------------+

settings.onFinalClick
    Defines the action when the user clicks on a final marker.

    .. code-block:: javascript

        const settings = {
            onFinalClick: function (marker, data) {
                alert(JSON.stringify(data))
            }
        };


settings.onGotClusters
    Defines actions after the map has been updated with new clusters, such as after panning or zoom level changes.

    .. code-block:: javascript

        const settings = {
            onFinalClick: function () {
                console.log('got new clusters!')
            }
        };


Filtering
---------

Manage the datasets displayed on your map using filters.

Filter Object
^^^^^^^^^^^^^

.. code-block:: javascript

    const filter = {
        "column": "DATABASE_COLUMN",
        "operator": "OPERATOR",
        "value" : VALUE,
        "logicalOperator": "LOGICAL_OPERATOR" // optional, only has effect if more than one filter is present
    };


DATABASE_COLUMN
    The database column to which this filter should be applied.

VALUE
    The value of the filter can be of type :code:`string`, :code:`number`, :code:`bool`, or :code:`Array`.

OPERATOR
    The operator used in the filter, options include:

    +---------------------+----------------------------------------------------+----------------------------------------+
    | Operator            | Description                                        | Applicable to Value Types              |
    +=====================+====================================================+========================================+
    | =                   | Equals                                             | string, number, bool                   |
    +---------------------+----------------------------------------------------+----------------------------------------+
    | !=                  | Does not equal                                     | string, number, bool                   |
    +---------------------+----------------------------------------------------+----------------------------------------+
    | >=                  | Larger than or equal to                            | number                                 |
    +---------------------+----------------------------------------------------+----------------------------------------+
    | <=                  | Smaller than or equal to                           | number                                 |
    +---------------------+----------------------------------------------------+----------------------------------------+
    | startswith          | String starts with, case insensitive               | string                                 |
    +---------------------+----------------------------------------------------+----------------------------------------+
    | contains            | String contains, case insensitive                  | string                                 |
    +---------------------+----------------------------------------------------+----------------------------------------+
    | in                  | Values equal to one of the list items              | Array                                  |
    +---------------------+----------------------------------------------------+----------------------------------------+
    | not in              | Values different from all of the list items        | Array                                  |
    +---------------------+----------------------------------------------------+----------------------------------------+


LOGICAL_OPERATOR

    The logical operator used to combine multiple filters:

    +---------------------+----------------------------------------------------+
    | Logical Operator    | Description                                        | 
    +=====================+====================================================+
    | AND                 | Filters are concatenated using SQL AND             |
    +---------------------+----------------------------------------------------+
    | OR                  | Filters are concatenated using SQL OR              |
    +---------------------+----------------------------------------------------+


    The default method for combining filters is :code:`AND`.



Filtering Methods of djangoMapClusterClient
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

filter(filterObject or filterObject[], reloadMarkers *boolean*)
    Applies the specified filter to djangoMapClusterClient, removing all other filters.

addFilter(filterObject, reloadMarkers *boolean*)
    Adds the specified filter to djangoMapClusterClient if it does not already exist. Does not remove previously added filters.

removeFilter(filterObject, reloadMarkers *boolean*)
    Removes the specified filter from djangoMapClusterClient if it exists.

addFilters(filterObject[], reloadMarkers *boolean*)
    Adds multiple filters to djangoMapClusterClient at once. Does not remove previously added filters.

removeFilters(filterObject[], reloadMarkers *boolean*)
    Removes multiple filters from djangoMapClusterClient at once.

resetFilters(reloadMarkers *boolean*)
    Removes all filters from djangoMapClusterClient.
   
Examples
^^^^^^^^

1. Applying one filter and refreshing the map.

.. code-block:: javascript

    let djangoMapClusterLeaflet = new djangoMapClusterLeaflet(map, apiUrl, markerFolderPath, settings);
    const filter = {
        "column": "style",
        "value": "flower",
        "operator": "=" 
    };

    djangoMapClusterLeaflet.filter(filter);


2. Applying two filters and refreshing the map only after applying the second filter. This equals an :code:`AND` lookup.

.. code-block:: javascript

    let djangoMapClusterLeaflet = new djangoMapClusterLeaflet(map, apiUrl, markerFolderPath, settings);
    const styleFilter = {
        "column": "style",
        "value": "flower",
        "operator": "=" 
    };

    djangoMapClusterLeaflet.addFilter(styleFilter, false);

    const entranceFilter = {
        "column": "free_entrance",
        "value": true,
        "operator": "=" 
    };

    djangoMapClusterLeaflet.addFilter(entranceFilter);

3. Applying a list filter and refreshing the map. This equals an :code:`OR` lookup.
   
.. code-block:: javascript

    let djangoMapClusterLeaflet = new djangoMapClusterLeaflet(map, apiUrl, markerFolderPath, settings);
    const filter = {
        "column": "style",
        "value": ["flower", "stone"],
        "operator": "in" 
    };

    djangoMapClusterLeaflet.filter(filter);


4. Applying a logical operator

.. code-block:: javascript

    let djangoMapClusterLeaflet = new djangoMapClusterLeaflet(map, apiUrl, markerFolderPath, settings);
    const filters = [
        {
            "column": "style",
            "value": "flower",
            "operator": "=" 
        },
        {
            "column": "style",
            "value": "stone",
            "operator": "=",
            "logicalOperator": "OR"
        },
    ];

    djangoMapClusterLeaflet.filter(filters);


Nested Filtering
----------------

If the standard filtering options are still not enough and you require more complex queries, you can use nested filters, alongside with logical operators.


Example
^^^^^^^

.. code-block:: javascript

    let djangoMapClusterLeaflet = new djangoMapClusterLeaflet(map, apiUrl, markerFolderPath, settings);
    const filters = [
        {
            "filters": [
                {
                    "column": "style",
                    "value": "flower",
                    "operator": "=" 
                },
                {
                    "column": "free_entrance",
                    "value": true,
                    "operator": "=" 
                }
            ]
        },
        {
            "filters": [
                {
                    "column": "style",
                    "value": "stone",
                    "operator": "=",
                },
                {
                    "column": "free_entrance",
                    "value": false,
                    "operator": "=" 
                }
            ],
            "logicalOperator": "OR"
        }
    ];

    djangoMapClusterLeaflet.filter(filters);



Counting
--------

You can count the objects which are currently displayed on the map in different ways.

getMapContentCount(modulations:object)   
    You can count what currently is visible on the map.

    .. code-block:: javascript

        let djangoMapClusterLeaflet = new djangoMapClusterLeaflet(map, apiUrl, markerFolderPath, settings);

        const mapContentCount = await djangoMapClusterLeaflet.getMapContentCount();

        const count = mapContentCount["count"];


    If no modulations are applied, the returned object looks like this:
    
    .. code-block:: javascript

        {
            "count": 756,
            "modulations": {}
        }

    
    **Modulations**

    Modulations are like filters, but they are applied only for the current :code:`getMapContentCount` request.
    They are not stored in :code:`djangoMapClusterClient.filters`.
    You can use simple filters as well as nested filters for modulations.
    
    .. code-block:: javascript

        let djangoMapClusterLeaflet = new djangoMapClusterLeaflet(map, apiUrl, markerFolderPath, settings);
        
        const modulations = {
            "stone" : {
                "column": "style",
                "value": "stone",
                "operator": "="
            },
            "flower" : {
                "column": "style",
                "value": "flower",
                "operator": "="
            },
            "flowerOrStone" : {
                "filters" : [
                    {
                        "column": "style",
                        "value": "stone",
                        "operator": "="
                    },
                    {
                        "column": "style",
                        "value": "flower",
                        "operator": "=",
                        "logicalOperator": "OR"
                    },
                ]
            }
        };

        const mapContentCount = await djangoMapClusterLeaflet.getMapContentCount(modulations);

    The returned object looks like this:

    .. code-block:: javascript

        {
            "count" : 756,
            "modulations": {
                "stone": {
                    "count": 102
                },
                "flower": {
                    "count": 76
                },
                "flowerOrStone": {
                    "count": 178
                }
            }
        }


getGroupedMapContents(groupBy:string)    
    You can query a list of the currently visible contents, grouped by a database column.
    
    .. code-block:: javascript

        let djangoMapClusterLeaflet = new djangoMapClusterLeaflet(map, apiUrl, markerFolderPath, settings);

        const groupBy = "style";
        const groupedMapContents = djangoMapClusterLeaflet.getGroupedMapContents(groupBy);

    
    The returned object looks like this:

    .. code-block:: javascript

        {
            "flower": {
                "count": 1773
            },
            "imperial": {
                "count": 1884
            },
            "japanese": {
                "count": 1893
            },
            "other": {
                "count":1883
            },
            "stone":{
                "count":1783
            }
        }

    :code:`flower`, :code:`imperial`, :code:`japanese`, :code:`other` and :code:`stone` are the occurring values of the column :code:`style`, which had been applied in the :code:`GROUP BY` SQL clause.



Getting Content
---------------

getMapContents(limit?: number, offset?:number)
    Fetches a list of the currently displayed data. By default, model instances with all their fields are returned.
    You can configure this using a custom serializer with :code:`settings.DJANGOMAPCLUSTER_GIS_MODEL_SERIALIZER`.