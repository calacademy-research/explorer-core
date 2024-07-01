<template>
  <div>
    <h1>Collections Dashboard</h1>
    <div id="stacked-bar-chart"></div>
  </div>
</template>

<script>
import axios from 'axios';
import Plotly from 'plotly.js/lib/core';

export default {
  data() {
    return {
      totalCollections: 0
    };
  },
  mounted() {
    axios.get('http://0.0.0.0:8000/collection/')
      .then(response => {
        
        this.collectionsData = response.data;
        console.log(this.collectionsData)
        console.log(this.collectionsData.Date)

        this.createBarChart();
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  },
  methods: {
    createBarChart(){
      
      const aggregatedAmounts = {};
      const collectionsdata = this.collectionsData

      for(let i = 0; i < collectionsdata['Date'].length; i++){
        const year = collectionsdata['Date'][i].substring(0,4);
        console.log(year)
        if(!aggregatedAmounts[year]){
          aggregatedAmounts[year] = collectionsdata['Collections'][i];
        } else{
          aggregatedAmounts[year] += collectionsdata['Collections'][i];
        }
      }
      
      console.log(aggregatedAmounts)
      const xValues = Object.keys(aggregatedAmounts);
      const yValues = Object.values(aggregatedAmounts);

      const data = [{
        x: xValues,
        y: yValues,
        type: 'bar'
      }];

      console.log(data)

      const layout = {
        title: 'CAS Botany Collections Over Time (by Year)',
        xaxis: { title: 'Year cataloged' },
        yaxis: { title: 'Total number of specimens digitized' },
        barmode: 'stack' // Stacked bar mode
      };

      Plotly.newPlot('stacked-bar-chart', data, layout);
    }
  }
};
</script>



<style scoped>
/* Add any custom styles here */
</style>
