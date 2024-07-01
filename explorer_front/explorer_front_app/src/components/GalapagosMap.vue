<template>
<div>
  <div ref="mapContainer" class="map-container"></div>
  
  <div v-if="showPopup" class="iframe-popup">
    <!-- <iframe :src="'https://www.morphosource.org/uv.html#?manifest=/manifests/44b0cd03-9165-4367-b20a-8ed303a2f3c4'" width="560" height ="420" frameborder="0" allow="fullscreen; accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"></iframe> -->
    <iframe :src=popupURL width="800" height ="420" frameborder="0" allow="fullscreen; accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"></iframe>
  </div>
</div>
</template>



<script setup>
import {ref, onMounted} from 'vue';
import L from 'leaflet';

import markerImage from '@/assets/marker.png'

import 'leaflet-draw/dist/leaflet.draw.css';
import 'leaflet-draw/dist/leaflet.draw';
import islandsJSON from '../assets/galapagos.json';

const mapContainer = ref(null);
const showPopup = ref(false);
let map;
let markers = [];

let islandMarkers = {
  'Isabela Island': [{
      'latlong': [-0.0358333333, -91.3761111111],
      'popUp': 'turtle',
      'iframeURL': 'https://www.morphosource.org/uv.html#?manifest=/manifests/44b0cd03-9165-4367-b20a-8ed303a2f3c4'
  
  }],
  'Española Island': [{
    'latlong': [-1.3541666667,  -89.6598611111],
    'popUp': 'iguana',
    'iframeURL': 'https://www.morphosource.org/uv.html#?manifest=/manifests/d22b0459-dbfe-4d32-b35e-fac4e0ee33e6'
  }]
}


const iframeURLs = {
  turtle: 'https://www.morphosource.org/uv.html#?manifest=/manifests/44b0cd03-9165-4367-b20a-8ed303a2f3c4',
  iguana: 'https://www.morphosource.org/uv.html#?manifest=/manifests/d22b0459-dbfe-4d32-b35e-fac4e0ee33e6',
  'Amblyrhynchus cristatus': 'https://www.morphosource.org/uv.html#?manifest=/manifests/9bfc88a8-8f39-4993-ad89-591ca0b7948f'
};

onMounted(() => {
      map = L.map(mapContainer.value).setView([-0.207259, -90.142578], 8); 
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
      

      addIslands();
      // addMarkers();
      // setupMarkerClickEvents();

      var drawnItems = new L.FeatureGroup();
      map.addLayer(drawnItems);

      var drawControl = new L.Control.Draw({
        draw: {
          polygon: true,
          polyline: false,
          rectangle: false,
          circle: false,
          marker: false,
        },
        edit: {
          featureGroup: drawnItems,
          edit: false,
          remove: false,
        },
      });

      map.addControl(drawControl);

      map.on(L.Draw.Event.CREATED, function (event) {
      var layer = event.layer;
      drawnItems.addLayer(layer);

      // Do something with the drawn polygon, like getting its coordinates
      var polygonCoordinates = layer.getLatLngs();
      console.log("layer info", layer);
      var geoJSONinfo = layer.toGeoJSON();
      console.log("geoJSON: ", geoJSONinfo);
      console.log(JSON.stringify(geoJSONinfo.geometry.coordinates));
      console.log(polygonCoordinates);
      console.log(JSON.stringify(polygonCoordinates));

      layer.bindPopup('<p>Island <br>'+JSON.stringify(geoJSONinfo)+'</p>');
  
      });


    //return { mapContainer };
  });
  

  function addMarkers(whichIsland){

       var myIcon = L.icon({
        //iconUrl: require('./src/assets/marker.png'),
        iconUrl: markerImage,
        //iconSize: [38, 95],
        //iconAnchor: [22, 94],
        //popupAnchor: [-3, -76],
        //shadowUrl: ,
        //shadowSize: [68, 95],
        //shadowAnchor: [22, 94]
      });

      // markers = [
      //   L.marker([-0.0358333333, -91.3761111111], {icon: myIcon}).bindPopup('turtle').addTo(map),
      //   L.marker([-1.3541666667,  -89.6598611111], {icon: myIcon}).bindPopup('iguana').addTo(map),
      //   L.marker([	0.3630555556, -90.5347222222], {icon: myIcon}).bindPopup('Amblyrhynchus cristatus').addTo(map)
      // ];

      console.log("this: ", islandMarkers[whichIsland]);

      for (const islandDict of islandMarkers[whichIsland]){
        console.log("islandDict: ", islandDict);
        let latlong = islandDict['latlong'];
        console.log(latlong);
        markers = [
          L.marker(latlong, {icon: myIcon}).bindPopup(islandDict['popUp']).addTo(map)
        ];
      }
      
      setupMarkerClickEvents();
   }

  function setupMarkerClickEvents(){
      markers.forEach(marker => {
        marker.on('click', () =>{
          openPopup(marker);
        });
      });
   }

  function openPopup(marker){
      const popupURLKey = marker.getPopup().getContent();
      console.log(popupURLKey);
      popupURL.value = iframeURLs[popupURLKey]
      //console.log(popupURL)
      showPopup.value = true;
   }

function addIslands(){
    const geojsonLayer = L.geoJSON(islandsJSON, {
        style: {
          color: 'blue',
          weight: 1,
          fillOpacity: 0.1,
        },
      }).addTo(map);

      geojsonLayer.on('click', (event) =>{
        const feature = event.layer.feature;
        console.log(feature.properties.name);
        var whichIsland = feature.properties.name;
        // popupURL.value = iframeURLs['turtle'];
        // popupURL.value = true;


        //set-up addMarkers and setupMarkerClickEvents in here?
        // pass island name (feature.properties.name)

        addMarkers(whichIsland);
        //setupMarkerClickEvents();

      });
  }

const popupURL = ref('');

</script>

<style scoped>
.map-container {
  height: 850px; /* Set map container height */
  width: 80%;
}

.iframe-popup {
  position: fixed;
  top: 0;
  right: 0;
  width: 600px; /* Adjust as needed */
  height: 100%;
  background-color: white;
  z-index: 1000;
}

iframe {
  width: 100%;
  height: 100%;
}
</style>