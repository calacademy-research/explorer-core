<template>
  <h1>Botany collecting events around the world</h1>
  <div ref="mapContainer" style="width: 60%; height: 800px;"></div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import L from 'leaflet';
import "leaflet/dist/leaflet.css";
import axios from 'axios';
import markerImage from '@/assets/marker.png';

const mapContainer = ref(null);
let map;
let popupString;
let markers = [];

onMounted(() => {
   map = L.map(mapContainer.value).setView([0,0],2);
    //map = L.map(mapContainer.value).fitWorld();
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors',
  }).addTo(map);

//   const bounds = [[-90, -180], [90, 180]]
//   map.fitBounds(bounds);

    fetchCoordinates();

});

async function fetchCoordinates(){
    var myIcon = L.icon({
    //iconUrl: require('./src/assets/marker.png'),
    iconUrl: markerImage,
    //iconSize: [38, 95],
    iconAnchor: [22, 94],
    popupAnchor: [-3, -76],
    //shadowUrl: ,
    //shadowSize: [68, 95],
    //shadowAnchor: [22, 94]
});

    try {
        const response = await axios.get('http://0.0.0.0:8000/collection_map/');
        let data = response.data; // Assuming the API response is an array of marker data
        console.log(data)
        data = JSON.parse(data)
        // console.log(typeof(data2))
        // console.log(data2.length)
        // console.log(data2[0])
        data.forEach(item => {
            // console.log(item)
            // console.log(item.Latitude)
            // console.log(parseFloat(item.Latitude))
            const marker = L.marker([parseFloat(item.Latitude), parseFloat(item.Longitude)], {icon: myIcon}).addTo(map);
            if (item.Remarks!=null){
              popupString = "<i>\"" + item.Remarks + "\"</i><br>" + item.Geoname + "<br>" + item.Start
            }
            else{
              popupString = item.Geoname + "<br>" + item.Start
            }
            //marker.bindPopup('<br>Hi CAS!</br>')
            marker.bindPopup(popupString)
            markers.push(marker);
                    
    });
  } catch (error) {
        console.error('Error fetching data:', error);
  }    
}
</script>

<style>

</style>
