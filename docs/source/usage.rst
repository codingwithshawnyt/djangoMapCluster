Basic Usage
===========

OpenLayers
----------

1. Installation or Manual Download of the djangoMapCluster-OpenLayers Client
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**npm Installation**

You can install djangoMapCluster-OpenLayers via npm with the following command:

.. code-block:: shell

    npm install djangoMapCluster-openlayers

**Manual Integration**

Alternatively, you may manually download and integrate the djangoMapCluster-OpenLayers client into your project's static assets.
Place the files `djangoMapCluster-openlayers.js` and `djangoMapCluster-openlayers.js.map` within your project's static directory.

2. Configuration of Marker Images
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
djangoMapCluster requires the provision of marker images to be displayed on the map. These images can either be custom-designed or sourced externally.

Ensure that these images are accessible to djangoMapCluster-OpenLayers. For instance, if utilizing Django templates, you should store the marker images within your static files directory, such as `{your_directory}/static/djangoMapCluster/`.

3. Script Creation for djangoMapCluster-OpenLayers Initialization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
    It is imperative to set `constrainResolution: true` in your `ol.View` to ensure the usage of only integer zoom levels.

    Below is an example script tailored for a Django template setup. If djangoMapCluster-OpenLayers was installed via npm, include the module using:
    
    .. code:: javascript
    
        import { djangoMapClusterOpenLayers } from 'djangoMapCluster-openlayers';

    **Important:** By default, OpenLayers operates under the `EPSG:3857` projection. Adjust your settings to align with this configuration if necessary.

.. code-block:: javascript

    import { djangoMapClusterOpenLayers } from '/static/djangoMapCluster-openlayers.js';

    const Map = ol.Map;
    const TileLayer = ol.layer.Tile;
    const OSM = ol.source.OSM;
    const View = ol.View;
    const fromLonLat = ol.proj.fromLonLat

    let map = new Map({
        target: 'map',
        layers: [
            new TileLayer({
                source: new OSM(),
            }),
        ],
        view: new View({
            center: fromLonLat([10.3, 47.4]),
            zoom: 3,
            minZoom: 3,
            constrainResolution: true,
        }),
    });

    const apiUrl = 'URL_TO_YOUR_SERVER_RUNNING_DJANGOMAPCLUSTER';

    const settings = {
        srid: 'EPSG:3857',
        onFinalClick: function (marker, data) {
            alert(JSON.stringify(data))
        }
    };

    const markerFolderPath = '/static/djangoMapCluster/images/';

    let djangoMapClusterOpenLayers = new djangoMapClusterOpenLayers(map, apiUrl, markerFolderPath, settings);
    
Incorporate this script into the appropriate Django template or JavaScript file to enable marker clustering on your OpenLayers map.

**Completion**

Upon successful integration and configuration, your OpenLayers map will now effectively cluster markers.

----

Leaflet
-------

1. Installation or Manual Download of the djangoMapCluster-Leaflet Client
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**npm Installation**

You can install djangoMapCluster-Leaflet via npm with the following command:

.. code-block:: shell

    npm install djangoMapCluster-leaflet

**Manual Integration**

Alternatively, you may manually download and integrate the djangoMapCluster-Leaflet client into your project's static assets.
Place the files `djangoMapCluster-leaflet.js` and `djangoMapCluster-leaflet.js.map` within your project's static directory.

2. Configuration of Marker Images
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
djangoMapCluster requires the provision of marker images to be displayed on the map. These images can either be custom-designed or sourced externally.

Ensure that these images are accessible to djangoMapCluster-Leaflet. For instance, if utilizing Django templates, you should store the marker images within your static files directory, such as `{your_directory}/static/djangoMapCluster/`.

3. Script Creation for djangoMapCluster-Leaflet Initialization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
    Below is an example script tailored for a Django template setup. If djangoMapCluster-Leaflet was installed via npm, include the module using:
    
    .. code:: javascript
    
        import { djangoMapClusterLeaflet } from 'djangoMapCluster-leaflet';

.. code-block:: javascript

    import { djangoMapClusterLeaflet } from '/static/djangoMapCluster-leaflet.js';

    let map = L.map('map', {
        center: [47.4, 10.3],
        zoom: 3,
        minZoom: 3,
        worldCopyJump: true,
    });

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

    const apiUrl = 'URL_TO_YOUR_SERVER_RUNNING_DJANGOMAPCLUSTER';

    const settings = {
        onFinalClick: function (marker, data) {
            alert(JSON.stringify(data))
        }
    };

    const markerFolderPath = '/static/djangoMapCluster/images/';

    let djangoMapClusterLeaflet = new djangoMapClusterLeaflet(map, apiUrl, markerFolderPath, settings);

Incorporate this script into the appropriate Django template or JavaScript file to enable marker clustering on your Leaflet map.

**Completion**

Upon successful integration and configuration, your Leaflet map will now effectively cluster markers.

----

Google Maps
-----------

1. Installation or Manual Download of the djangoMapCluster-Google Client
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**npm Installation**

You can install djangoMapCluster-Google via npm with the following command:

.. code-block:: shell

    npm install djangoMapCluster-google

**Manual Integration**

Alternatively, you may manually download and integrate the djangoMapCluster-Google client into your project's static assets.
Place the files `djangoMapCluster-google.js` and `djangoMapCluster-google.js.map` within your project's static directory.

2. Configuration of Marker Images
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
djangoMapCluster requires the provision of marker images to be displayed on the map. These images can either be custom-designed or sourced externally.

Ensure that these images are accessible to djangoMapCluster-Google. For instance, if utilizing Django templates, you should store the marker images within your static files directory, such as `{your_directory}/static/djangoMapCluster/`.

3. Script Creation for djangoMapCluster-Google Initialization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
    Below is an example script tailored for a Django template setup. If djangoMapCluster-Google was installed via npm, include the module using:
    
    .. code:: javascript
    
        import { djangoMapClusterGoogle } from 'djangoMapCluster-google';

.. code-block:: javascript

    import { djangoMapClusterGoogle } from "/static/djangoMapCluster-google.js";

    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 3,
        center: { lat: 47.4, lng: 10.3 },
    });

    const singlePinImages = {
        'imperial': '/static/djangoMapCluster/pin_imperial.png',
        'stone': '/static/djangoMapCluster/pin_stone.png',
        'wild': '/static/djangoMapCluster/pin_wild.png',
        'japanese': '/static/djangoMapCluster/pin_japan.png',
        'flower': '/static/djangoMapCluster/pin_flower.png'
    }

    const apiUrl = "http://localhost:8080/djangoMapCluster/";

    const settings = {
        singlePinImages: singlePinImages,
        onFinalClick: function (marker, data) {
            alert(JSON.stringify(data))
        }
    };

    const markerFolderPath = '/static/djangoMapCluster/images/';

    google.maps.event.addListenerOnce(map, 'bounds_changed', function() {
        const djangoMapClusterGoogle = new djangoMapClusterGoogle('{{ google_maps_api_key }}', map, apiUrl, markerFolderPath, settings);
    });

Incorporate this script into the appropriate Django template or JavaScript file to enable marker clustering on your Google Maps map.

**Completion**

Upon successful integration and configuration, your Google Maps map will now effectively cluster markers.