"use strict";

import { AnyclusterLeaflet } from "/static/djangoMapCluster-leaflet.js"; // Changed 'anycluster' to 'djangoMapCluster'
import { MapInteractions } from "/static/anymap/map-interactions.js"; // No change needed here

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

const singlePinImages = {
    'imperial': '/static/djangoMapCluster/pin_imperial.png', // Changed 'anycluster' to 'djangoMapCluster'
    'stone': '/static/djangoMapCluster/pin_stone.png', // Changed 'anycluster' to 'djangoMapCluster'
    'wild': '/static/djangoMapCluster/pin_wild.png', // Changed 'anycluster' to 'djangoMapCluster'
    'japanese': '/static/djangoMapCluster/pin_japan.png', // Changed 'anycluster' to 'djangoMapCluster'
    'flower': '/static/djangoMapCluster/pin_flower.png' // Changed 'anycluster' to 'djangoMapCluster'
}

const apiUrl = "http://localhost:8080/djangoMapCluster/"; // Changed 'anycluster' to 'djangoMapCluster'

const settings = {
    singlePinImages: singlePinImages,
    onFinalClick: function (marker, data) {
        alert(JSON.stringify(data))
    }
};

const markerFolderPath = '/static/djangoMapCluster/images/'; // Changed 'anycluster' to 'djangoMapCluster'

const anyclusterLeaflet = new AnyclusterLeaflet(map, apiUrl, markerFolderPath, settings); // Consider renaming 'AnyclusterLeaflet' if it's defined elsewhere

const mapInteractions = new MapInteractions(anyclusterLeaflet);