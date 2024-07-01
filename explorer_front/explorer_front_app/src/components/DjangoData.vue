<template>
  <div>
    <h1>CAS Botany Collection Images:</h1>
    <br>
    <!-- <div v-for="(item, collectionid) in collectionobjectData" :key="collectionid">{{ item.collectionobjectidData }}> -->
    <div v-for="(innerDict, collectionobjid) in collectionobjectData" :key="collectionobjid">
        <h2>Collection object {{ collectionobjid }}</h2>
        <!-- <div v-for="(image, filename) in innerDict" :key="filename">
            <img :src="image.image_file" :alt="filename" />
            <p>{{ image.collectiondesc }}</p>
            <p>{{ image.file_createddate}}</p>
            <p>{{ image.collectingevent_start }}</p> -->
            <img :src="innerDict.image_file" :alt="'[Redacted photo]'" class="image-thumbnail"/>
            <p v-if="innerDict.collection_desc">Collection notes: <i>"{{ innerDict.collection_desc }}"</i></p>
            <p>Image collection date: {{ innerDict.file_createddate}}</p>
            <p>Species collection date: {{ innerDict.collectingevent_start}}</p>
            <br>
    </div>
</div>
</template>

<script>
import axios from 'axios';

// Assuming you have a token or authentication key
const token = 'Token ' + "b38c2d04f1eeabb743e5ecbe671897cae1794974";

// Set up Axios instance with default headers
const axiosInstance = axios.create({
  baseURL: 'http://0.0.0.0:8000/',
  headers: {
    'Authorization': `${token}`,
    'Content-Type': 'application/json', // Example of another header
  },
});

export default {
    //[collectionobjectid, attachmentid, file_createddate_str, 
    //image_file, catalogeddate_str, collection_desc, 
    //collectingevent_start_str, agent_name]
  data() {
    return {
      responseData: [],
      collectionobjectData: {},
      collectionobjectidData: {},
      attachmentidData: {},
      filecreateddateData: {},
      imagefileData: [],
      catalogeddateData: [],
      collectiondescData: [],
      collectingeventstartData: [],
      agentnameData: []
    };
  },


mounted(){
        axiosInstance.get('collection_images')
        .then(response =>{

        // response.data is a dictionary of dictionaries of format: 
         /* collectiondictionary[collectionobjectid] = {
            'attachmentid': value,
            'file_createddate': value,
            'image_file': value,
            'catalogeddate': value,
            'collection_desc': value,
            'collectingevent_start': value,
            'agentname_collection': value,
            'agentname_image': value
         } */
        
            let jsonObject = JSON.parse(response.data);
            this.collectionobjectData = jsonObject
            console.log(jsonObject)
            console.log(Object.keys(jsonObject))
            console.log(Object.getOwnPropertyNames(jsonObject).length)

         // Map each inner array to the desired key
          

        })
        .catch(error =>{
            console.log(error)
        })

    }
//   mounted() {
//     axiosInstance.get('collection_images')
//       .then(response => {

//          const arrayOfArrays = response.data;
//          console.log(response.data)

//          // Map each inner array to the desired key
//         this.collectionobjectidData = arrayOfArrays.map(arr => ({ collectionobjectid: arr[0] }));
//         this.attachmentidData = arrayOfArrays.map(arr => ({ attachmentid: arr[1] }));
//         this.filecreateddateData = arrayOfArrays.map(arr => ({ filecreateddate: arr[2] }));
//         this.imagefileData = arrayOfArrays.map(arr => ({ imagefile: arr[3] }));
//         this.catalogeddateData = arrayOfArrays.map(arr => ({ catalogeddate: arr[4] }));
//         this.collectiondescData = arrayOfArrays.map(arr => ({ collectiondesc: arr[5] }));
//         this.collectingeventstartData = arrayOfArrays.map(arr => ({ collectingeventstart: arr[6] }));
//         this.agentnameData = arrayOfArrays.map(arr => ({ agentname: arr[7] }));

//         // You can also append the entire response data to a single key if needed
//         this.responseData = arrayOfArrays;
//         console.log("test")
//         console.log(JSON.stringify(this.imagefileData))
//       })
//       .catch(error => {
//         console.error('Error fetching data:', error);
//       });
//   },
};
</script>

<style scoped>
/* Add any custom styles here */
.image-thumbnail {
  max-width: 500px; /* Set the maximum width */
  max-height: 800px; /* Set the maximum height */
}
</style>