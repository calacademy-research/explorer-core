// main.js
//import Vue from 'vue';
import {createRouter, createWebHistory} from 'vue-router';
//import App from './App.vue';
import Dashboard from './components/explorerDashboard.vue';
import DjangoData from './components/DjangoData.vue';
import Map from './components/explorerMap.vue';
import GalapagosMap from './components/GalapagosMap.vue';


const routes = [
  { path: '/', component: Dashboard },
  { path: '/images', component: DjangoData },
  { path: '/map', component: Map},
  { path: '/islands', component: GalapagosMap}
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;