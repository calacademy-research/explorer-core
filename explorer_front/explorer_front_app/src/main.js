//import Vue from 'vue';
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import './styles/global.css';
//import * as THREE from 'three';

// Vue.config.productionTip = false;

// new Vue({
//   router,
//   render: h => h(App),
// }).$mount('#app');

createApp(App).use(router).mount('#app');