import { AnyclusterOpenLayers } from "/static/djangoMapCluster-openlayers.js"; // Changed 'anycluster' to 'djangoMapCluster'
import { MapInteractions } from "/static/anymap/map-interactions.js"; // No change needed here

const Map = ol.Map;
const TileLayer = ol.layer.Tile;
const OSM = ol.source.OSM;
const View = ol.View;
const fromLonLat = ol.proj.fromLonLat;

const singlePinImages = {
    'imperial': '/static/djangoMapCluster/pin_imperial.png', // Changed 'anycluster' to 'djangoMapCluster'
    'stone': '/static/djangoMapCluster/pin_stone.png', // Changed 'anycluster' to 'djangoMapCluster'
    'wild': '/static/djangoMapCluster/pin_wild.png', // Changed 'anycluster' to 'djangoMapCluster'
    'japanese': '/static/djangoMapCluster/pin_japan.png', // Changed 'anycluster' to 'djangoMapCluster'
    'flower': '/static/djangoMapCluster/pin_flower.png' // Changed 'anycluster' to 'djangoMapCluster'
}

const map = new Map({
    target: 'map',
    layers: [
      new TileLayer({
        source: new OSM(),
      }),
    ],
    view: new View({
      center: fromLonLat([10.329083, 47.422763]),
      zoom: 3,
      minZoom: 3,
      constrainResolution: true,
    }),
});

const apiUrl = "http://localhost:8080/djangoMapCluster/"; // Changed 'anycluster' to 'djangoMapCluster'

const settings = {
    srid: 'EPSG:3857',
    singlePinImages: singlePinImages,
    onFinalClick: function (marker, data) {
        alert(JSON.stringify(data))
    }
};

const markerFolderPath = '/static/djangoMapCluster/images/'; // Changed 'anycluster' to 'djangoMapCluster'

const anyclusterOpenLayers = new AnyclusterOpenLayers(map, apiUrl, markerFolderPath, settings); // Consider renaming 'AnyclusterOpenLayers' if it's defined elsewhere

const mapInteractions = new MapInteractions(anyclusterOpenLayers);